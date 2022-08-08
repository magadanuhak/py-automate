from Services.DriverService import DriverService
from Services.RunnerService import RunnerService
from Tests.Country.CategoryTest import CategoryTest

drivers = [
    DriverService.get_chrome(),
    DriverService.get_firefox(),
    DriverService.get_opera(),
    DriverService.get_brave()
]

tests = [
    CategoryTest,
]

RunnerService.run_tests_for(drivers, tests)

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
