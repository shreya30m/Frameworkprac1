**OrangeHRM Selenium Automation Framework**
This repository contains a Selenium-based automation framework for testing the OrangeHRM site. The framework is designed to automate end-to-end tests for various functionalities such as user authentication, employee management, leave management, and more.
Project Structure

The framework follows a modular structure, organized into the following directories:

    1)Configuration: Contains configuration files for environment settings, browser configurations, and credentials.
    2)Logs: Stores log files generated during test execution.
    3)PageObjects: Houses Page Object Model (POM) classes representing web pages and their elements.
    4)Screenshots: Stores screenshots captured during test execution, useful for debugging failures.
    5)TestCases: Contains Python scripts defining the automated test cases using Selenium WebDriver.
    6)Testdata: Holds test data files used for parameterization or data-driven testing.
    7)Utilities: Contains utility functions and helper classes for common tasks such as WebDriver initialization, custom waits, and logging.

Prerequisites
    Python 3.x installed on your system.
    Python package manager (pip) installed.
    WebDriver executable for your preferred browser (e.g., ChromeDriver for Google Chrome).

Setup
    Clone this repository to your local machine:
git clone <repository-url>
Navigate to the project directory
cd orangehrm-selenium-automation
Install project dependencies using pip:
pip install -r requirements.txt
Download the appropriate WebDriver executable (e.g., ChromeDriver) and ensure it's in your system's PATH.

Writing and Running Tests
    Define test scenarios in Python scripts located in the TestCases directory.
    Utilize the Page Object Model (POM) pattern to encapsulate page interactions in separate Python classes located in the PageObjects directory.
    Use WebDriver methods and assertions to interact with web elements and verify expected outcomes.
    Execute test scripts and monitor test execution using your preferred test runner tool.
