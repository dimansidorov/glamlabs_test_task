import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class InitDriver:
    def __enter__(self):
        options = Options()
        # options.add_argument("--headless")
        service = Service('chromedriver')
        self.driver = webdriver.Chrome(options=options, service=service)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


def get_instagram_photo_links(username: str, count: int):
    with InitDriver() as driver:
        profile_url = f"https://www.instagram.com/{username}/"
        driver.get(profile_url)
        time.sleep(3)

        driver.execute_script("window.scrollTo(0, 8000);")

        images = driver.find_elements(By.CSS_SELECTOR, 'div._aagv img')
        images = [image.get_attribute('src') for image in images]

        return images


print(get_instagram_photo_links('dimansidorov', 3))