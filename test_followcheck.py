from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from locators import Locators


import time


def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    driver.maximize_window();



def test_followCheck():
    driver.get("https://identity.flickr.com/");
    print(driver.title);



    myEmail = "mariamaximus1012@gmail.com";
    myPassword = "1234567891011m";
    # myEmail = "passantahmedmaher@gmail.com";
    # myPassword = "1234567891011!!";
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

    searchInput=driver.find_element_by_xpath(Locators.searchInputXpath);
    profile="myriammaximus"
    searchInput.send_keys(profile);
    time.sleep(2)
    searchPeople=driver.find_element_by_xpath(Locators.searchPeopleXpath);
    driver.execute_script("arguments[0].click();", searchPeople)
    followButton = driver.find_element_by_xpath(Locators.followButtonXpath)
    driver.execute_script("arguments[0].click();", followButton)
    time.sleep(3)
    #press follow button
    followButton = driver.find_element_by_xpath(Locators.followButtonXpath)
    print(followButton.text)
    # assert followButton.text == 'Following';
    time.sleep(2);
    #go to my profile
    ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
    ProfileButton.click();
    time.sleep(3);
    ProfileNameButton=driver.find_element_by_xpath(Locators.profileNameButtonXpath);
    ProfileNameButton.click();


    followersButton=driver.find_element_by_xpath(Locators.followingButtonXpath);
    followersButton.click();


    searchFollowingInput=driver.find_element_by_xpath(Locators.searchFollowingInputXpath);
    searchFollowingInput.send_keys(profile)
    try:
        searchProfile = driver.find_element_by_xpath(Locators.searchProfileXpath);
        print("found")
        profileName=searchProfile.text;
        time.sleep(3);
        # print(profileName)
        # print(profile)
        assert profile == profileName, "Failed to follow this user"


    except NoSuchElementException:
        print("not found")


def test_teardown():
    driver.close()
    driver.quit()
    print("end of test")



