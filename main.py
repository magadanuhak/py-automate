from Services.DriverService import DriverService
from Tests.Country.CountryTest import CountryTest

drivers = [
    DriverService.get_chrome(),
]

tests = [
    CountryTest,
]


for driver in drivers:
    for test in tests:
        test_methods = [func for func in dir(test) if callable(getattr(test, func)) and func.startswith("test")]
        auth_test_methods = [func for func in dir(test) if callable(getattr(test, func)) and func.startswith("auth_test")]
        initializedTest = test(driver)

        for test_method in test_methods:
            methodCallable = getattr(initializedTest, test_method)
            methodCallable()

        for auth_test_method in auth_test_methods:
            initializedTest.authorize(initializedTest.authorizator(driver))
            methodCallable = getattr(initializedTest, auth_test_method)
            methodCallable()
    #
#
# f = open('credentials.json')
#
# credentials = json.load(f)
#
# chrome.get('https://facebook.com/')
#
# chrome.implicitly_wait(10)
#
# chrome.find_element(By.ID, 'email').send_keys(credentials['email'])
# chrome.find_element(By.ID, 'pass').send_keys(credentials['password'])
# chrome.find_element(By.NAME, 'login').click()
#
# chrome.implicitly_wait(15)
#
# chrome.find_element(By.CSS_SELECTOR, '[aria-label="Îmi place"]').click()
