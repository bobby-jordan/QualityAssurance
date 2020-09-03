# Import unittest module for creating unit tests
import unittest
import time
from selenium import webdriver
import win32api
import win32com.client
import pythoncom

class PythonOrgSearchFireFox(unittest.TestCase):
    def setUp(self):
        # Initialize the Firefox driver
        self.driver = webdriver.Firefox()

        self.driver.maximize_window()

    def test_search_in_python_firefox(self):
        driver = self.driver

        driver.get('http://www.google.com')

        self.assertIn("Google", driver.title)

        search_box = driver.find_element_by_name('q')

        search_box.send_keys('Selenium')

        assert "No results found." not in driver.page_source

        # Submit the search box form
        search_box.submit()

        # Another pause so we can see what's going on
        time.sleep(15)

        # Find and select the search box element on the page
        search_box = driver.find_element_by_class_name('r')
        # Make sure the results page returned something

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
        self.driver.close()


# Boilerplate code to start the unit tests
if __name__ == "__main__":
    unittest.main()