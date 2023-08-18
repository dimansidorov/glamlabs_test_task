from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import asyncio

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SLEEP_TIME = 2
URL = 'www.instagram.com'


class InitDriver:
    async def __aenter__(self):
        options = Options()
        # options.add_argument("--headless")
        service = Service('chromedriver')
        self.driver = webdriver.Chrome(
            options=options,
            # service=service
        )
        return self.driver

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


async def get_instagram_photo_links(username: str, count: int):
    async with InitDriver() as driver:
        profile_url = f"https://{URL}/{username}/"
        driver.get(profile_url)
        await asyncio.sleep(SLEEP_TIME)

        images = []

        while len(images) < count:
            try:
                load_more_button = WebDriverWait(driver, SLEEP_TIME).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'button._any9._anya._anyc'))
                )
                load_more_button.click()
            except:
                pass

            # script = """
            # var popupElement = document.querySelector('.x1ja2u2z.x1afcbsf.x1a2a7pz.x6ikm8r.x10wlt62.x71s49j.x6s0dn4.x78zum5.xdt5ytf.xl56j7k.x1n2onr6');
            # if (popupElement) {
            #     popupElement.style.display = 'none';
            # }
            # """
            # driver.execute_script(script)

            visible_images = driver.find_elements(By.CSS_SELECTOR, 'div._aagv img')
            visible_images = [image.get_attribute('src') for image in visible_images]

            new_images = [image for image in visible_images if image not in images]
            images.extend(new_images)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            await asyncio.sleep(SLEEP_TIME)

        return images[:count]
