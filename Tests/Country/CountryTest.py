from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Services.Authorization.AdminAuthorization import AdminAuthorization
from Services.BaseTest.BaseTest import BaseTest


class CountryTest(BaseTest):

    def authorizator(self, driver: WebDriver):
        authorization = AdminAuthorization(driver)
        return authorization

    def test_country_list(self):
        pass
        # self.get_driver().implicitly_wait(10)

        # self.get_endpoint('/admin/countries')

    def auth_test_country_list(self):
        self.get_driver().find_element(By.XPATH, "//button[@class='shrink-0 flex items-center justify-center "
                                                 "w-10 h-10 text-primary-500 rounded-full "
                                                 "filament-sidebar-open-button hover:bg-gray-500/5 "
                                                 "focus:bg-primary-500/10 focus:outline-none lg:hidden']//*["
                                                 "name()='svg']//*[name()='path' and contains(@stroke-linecap,"
                                                 "'round')]").click()

        # Open categories
        self.get_driver().find_element(By.XPATH, "//span[normalize-space()='Categories']").click()
        self.get_driver().implicitly_wait(10)

        displayed = self.get_driver().find_element(By.XPATH, "//h1[@class='text-2xl font-bold tracking-tight md:text-3xl filament-header-heading']").is_displayed()

        if displayed:
            print('Category list successfull')
        else:
            Exception('Canot show categories list')

        self.get_driver().quit()
