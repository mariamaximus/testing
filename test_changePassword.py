from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from locators import Locators


import time
import pytest


@pytest.fixture()
def setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    driver.maximize_window();
    driver.get("https://identity.flickr.com/");
    print(driver.title);



    myEmail = "maria.ossama10@yahoo.com";
    myPassword = "000011112222m";

    emailAddressField = driver.find_element_by_id("login-email");
    nextButton = driver.find_element_by_xpath(Locators.nextButtonXpath);
    emailAddressField.send_keys(myEmail);
    nextButton.click();
    driver.implicitly_wait(60)
    passwordField = driver.find_element_by_id("login-password");
    passwordField.send_keys(myPassword);
    signInButton = driver.find_element_by_xpath(Locators.signInButtonXpath);
    signInButton.click();
    driver.implicitly_wait(60)
    pageTitle=driver.title;
    yield
    driver.close()
    driver.quit()




def test_acceptablePassword(setup):
    #go to my settings
    ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
    ProfileButton.click();
    time.sleep(2);
    settingsButton=driver.find_element_by_xpath(Locators.settingsButtonXpath);
    settingsButton.click();

    editPassword=driver.find_element_by_xpath(Locators.editPasswordXpath);
    editPassword.click();


    ## CORRECT PASSWORD
    currentPass="000011112222m";
    ## ACCEPTABLE NEW PASSWORD
    newPass="1234567891011m";


    currentPasswordInput=driver.find_element_by_xpath(Locators.currentPasswordInputXpath);
    currentPasswordInput.send_keys(currentPass);
    newPasswordInput=driver.find_element_by_xpath(Locators.newPasswordInputXpath);
    newPasswordInput.send_keys(newPass);
    changePasswordButton=driver.find_element_by_xpath(Locators.changePasswordButtonXpath);
    changePasswordButton.click();
    time.sleep(2);
    currURL= driver.current_url;
    print(currURL);
    completeURL="https://identity.flickr.com/change-complete/change-password";
    assert currURL==completeURL , "NO Change"

    gotItButton=driver.find_element_by_xpath(Locators.gotItButtonXpath);
    gotItButton.click();

    time.sleep(2);
    currURL=driver.current_url;
    print(currURL);
    accURL="https://www.flickr.com/account";

    assert currURL==accURL,"failed to redirect to account";