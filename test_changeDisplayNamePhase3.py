from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from locators import Locators
from locators_phase3 import locatorsPhase3


import time
import pytest

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
    time.sleep(2);

    #go to my settings
    profileButton = driver.find_element_by_xpath(locatorsPhase3.profileButtonXpath)
    profileButton.click()
    time.sleep(2);

    #assert pageURL==expectedPageURL , "Login failed"

    # headerYou=driver.find_element_by_xpath(locatorsPhase3.headerYouXpath);
    # hoverYou = ActionChains(driver).move_to_element(headerYou)
    #hoverYou.perform()
    yield
    driver.close()
    driver.quit()


def test_displayNameAsNumbers(setup):


    URL="https://www.flickrclone.tech/AccountSettings"
    currURL=driver.current_url
    assert URL==currURL,"failed to go to settings"



    ###### Change Display Name #######
    changeDisplayName=driver.find_element_by_xpath(locatorsPhase3.changeDisplayNameXpath);
    changeDisplayName.click();
    time.sleep(1);
    URL="https://www.flickrclone.tech/dispChange";
    currURL=driver.current_url;
    assert URL==currURL , "failed to redirect to change display name"
    displayName=driver.find_element_by_xpath(locatorsPhase3.changeBarXpath);
    newDisplayName="@";
    displayName.send_keys(newDisplayName);

    saveDisplayName=driver.find_element_by_xpath(locatorsPhase3.saveDisplayNameXpath);
    saveDisplayName.click();
    time.sleep(2);

    youNav=driver.find_element_by_xpath(locatorsPhase3.headerYouXpath)
    youNav.click()
    time.sleep(3);
    profileDisplayName=driver.find_element_by_xpath(locatorsPhase3.profileDisplayNameXpath).text

    assert newDisplayName==profileDisplayName,"failed to change display name"




def test_emptyDisplayName(setup):
    # # go to my settings
    # profileButton = driver.find_element_by_xpath(locatorsPhase3.profileButtonXpath).is_enabled()
    # assert profileButton == False, "failed to click on profile button"
    # profileButton.click()
    # time.sleep(2);

    URL = "https://www.flickrclone.tech/AccountSettings"
    currURL = driver.current_url
    assert URL == currURL, "failed to go to settings"

    ###### Change Display Name #######
    changeDisplayName = driver.find_element_by_xpath(locatorsPhase3.changeDisplayNameXpath);
    changeDisplayName.click();
    time.sleep(1);
    URL = "https://www.flickrclone.tech/dispChange";
    currURL = driver.current_url;
    assert URL == currURL, "failed to redirect to change display name"
    displayName = driver.find_element_by_xpath(locatorsPhase3.changeBarXpath);
    newDisplayName = "";
    displayName.send_keys(newDisplayName);
    oldDisplayName="@"
    saveDisplayName = driver.find_element_by_xpath(locatorsPhase3.saveDisplayNameXpath);
    saveDisplayName.click();
    time.sleep(2);

    youNav = driver.find_element_by_xpath(locatorsPhase3.headerYouXpath)
    youNav.click()
    time.sleep(3);
    profileDisplayName = driver.find_element_by_xpath(locatorsPhase3.profileDisplayNameXpath).text

    assert oldDisplayName == profileDisplayName, "Changed to an empty display name"


def test_alreadyTakenDisplayName(setup):
    # # go to my settings
    # profileButton = driver.find_element_by_xpath(locatorsPhase3.profileButtonXpath).is_enabled()
    # assert profileButton == False, "failed to click on profile button"
    # profileButton.click()
    # time.sleep(2);

    URL = "https://www.flickrclone.tech/AccountSettings"
    currURL = driver.current_url
    assert URL == currURL, "failed to go to settings"

    ###### Change Display Name #######
    changeDisplayName = driver.find_element_by_xpath(locatorsPhase3.changeDisplayNameXpath);
    changeDisplayName.click();
    time.sleep(1);
    URL = "https://www.flickrclone.tech/dispChange";
    currURL = driver.current_url;
    assert URL == currURL, "failed to redirect to change display name"
    displayName = driver.find_element_by_xpath(locatorsPhase3.changeBarXpath);
    takenDisplayName = "1"
    displayName.send_keys(takenDisplayName);

    saveDisplayName = driver.find_element_by_xpath(locatorsPhase3.saveDisplayNameXpath);
    saveDisplayName.click();
    time.sleep(2);
    errorMessage=False
    try:
        mess = driver.find_element_by_xpath(Locators.errorMessageDisplayXpath).text;
        errorMessage=True

    except NoSuchElementException:
        errorMessage=False
    assert errorMessage==True ,"No message displayed to inform that this a taken display name although it wasn't updated in the database"
    youNav = driver.find_element_by_xpath(locatorsPhase3.headerYouXpath)
    youNav.click()
    time.sleep(3);
    profileDisplayName = driver.find_element_by_xpath(locatorsPhase3.profileDisplayNameXpath).text

    assert takenDisplayName != profileDisplayName, "Changed to a taken display name"




