from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Services.Authorization.AdminAuthorization import AdminAuthorization
from Services.BaseTest.BaseTest import BaseTest


class CategoryTest(BaseTest):

    def authorizator(self, driver: WebDriver):
        return AdminAuthorization(driver)

    def test_laravel_page(self):
        self.get_endpoint('/')

    def auth_test_category_list(self):
        self.get_driver().implicitly_wait(10)
        self.get_driver().find_element(By.XPATH, "//button[@class='shrink-0 flex items-center justify-center "
                                                 "w-10 h-10 text-primary-500 rounded-full "
                                                 "filament-sidebar-open-button hover:bg-gray-500/5 "
                                                 "focus:bg-primary-500/10 focus:outline-none lg:hidden']//*["
                                                 "name()='svg']//*[name()='path' and contains(@stroke-linecap,"
                                                 "'round')]").click()

        # Open categories
        self.get_driver().find_element(By.XPATH, "//span[normalize-space()='Categories']").click()
        self.get_driver().implicitly_wait(10)
        self.get_driver().find_element(By.CSS_SELECTOR, 'body').screenshot('./screenshots/screen' + self.get_driver().__module__ + self.__module__ + '.jpg')
        displayed = self.get_driver().find_element(By.XPATH, "//h1[@class='text-2xl font-bold tracking-tight md:text-3xl filament-header-heading']").is_displayed()

        if displayed:
            print('Category list successfully')
        else:
            Exception('Cannot show categories list')

    def auth_test_nothing(self):

        self.get_driver().find_element(By.CSS_SELECTOR, 'div')
