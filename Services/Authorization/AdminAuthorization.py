from abc import ABC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Services.Authorization.AuthorizationInterface import AuthorizationInterface
from Services.BaseTest.BaseTest import BaseTest


class AdminAuthorization(AuthorizationInterface, ABC):

    def login(self) -> WebDriver:
        driver = self.driver
        driver.fullscreen_window()
        driver.get('https://doit-api.powerit.dev/admin/login')
        driver.implicitly_wait(15)

        driver.find_element(By.CSS_SELECTOR, '#email').send_keys('root@domain.com')
        driver.find_element(By.CSS_SELECTOR, '#password').send_keys('123456789')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        driver.implicitly_wait(15)

        return driver
