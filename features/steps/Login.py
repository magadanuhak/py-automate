from behave import *
from Pages.LoginPage import LoginPage

use_step_matcher("re")


@given("I go to login page")
def step_impl(context):

    context.browser.delete_all_cookies()
    context.browser.get('https://doit.powerit.dev/auth/login')


@when("I fill login form")
def step_impl(context):
    lp = LoginPage(context.browser)

    lp.select_username('root@domain.com')
    lp.select_password('123456789')


@when("Submit login form")
def step_impl(context):
    LoginPage(context.browser).click_login()


@then("I was redirected to home page as logged in user")
def step_impl(context):

    context.browser.implicitly_wait(15)


