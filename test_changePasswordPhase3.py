from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from locators_phase3 import locatorsPhase3
from locators import Locators


import time
import pytest


@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    driver.maximize_window();
    driver.get("https://www.flickrclone.tech/login");
    global myEmail
    myEmail = "mimi@gmail.com";
    global myPassword
    myPassword= "Mm$123456789";

    emailAddressField = driver.find_element_by_id("login-email-field");
    emailAddressField.send_keys(myEmail);
    driver.implicitly_wait(30)
    passwordField = driver.find_element_by_id("login-psswrd-field");
    passwordField.send_keys(myPassword);
    signInButton = driver.find_element_by_xpath(locatorsPhase3.signInButtonXpath);
    signInButton.click();
    driver.implicitly_wait(100)
    pageURL = driver.current_url;
    expectedPageURL = "https://www.flickrclone.tech/home"
    time.sleep(2);

    # go to my settings
    profileButton = driver.find_element_by_xpath(locatorsPhase3.profileButtonXpath)
    profileButton.click()
    time.sleep(2);
    yield
    driver.close()
    driver.quit()


def test_unacceptablePassword(setup):
    #go to my settings
    URL = "https://www.flickrclone.tech/AccountSettings"
    currURL = driver.current_url
    assert URL == currURL, "failed to go to settings"

    changePassword = driver.find_element_by_xpath(locatorsPhase3.changePasswordXpath);
    changePassword.click();
    time.sleep(1);
    URL = "https://www.flickrclone.tech/editPass";
    currURL = driver.current_url;
    assert URL == currURL, "failed to redirect to change password page"
    #profileButton.click();
    time.sleep(2);
    currentPassword=driver.find_element_by_xpath(locatorsPhase3.currentPasswordXpath)
    currentPassword.send_keys(myPassword)
    time.sleep(1)
    newPassword=driver.find_element_by_xpath(locatorsPhase3.newPasswordXpath)
    newPass="123456"
    newPassword.send_keys()



    changePasswordButton=driver.find_element_by_xpath(locatorsPhase3.changePasswordButtonXpath);
    changePasswordButton.click();
    time.sleep(2);

    errorMessage = False
    try:
        mess = driver.find_element_by_xpath(locatorsPhase3.errorMessageXpath).text;
        errorMessage = True

    except NoSuchElementException:
        errorMessage = False
    assert errorMessage == True, "No message displayed to inform that this is an invalid password although it wasn't updated in the database"

    driver.find_element_by_xpath(locatorsPhase3.logoutXpath).click()
    driver.find_element_by_xpath(locatorsPhase3.loginXpath).click()
    time.sleep(5)

    emailAddressField = driver.find_element_by_id("login-email-field");
    emailAddressField.send_keys(myEmail);
    driver.implicitly_wait(30)
    passwordField = driver.find_element_by_id("login-psswrd-field");
    passwordField.send_keys(newPass);
    signInButton = driver.find_element_by_xpath(locatorsPhase3.signInButtonXpath);
    signInButton.click();
    driver.implicitly_wait(100)
    pageURL = driver.current_url;
    expectedPageURL = "https://www.flickrclone.tech/home"
    time.sleep(2);


def test_acceptablePassword(setup):
    #go to my settings
    URL = "https://www.flickrclone.tech/AccountSettings"
    currURL = driver.current_url
    assert URL == currURL, "failed to go to settings"

    changePassword = driver.find_element_by_xpath(locatorsPhase3.changePasswordXpath);
    changePassword.click();
    time.sleep(1);
    URL = "https://www.flickrclone.tech/editPass";
    currURL = driver.current_url;
    assert URL == currURL, "failed to redirect to change password page"
    #profileButton.click();
    time.sleep(2);
    currentPassword=driver.find_element_by_xpath(locatorsPhase3.currentPasswordXpath)
    currentPassword.send_keys(myPassword)
    time.sleep(1)
    newPassword=driver.find_element_by_xpath(locatorsPhase3.newPasswordXpath)
    newPass="MMmm$1234567"
    newPassword.send_keys(newPass)
    time.sleep(2)



    changePasswordButton=driver.find_element_by_xpath(locatorsPhase3.changePasswordButtonXpath);
    changePasswordButton.click();
    time.sleep(2);

    okGotIt = driver.find_element_by_xpath(locatorsPhase3.okGotItXpath)
    okGotIt.click()
    time.sleep(2)

    driver.find_element_by_xpath(locatorsPhase3.logoutXpath).click()
    time.sleep(2)
    driver.find_element_by_xpath(locatorsPhase3.loginXpath).click()
    time.sleep(5)

    emailAddressField = driver.find_element_by_id("login-email-field");
    emailAddressField.send_keys(myEmail);
    driver.implicitly_wait(30)
    passwordField = driver.find_element_by_id("login-psswrd-field");
    passwordField.send_keys(newPass);
    signInButton = driver.find_element_by_xpath(locatorsPhase3.signInButtonXpath);
    signInButton.click();
    driver.implicitly_wait(100)
    time.sleep(3)

    pageURL = driver.current_url;
    expectedPageURL = "https://www.flickrclone.tech/home"
    time.sleep(2);
    assert pageURL==expectedPageURL,"Login Successfuly"

