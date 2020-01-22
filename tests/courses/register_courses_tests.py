import sys
sys.path.append(".")
sys.path.append("..")
sys.path.append("...")

from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import os
#print (os.getcwd())
from selenium import webdriver
import os
from base.webdriverfactory import WebDriverFactory

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@pytest.mark.filterwarnings("ignore:PytestCollectionWarning")
class RegisterCoursesTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    @pytest.mark.filterwarnings("ignore:PytestWarning")
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

#    def test_letslogin(self):
  #      wdf = WebDriverFactory("chrome")
  #      driver = wdf.getWebDriverInstance()
 #       logInstance = LoginPage(driver = driver)
  #      logInstance.login(email="test@email.com", password="abcabc")
    
    @pytest.mark.filterwarnings("ignore:PytestWarning")
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse()
        result = self.courses.verifyEnrollFailed()
        print(result)
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
