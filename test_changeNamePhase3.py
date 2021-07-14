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
    myEmail = "mariamaximus1012@gmail.com";
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
    hoverYou = ActionChains(driver).move_to_element(headerYou)
    hoverYou.perform()
    yield
    driver.close()
    driver.quit()

def test_changeNameNumbersAndEmpty(setup):
    #go to my settings
    profileButton = driver.find_element_by_xpath(locatorsPhase3.profileButtonXpath).is_enabled()
    assert profileButton == False, "failed to go to settings"
    # profileButton.click();
    time.sleep(2);
    settingsButton = driver.find_element_by_xpath(Locators.settingsButtonXpath);
    settingsButton.click();
    settingsButton=driver.find_element_by_xpath(Locators.settingsButtonXpath);
    settingsButton.click();


    #change Real name
    changeRealName=driver.find_element_by_xpath(Locators.changeRealNameXpath);
    changeRealName.click();
    firstNameInput=driver.find_element_by_xpath(Locators.firstNameInputXpath).clear();
    firstNameInput=driver.find_element_by_xpath(Locators.firstNameInputXpath);
    first=""
    last="10"
    lastNameInput=driver.find_element_by_xpath(Locators.lastNameInputXpath).clear()
    lastNameInput=driver.find_element_by_xpath(Locators.lastNameInputXpath);

    firstNameInput.send_keys(first);
    time.sleep(1)
    lastNameInput.send_keys(last)
    time.sleep(2);

    scroll=driver.execute_script("window.scrollTo(0, 1000)");
    saveRealName=driver.find_element_by_xpath(Locators.saveRealNameXpath);
    saveRealName.click();
    time.sleep(2);
    checkURL="https://www.flickr.com/account/?tab=default&doneprofile=1"
    currURL=driver.current_url;
    assert checkURL==currURL,"failed to change Real Name";

    #go to my profile
    ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
    ProfileButton.click();
    time.sleep(2);
    ProfileNameButton=driver.find_element_by_xpath(Locators.profileNameButtonXpath);
    handleName=ProfileNameButton.text;
    #print(handleName);
    ProfileNameButton.click();

    profile=first+last;

    time.sleep(2);
    message = driver.find_elements_by_tag_name('h1')
    for i in message:
        #print(i.text)
        if i.text==profile:
            print(i.text);
            print("Real Name is Changed")
        elif i.text==handleName:
            print(i.text);
            print("Real Name is Changed")



def test_changeNameAllEmpty(setup):
    # go to my settings
    # go to my settings
    profileButton = driver.find_element_by_xpath(locatorsPhase3.profileButtonXpath).is_enabled()
    assert profileButton == False, "failed to go to settings"
    # profileButton.click();
    time.sleep(2);
    settingsButton = driver.find_element_by_xpath(Locators.settingsButtonXpath);
    settingsButton.click();

    # change Real name
    changeRealName = driver.find_element_by_xpath(Locators.changeRealNameXpath);
    changeRealName.click();
    firstNameInput = driver.find_element_by_xpath(Locators.firstNameInputXpath).clear();
    firstNameInput = driver.find_element_by_xpath(Locators.firstNameInputXpath);
    first = ""
    last = ""
    lastNameInput = driver.find_element_by_xpath(Locators.lastNameInputXpath).clear()
    lastNameInput = driver.find_element_by_xpath(Locators.lastNameInputXpath);

    firstNameInput.send_keys(first);
    time.sleep(1)
    lastNameInput.send_keys(last)
    time.sleep(2);

    scroll = driver.execute_script("window.scrollTo(0, 1000)");
    saveRealName = driver.find_element_by_xpath(Locators.saveRealNameXpath);
    saveRealName.click();
    time.sleep(2);
    checkURL = "https://www.flickr.com/account/?tab=default&doneprofile=1"
    currURL = driver.current_url;
    assert checkURL == currURL, "failed to change Real Name";

    # go to my profile
    ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
    ProfileButton.click();
    time.sleep(2);
    ProfileNameButton = driver.find_element_by_xpath(Locators.profileNameButtonXpath);
    handleName = ProfileNameButton.text;
    # print(handleName);
    ProfileNameButton.click();

    profile = first + last;

    time.sleep(2);
    message = driver.find_elements_by_tag_name('h1')
    for i in message:
        # print(i.text)
        if i.text == profile:
            print(i.text);
            print("Real Name is Changed")
        elif i.text == handleName:
            print(i.text);
            print("Real Name is Changed")



