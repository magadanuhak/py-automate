from selenium.webdriver.remote.webdriver import WebDriver
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    url = 'https://doit.powerit.dev/auth/login'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    locators = {
        'username': ('CSS', "#email-input"),
        'password': ('CSS', '#password-input'),
        'login_btn': ('css', 'button[type="submit"]'),
        'forgot_password_link': ('css', 'button[type="submit"]'),
        'register_link': ('css', 'button[type="submit"]'),

    }

    def select_username(self, username):
        self.username.set_text(username)

    def select_password(self, password):
        self.password.set_text(password)

    def click_login(self):
        self.login_btn.click()

    def click_forgot_password(self):
        self.forgot_password_link.click()

    def click_register(self):
        self.register_link.click()
