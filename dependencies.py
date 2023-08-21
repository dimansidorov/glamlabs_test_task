import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import asyncio

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SLEEP_TIME = 2
URL = 'www.instagram.com'


class EmptyPageException(Exception):
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
        print("start")
        profile_url = f"https://{URL}/{username}/"
        driver.get(profile_url)
        time.sleep(SLEEP_TIME)

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
            time.sleep(SLEEP_TIME)

        print("end")
        return images[:count] if count < len(images) else images
