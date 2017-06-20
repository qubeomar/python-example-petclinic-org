import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import HTMLTestRunner


class HomePageMenuLinkTests(unittest.TestCase):
    SELENIUM_SERVER_URL = "http://localhost:1234/wd/hub"
    TARGET_PAGE_URL = "http://myjavahost/static/home.html"
    
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=HomePageMenuLinkTests.SELENIUM_SERVER_URL,
            desired_capabilities= DesiredCapabilities.FIREFOX)
        self.driver.get(HomePageMenuLinkTests.TARGET_PAGE_URL)


    def test_about_menu_link(self):
        driver = self.driver
        elem = driver.find_element_by_link_text("about")
        elem.send_keys("about")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_about_services_link(self):
        driver = self.driver
        elem = driver.find_element_by_link_text("services")
        elem.send_keys("services")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_about_links_link(self):
        driver = self.driver
        elem = driver.find_element_by_link_text("links")
        elem.send_keys("links")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_about_contacts_link(self):
        driver = self.driver
        elem = driver.find_element_by_link_text("contacts")
        elem.send_keys("contacts")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    HomePageMenuLinkTests.SELENIUM_SERVER_URL = sys.argv[1]
    HomePageMenuLinkTests.TARGET_PAGE_URL = sys.argv[2]
    suite = unittest.TestLoader().loadTestsFromTestCase(HomePageMenuLinkTests)
    outfile = open('dist' + "/SmokeTestReport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title = 'PyPet Test Report', description = 'UI selenium test')
    runner.run(suite)
    #unittest.TextTestRunner(verbosity=2).run(suite)
