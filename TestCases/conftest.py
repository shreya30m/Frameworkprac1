from selenium import webdriver
import pytest

driver = None

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    return driver


def pytest_addoption(parser):  ###This will get value from CLI/hooks
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):  # This will return the browser to setup method
    return request.config.getoption("--browser")


# ##########pYTEST HTML REPORTS########################
# # It is hook for adding environment infor to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'
#     config._metadata['Tester'] = 'Shreya'
#
# #It is hook to delete/modify environment info to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("plugins",None)
#

