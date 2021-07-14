from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from locators import Locators
from locators_phase3 import locatorsPhase3

import pytest
import time

@pytest.fixture()
def setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    driver.maximize_window();
    driver.get("https://www.flickrclone.tech/login");
    myEmail = "max@gmail.com";
    myPassword = "Mm$123456789";

    emailAddressField = driver.find_element_by_id("login-email-field");
    emailAddressField.send_keys(myEmail);
    driver.implicitly_wait(30)
    passwordField = driver.find_element_by_id("login-psswrd-field");
    passwordField.send_keys(myPassword);
    signInButton = driver.find_element_by_xpath(locatorsPhase3.signInButtonXpath);
    signInButton.click();
    driver.implicitly_wait(100)
    pageURL = driver.current_url;
    expectedPageURL="https://www.flickrclone.tech/home"
    #assert pageURL==expectedPageURL , "Login failed"
    headerYou=driver.find_element_by_xpath(locatorsPhase3.headerYouXpath);
    # hoverYou = ActionChains(driver).move_to_element(headerYou)
    # hoverYou.perform()
    headerYou.click()
    yield
    driver.close()
    driver.quit()


def test_seeFollowers(setup):
    # go to my settings
    #print("sssss")
    followersList=driver.find_element_by_xpath(locatorsPhase3.followersListXpath)
    followersList.click()
    follwersSearchBar=driver.find_element_by_xpath(locatorsPhase3.follwersSearchBarXpath)
    search=False
    try:
        driver.find_element_by_xpath(locatorsPhase3.follwersSearchBarXpath)
        search=False
    except NoSuchElementException:
        search=True

    assert search == True,"falied to search in followers list"





