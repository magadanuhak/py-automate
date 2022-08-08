import abc
import json
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver

from Services.Authorization import AuthorizationInterface


class BaseTest:

    def __init__(self, driver: WebDriver):
        self.__load_config()
        self.__driver = driver


    def get_endpoint(self, endpoint: str) -> WebDriver:
        self.__driver.get(self.site + endpoint)

        return self.__driver

    def get_driver(self):
        return self.__driver

    def __load_config(self):
        config_file = open('config.json')

        config = json.load(config_file)

        self.site = config['site']

    @abc.abstractmethod
    def authorizator(self):
        pass

    def authorize(self, authorizationObject):
       authorizationObject.login()
