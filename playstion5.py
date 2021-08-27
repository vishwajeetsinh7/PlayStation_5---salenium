import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def playstion_5():
    global driver
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get(
        "https://www.amazon.in/Sony-CFI-1008A01R-PlayStation-5-console/dp/B08FV5GC28")

    if not elementPresent('nav-action-inner'):
        exit()
    driver.find_element_by_class_name('nav-action-inner').click()

    element = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]/span').click()
    Keys.TAB
    element = driver.find_element_by_xpath(
        '/html/body/div/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/input')
    element.send_keys("vishwajeet@mail2tor")    # enter your email
    Keys.TAB
    element = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/input')
    # enter your password don't try mine
    element.send_keys("entermypassword my password is 12345")
    Keys.ENTER
    element = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div[4]').click()

   # =====================================================================================================
   # ============================= LOG IN COMPLETED ===================================================================
   # ===================================================================================================================

    while True:
        try:
            element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='bttHider']")))
            element.click()
            break
        except:
            driver.refresh()
            continue

    while True:
        try:
            element = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='button']")))
            element.click()
            break
        except:
            driver.refresh()
            continue

        # payment part otp var


def elementPresent(className):
    try:
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, className))
        WebDriverWait(driver, 100).until(element_present)
        return 1
    except TimeoutException:
        print("time out thai gayo che fari process chalu  ")
        driver.quit()
        return 0


# start of the program
if __name__ == "__main__":
    playstion_5()
