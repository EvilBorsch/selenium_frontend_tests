from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def clear(el):
    count = len(el.get_attribute("value"))
    for i in range(count):
        el.send_keys(Keys.BACKSPACE)


class BaseSteps(object):
    def __init__(self, driver: Remote):
        self.driver = driver

    def wait_until_and_get_elem_by_xpath(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 15, 0.1).until(EC.visibility_of_element_located((By.XPATH, elem)))

    def wait_until_and_get_elem_by_css(self, elem) -> WebElement:
        return WebDriverWait(self.driver, 15, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elem)))

    def wait_for_url(self, url):
        return WebDriverWait(self.driver, 15, 0.1).until(EC.url_to_be(url))

    def fill_input(self, path, info):
        el = self.wait_until_and_get_elem_by_xpath(path)
        el.click()
        clear(el)
        el.send_keys(info)
        el.submit()

    def get_element_text(self, path) -> str:
        try:
            return self.driver.find_element_by_xpath(path).text
        except Exception:
            return ""
