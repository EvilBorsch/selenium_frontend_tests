from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BaseComponent(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_until_and_get_elem_by_xpath(self, elem):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elem)))