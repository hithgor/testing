import sys
sys.path.append(".")
sys.path.append("..")
sys.path.append("...")

import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import unittest
import pytest
import time



class TestElementsPractice(unittest.TestCase):

        log = cl.customLogger(logging.DEBUG)
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driverLocation = "C:\\Users\\hithg\\Desktop\\pythonlearning\\seltest\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
       
            
        def testRadioButtons(self):
            RadioButtonBMW = self.driver.find_elements(By.XPATH,
                                                     "//input[contains(@type,'radio') and contains(@name,'cars')]")
            RadioButtonBMW[0].click()
            time.sleep(1)
            RadioButtonBMW[2].click()   
            time.sleep(1)


        def testSelectExample(self):
            SelectExample = self.driver.find_element_by_id("carselect")
            sel = Select(SelectExample)
            sel.select_by_value("honda")
            time.sleep(1)


        def testSelectExample2(self):
            SelectExample = self.driver.find_element_by_id("multiple-select-example")
            sel = Select(SelectExample)
            sel.select_by_value("orange")
            time.sleep(1)

        def testCheckboxExample3(self):
            CheckboxExample = self.driver.find_element_by_id("bmwcheck")
            CheckboxExample.click()
            time.sleep(1)
            CheckboxExample = self.driver.find_element_by_id("hondacheck")
            CheckboxExample.click()
            time.sleep(1)

        def testSwitchWindow(self):
            #Find parent handle --> main window
            parentHandle = self.driver.current_window_handle
            print("Parent Handle: " + parentHandle)
            #Find open window button and click it
            openWindowButton = self.driver.find_element_by_id("openwindow")
            openWindowButton.click()
            #find all handles
            allHandles = self.driver.window_handles
            
            #find opened handle, switch to it, make stuff and close
            for handle in allHandles:
                if handle not in parentHandle:
                    self.driver.switch_to.window(handle)
                    searchBox = self.driver.find_element_by_id("search-courses")
                    searchBox.send_keys("Python 3 from scratch")
                    time.sleep(2)
                    searchButton = self.driver.find_element_by_id("search-course-button")
                    searchButton.click()
                    time.sleep(1)
                    self.driver.close()
                    break

            self.driver.switch_to.window(parentHandle)


        def testSwitchTab(self):
            #Find parent handle --> main window
            parentHandle = self.driver.current_window_handle
            print("Parent Handle: " + parentHandle)
            #Find open window button and click it
            openWindowButton = self.driver.find_element_by_id("opentab")
            openWindowButton.click()
            #find all handles
            allHandles = self.driver.window_handles
            
            #find opened handle, switch to it, make stuff and close
            for handle in allHandles:
                if handle not in parentHandle:
                    self.driver.switch_to.window(handle)
                    searchBox = self.driver.find_element_by_id("search-courses")
                    searchBox.send_keys("Python 3 from scratch")
                    time.sleep(2)
                    searchButton = self.driver.find_element_by_id("search-course-button")
                    searchButton.click()
                    time.sleep(3)
                    self.driver.close()
                    break

            self.driver.switch_to.window(parentHandle)
            self.driver.close

        def testAlertExample(self):
            #clicking and confirming alert
            textField = self.driver.find_element_by_id("name")
            textField.send_keys("Starving Tester-Wannabe")
            alertButton = self.driver.find_element_by_id("alertbtn")
            alertButton.click()
            alertFrame = self.driver.switch_to.alert
            time.sleep(2)
            alertFrame.accept()


        def testHideShow(self):
            #click hide/show buttons and assert visibility of an element
            showButton = self.driver.find_element_by_id("show-textbox")
            hideButton = self.driver.find_element_by_id("hide-textbox")
            textField = self.driver.find_element_by_id("displayed-text")
            textField.send_keys("Hire me, please")
            time.sleep(2)
            hideButton.click()
            time.sleep(1)
            assert not textField.is_displayed()
            showButton.click()
            assert textField.is_displayed()
            textField.clear()
            textField.send_keys("I'm starving.")
            time.sleep(2)
            hideButton.click()

        def testMouseHover(self):
            #Hover to element, check visibility of scrolldown and click the first
            mouseHoverButton = self.driver.find_element_by_id("mousehover")
            itemToBeSeenAfterHovering = self.driver.find_element_by_xpath(
                                        ".//div[@class='mouse-hover-content']//a[text()='Top']")
            actions = ActionChains(self.driver)
            actions.move_to_element(mouseHoverButton).perform()
            time.sleep(1)
            assert itemToBeSeenAfterHovering.is_displayed()
            actions.move_to_element(itemToBeSeenAfterHovering).click().perform()

        def testIframeSwitching(self):
            self.driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(2)
            self.driver.switch_to.frame("iframe-name")
            time.sleep(1)
            try:
                searchBox = self.driver.find_element_by_id("search-courses")
                searchBox.send_keys("I can into iFrame")
            except NoSuchElementException:
                print("  iFRAME nie wczytuje się w oprogramowaniu testowym.")
            
            time.sleep(2)
            self.driver.switch_to.default_content()
            self.driver.execute_script("window.scrollBy(0, -300);")




            





