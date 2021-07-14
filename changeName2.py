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


#go to my settings
ProfileButton = driver.find_element_by_xpath(Locators.profileButtonXpath);
ProfileButton.click();
time.sleep(2);
settingsButton=driver.find_element_by_xpath(Locators.settingsButtonXpath);
settingsButton.click();


#change Real name
changeRealName=driver.find_element_by_xpath(Locators.changeRealNameXpath);
changeRealName.click();
firstNameInput=driver.find_element_by_xpath(Locators.firstNameInputXpath).clear();
firstNameInput=driver.find_element_by_xpath(Locators.firstNameInputXpath);
first=""
last=""
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





