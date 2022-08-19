from Services.DriverService import DriverService
from Services.RunnerService import RunnerService
from Tests.Modular.Category.CategoryTest import CategoryTest

drivers = [
    DriverService.get_chrome()
]

tests = [
    CategoryTest,
]

RunnerService.run_tests_for(drivers, tests)
