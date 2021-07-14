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
    #print(driver.title);
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
    pageTitle = driver.title;
    yield
    driver.close()
    driver.quit()


def test_displayNameAsNumbers(setup):
    # myEmail = "maria.ossama10@yahoo.com";
    # myPassword = "000011112222m";
    #
    # emailAddressField = driver.find_element_by_id("login-email");
    # nextButton = driver.find_element_by_xpath(Locators.nextButtonXpath);
    # emailAddressField.send_keys(myEmail);
    # nextButton.click();
    # driver.implicitly_wait(60)
    # passwordField = driver.find_element_by_id("login-password");
    # passwordField.send_keys(myPassword);
    # signInButton = driver.find_element_by_xpath(Locators.signInButtonXpath);
    # signInButton.click();
    # driver.implicitly_wait(60)
    # pageTitle=driver.title;


    #go to my settings
    ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
    ProfileButton.click();
    time.sleep(2);
    settingsButton=driver.find_element_by_xpath(Locators.settingsButtonXpath);
    settingsButton.click();


    ###### Change Display Name #######
    changeDisplayName=driver.find_element_by_xpath(Locators.changeDisplayNameXpath);
    changeDisplayName.click();
    time.sleep(1);
    dispURL="https://www.flickr.com/account/prefs/screenname/?from=personal";
    checkURL=driver.current_url;
    assert checkURL==dispURL , "failed to direct to change display name"
    displayName=driver.find_element_by_xpath(Locators.displayNameXpath).clear();
    displayName=driver.find_element_by_xpath(Locators.displayNameXpath);
    newDisplayName="10121998";
    displayName.send_keys(newDisplayName);

    saveDisplayName=driver.find_element_by_xpath(Locators.saveDisplayNameXpath);
    saveDisplayName.click();
    time.sleep(2);
    try:
        mess=driver.find_element_by_xpath(Locators.errorMessageDisplayXpath).text;
        print(mess);

    except NoSuchElementException:
        print("Acceptable Display name");

    ###check###
    checkURL2="https://www.flickr.com/account?donename=1";
    currURL=driver.current_url;
    assert checkURL2==currURL, "Failed to change Display Name";

    time.sleep(3);
    #go to my profile
    ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
    ProfileButton.click();
    time.sleep(2);
    ProfileNameButton=driver.find_element_by_xpath(Locators.profileNameButtonXpath);
    prof=ProfileNameButton.text;
    print(prof);
    ProfileNameButton.click();

    # time.sleep(2);
    # message = driver.find_element_by_xpath(Locators.handleNameXpath);
    # for i in message:
    #     print(i.text)
    #     if i.text==newDisplayName:
    #         print("Display Name is changed");



def test_emptyDisplayName(setup):


    # go to my settings
    ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
    ProfileButton.click();
    time.sleep(2);
    settingsButton = driver.find_element_by_xpath(Locators.settingsButtonXpath);
    settingsButton.click();

    ###### Change Display Name #######
    changeDisplayName = driver.find_element_by_xpath(Locators.changeDisplayNameXpath);
    changeDisplayName.click();
    time.sleep(1);
    dispURL = "https://www.flickr.com/account/prefs/screenname/?from=personal";
    checkURL = driver.current_url;
    assert checkURL == dispURL, "failed to direct to change display name"
    displayName = driver.find_element_by_xpath(Locators.displayNameXpath).clear();
    displayName = driver.find_element_by_xpath(Locators.displayNameXpath);
    newDisplayName = "";
    displayName.send_keys(newDisplayName);

    saveDisplayName = driver.find_element_by_xpath(Locators.saveDisplayNameXpath);
    saveDisplayName.click();
    time.sleep(2);
    try:
        mess = driver.find_element_by_xpath(Locators.errorMessageDisplayXpath).text;
        print(mess);

    except NoSuchElementException:
        print("Acceptable Display name");

    ###check###
    checkURL2 = "https://www.flickr.com/account/prefs/screenname/";
    currURL = driver.current_url;
    assert checkURL2 == currURL, "Failed to change Display Name";

    # go to my profile
    time.sleep(2);
    profileButton = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/form/p[3]/a")
    profileButton.click()

    time.sleep(2);
    message = driver.find_element_by_xpath(Locators.handleNameXpath).text;
    print(message)
    assert message != newDisplayName, "Changed to empty,wrong"


def test_alreadyTakenDisplayName(setup):
    # go to my settings
    ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
    ProfileButton.click();
    time.sleep(2);
    settingsButton = driver.find_element_by_xpath(Locators.settingsButtonXpath);
    settingsButton.click();

    ###### Change Display Name #######
    changeDisplayName = driver.find_element_by_xpath(Locators.changeDisplayNameXpath);
    changeDisplayName.click();
    time.sleep(1);
    dispURL = "https://www.flickr.com/account/prefs/screenname/?from=personal";
    checkURL = driver.current_url;
    assert checkURL == dispURL, "failed to direct to change display name"
    time.sleep(2)
    displayName = driver.find_element_by_xpath(Locators.displayNameXpath).clear();
    displayName = driver.find_element_by_xpath(Locators.displayNameXpath);
    newDisplayName = "Myriam10";
    displayName.send_keys(newDisplayName);
    time.sleep(2)

    saveDisplayName = driver.find_element_by_xpath(Locators.saveDisplayNameXpath);
    saveDisplayName.click();
    time.sleep(2);
    try:
        mess = driver.find_element_by_xpath(Locators.errorMessageDisplayXpath).text;
        print(mess);

    except NoSuchElementException:
        print("Acceptable Display name");

    ###check###
    checkURL2 = "https://www.flickr.com/account/prefs/screenname/";
    currURL = driver.current_url;
    assert checkURL2 == currURL, "Changed to a taken username";

    # go to my profile
    profilebutton = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/form/p[3]/a")
    profilebutton.click()


    time.sleep(2);

    message = driver.find_element_by_xpath(Locators.handleNameXpath).text;
    print(message)
    assert message != newDisplayName, "Changed to already taken username"




