from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from locators import Locators


import time


driver=webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
driver.maximize_window();
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

#go to my profile
ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
ProfileButton.click();
time.sleep(2);
ProfileNameButton=driver.find_element_by_xpath(Locators.profileNameButtonXpath);
ProfileNameButton.click();


#followers button
followersButton=driver.find_element_by_xpath(Locators.followersButtonXpath);
followersButton.click();

#go to the first follower profile
firstFollower=driver.find_element_by_xpath(Locators.firstFollowerXpath);
firstFollower.click();

followersButton=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div[2]/div[2]/p[3]/a");
followersButton.click();

profile="mariamaximus"

message = driver.find_elements_by_tag_name('h2')
for i in message:
    print(i.text)
    if i.text==profile:
        print("correct")





