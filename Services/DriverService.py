from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.core.utils import ChromeType


class DriverService:

    @staticmethod
    def get_chrome() -> WebDriver:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    @staticmethod
    def get_firefox() -> WebDriver:
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    @staticmethod
    def get_brave() -> WebDriver:
        return webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
