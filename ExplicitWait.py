from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

# This is a Python class that sets up a web driver for Microsoft Edge using the unittest module.
class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')
# This function opens Google website and waits for the presence of an element with name 'q' using explicit wait.
    def test_using_explecit(self):
        driver = self.driver
        driver.get('https://www.google.com')
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.NAME, 'q')
                )
            )
        finally:
            driver.quit()
# `if __name__ == '__main__':` is a conditional statement that checks if the current module is being
# run as the main program. If it is, then `unittest.main()` is called, which runs the test cases
# defined in the class `using_unittest`. This allows the module to be run as a standalone program and
# execute the test cases.
if __name__ == '__main__':
    unittest.main()