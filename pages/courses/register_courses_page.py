import sys
sys.path.append(".")
sys.path.append("..")
sys.path.append("...")
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    
    #Locators
    _search_box = "search-courses"
    _course = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _toe_checkbox = "agreed_to_terms_checkbox"
    _cc_postal = "postal"
    _submit_enroll = "//button[@id='confirm-purchase']/parent::div"
    _submit_enroll_enabled = "//button[@class='btn btn-primary spc__button']/parent::div"
    _enroll_error_message = ""


    def enterCourseName(self, name):
        self.sendKeys(name, locator = self._search_box)
        self.elementClick(locator="search-course-button")
    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator = self._course, locatorType = 'xpath')
    
    def clickOnEnrollButton(self):
        self.elementClick(locator = self._enroll_button)

    def enterCardNum(self, num):
        self.switchToFrame(name="__privateStripeFrame8")
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()
    def enterCardExp(self, exp):
        self.switchToFrame(name="__privateStripeFrame9")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()
    def enterCardCVV(self, cvv):
        self.switchToFrame(name="__privateStripeFrame10")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()
    def enterCardPostal(self, postal):
        self.switchToFrame(name="__privateStripeFrame11")
        self.sendKeys(postal, locator= self._cc_postal, locatorType = 'name')
        self.switchToDefaultContent()
    def clickEnrollSubmitButton(self):
        self.waitForElement(self._submit_enroll_enabled, locatorType="xpath")
        self.elementClick(locator= self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv, postal):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterCardPostal(postal)


    def enrollCourse(self, num="4402645405558113", exp="0125", cvv="589", postal = "21134"):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv, postal)
        self.elementClick(locator = self._toe_checkbox)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element = messageElement)
        return result

    