from termcolor import colored
import emoji


class RunnerService:

    @staticmethod
    def run_tests_for(drivers: list, tests: list) -> None:

        for driver in drivers:
            print('Test in browser ' + driver.__module__)
            for test in tests:
                test_methods = [func for func in dir(test) if callable(getattr(test, func)) and func.startswith("test")]
                auth_test_methods = [func for func in dir(test) if
                                     callable(getattr(test, func)) and func.startswith("auth_test")]
                initializedTest = test(driver)

                for test_method in test_methods:
                    try:
                        methodCallable = getattr(initializedTest, test_method)
                        methodCallable()

                        print(colored(emoji.emojize(" :check_mark:") + ' [U] Done: ', 'green') + initializedTest.__module__ + "." + test_method )
                    except Exception as e:
                        print(colored(emoji.emojize(":cross_mark:") + " [U] Failed: ", 'red') + initializedTest.__module__ + "." + test_method + str(e))

                        driver.quit()

                for auth_test_method in auth_test_methods:
                    try:
                        initializedTest.authorize(initializedTest.authorizator(driver))
                        methodCallable = getattr(initializedTest, auth_test_method)
                        methodCallable()

                        print(colored(emoji.emojize(" :check_mark:") + " [A]  Done: ", 'green') + initializedTest.__module__ + "." + auth_test_method)
                    except Exception as e:
                        print(colored(emoji.emojize(" :cross_mark:") + " [A] Failed: ", 'red') + initializedTest.__module__ + "." + auth_test_method + str(e))

                        driver.quit()