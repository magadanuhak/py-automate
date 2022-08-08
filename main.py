from Services.DriverService import DriverService
from Services.RunnerService import RunnerService
from Tests.Category.CategoryTest import CategoryTest

drivers = [
    DriverService.get_chrome(),
    DriverService.get_firefox(),
]

tests = [
    CategoryTest,
]

RunnerService.run_tests_for(drivers, tests)
