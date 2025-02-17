# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSelectorshub():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_selectorshub(self):
    self.driver.get("https://app.pluralsight.com/id/signin/?redirectTo=https%3A%2F%2Fapp.pluralsight.com%2Flibrary%2Fcourses%2Frelational-database-design%2Ftable-of-contents/c/3f2ad031-a8ef-4156-b806-3d9ee51d5811")
    self.driver.set_window_size(1296, 696)
    self.driver.find_element(By.ID, "prompt-textarea").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.execute_script("window.scrollTo(0,0)")
    element = self.driver.find_element(By.CSS_SELECTOR, ".h-\\[72px\\]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(3) .relative:nth-child(1) > .group .relative").click()
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
  
