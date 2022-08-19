from Services.DriverService import DriverService


def before_all(context):
    context.browser = DriverService.get_chrome()
    context.browser.fullscreen_window()


def after_all(context):
    pass
    # context.browser.quit()
