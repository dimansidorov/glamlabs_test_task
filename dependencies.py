from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import asyncio

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SLEEP_TIME = 2
URL = 'www.instagram.com'


class EmptyPageException(Exception):
    pass


class PageLoadError(Exception):
    pass


class InitDriver:
    async def __aenter__(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--start-maximized')

        self.driver = webdriver.Chrome(options=options)
        return self.driver

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


async def get_instagram_photo_links(username: str, count: int):
    async with InitDriver() as driver:
        profile_url = f"https://{URL}/{username}/"
        driver.get(profile_url)
        await asyncio.sleep(SLEEP_TIME)

        error_element = driver.find_elements(
            By.CSS_SELECTOR,
            'span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.x1ms8i2q.xo1l8bm.x5n08af.x4zkp8e.xw06pyt.x10wh9bi.x1wdrske.x8viiok.x18hxmgj'
        )
        if error_element:
            raise PageLoadError()

        images = []
        while len(images) < count:
            try:
                load_more_button = WebDriverWait(driver, SLEEP_TIME).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'button._any9._anya._anyc'))
                )
                load_more_button.click()
            except Exception as err:
                print(err)

            visible_images = driver.find_elements(By.CSS_SELECTOR, 'div._aagv img')
            visible_images = [image.get_attribute('src') for image in visible_images]

            new_images = [image for image in visible_images if image not in images]
            images.extend(new_images)

            if len(images) == 0:
                raise EmptyPageException

            elif len(new_images) < 12:
                break

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            await asyncio.sleep(SLEEP_TIME)

        return images[:count] if count < len(images) else images
