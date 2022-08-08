import abc

from selenium.webdriver.remote.webdriver import WebDriver


class AuthorizationInterface(metaclass=abc.ABCMeta):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @abc.abstractmethod
    def login(self) -> WebDriver:
        pass
