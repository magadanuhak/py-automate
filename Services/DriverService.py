import selenium
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class DriverService:

    @staticmethod
    def get_chrome() -> WebDriver:
        return selenium.webdriver.Chrome()

    @staticmethod
    def get_firefox() -> WebDriver:
        return selenium.webdriver.Firefox()

    @staticmethod
    def get_safari() -> WebDriver:
        return selenium.webdriver.Safari()

    @staticmethod
    def get_edge() -> WebDriver:
        return selenium.webdriver.Edge()

    @staticmethod
    def get_chromium_edge() -> WebDriver:
        return selenium.webdriver.ChromiumEdge()
