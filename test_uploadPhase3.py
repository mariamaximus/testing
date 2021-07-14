from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from locators_phase3 import locatorsPhase3
from selenium.webdriver.common.action_chains import ActionChains



import time
import pytest

@pytest.fixture()
def setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    driver.maximize_window();
    driver.get("https://www.flickrclone.tech/login");
    myEmail = "mariaphoto3@gmail.com";
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

def test_uploadPhotoFromSamllButton(setup):

    cameraRoll=driver.find_element_by_xpath(locatorsPhase3.cameraRollXpath)
    cameraRoll.click()
    cameraRollBarElement=driver.find_element_by_xpath(locatorsPhase3.cameraRollBarElementXpath).is_selected()
    pageURL=driver.current_url
    expectedPageURL="https://www.flickrclone.tech/cameraroll"
    assert pageURL==expectedPageURL , "failed to direct to profile page"
    assert cameraRollBarElement == True , "failed to redirect to profile page on camera roll section"
    uploadButton=driver.find_element_by_xpath(locatorsPhase3.uploadButtonXpath)
    uploadButton.click()
    pageURL=driver.current_url
    expectedPageURL="https://www.flickrclone.tech/upload"
    assert pageURL==expectedPageURL,"failed to redirect to upload page"
    chosePhotoOrVideoButton=driver.find_element_by_xpath(locatorsPhase3.chosePhotoOrVideoButtonXpath)
    chosePhotoOrVideoButton.click()
    time.sleep(10)
    uploadFinalButton=driver.find_element_by_xpath(locatorsPhase3.uploadFinalButtonXpath)
    uploadFinalButton.click()
    pageURL=driver.current_url
    expectedPageURL="https://www.flickrclone.tech/user/60be54d6f3e8b0001fa0c3fd/photostream"
    assert pageURL==expectedPageURL,"No message to inform that the upload is done and failed to redirect to photostream"



def test_validUploadPhotoFromSmallIcon(setup):
    time.sleep(2)
    cameraRoll = driver.find_element_by_xpath(locatorsPhase3.cameraRollXpath)
    cameraRoll.click()
    cameraRollBarElement = driver.find_element_by_xpath(locatorsPhase3.cameraRollBarElementXpath).is_selected()
    pageURL = driver.current_url
    expectedPageURL = "https://www.flickrclone.tech/cameraroll"
    #assert pageURL == expectedPageURL, "failed to direct to profile page"
    #assert cameraRollBarElement == True, "failed to redirect to profile page on camera roll section"
    print("failed to redirect to profile page on camera roll section")
    uploadButton = driver.find_element_by_xpath(locatorsPhase3.uploadButtonXpath)
    uploadButton.click()
    pageURL = driver.current_url
    expectedPageURL = "https://www.flickrclone.tech/upload"
    assert pageURL == expectedPageURL, "failed to redirect to upload page"
    #chosePhotoOrVideoButton = driver.find_element_by_xpath(locatorsPhase3.chosePhotoOrVideoButtonXpath)
    #chosePhotoOrVideoButton.click()
    #my wait
    time.sleep(15)
    uploadFinalButton = driver.find_element_by_xpath(locatorsPhase3.uploadFinalButtonXpath)
    uploadFinalButton.click()
    time.sleep(3)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath(locatorsPhase3.headerYouXpath)).perform()
    photoStream=driver.find_element_by_xpath(locatorsPhase3.photoStreamXpath)
    photoStream.click()
    time.sleep(15)
    driver.refresh()
    time.sleep(2)
    photoUploaded=False
    try:
        newPhoto=driver.find_element_by_xpath(locatorsPhase3.expectedPicTest1PlaceXplath).is_displayed()
        photoUploaded=True
    except NoSuchElementException:
        photoUploaded=False


    assert photoUploaded==True,"failed to upload photo,No count to check the photos or unique name for the picture"

    cameraRoll = driver.find_element_by_xpath(locatorsPhase3.cameraroll)
    cameraRoll.click()
    time.sleep(5)
    newPhotoCameraroll=False
    try:
        newPhoto=driver.find_element_by_xpath(locatorsPhase3.camerarollPic1Xpath)
        newPhotoCameraroll=True
    except NoSuchElementException:
        newPhotoCameraroll=False

    assert newPhotoCameraroll==True,"failed to appear in cameraroll"




def test_failedUploadPhotoFromBarIcon(setup):
    time.sleep(2)
    headerYou = driver.find_element_by_xpath(locatorsPhase3.headerYouXpath);
    hoverYou = ActionChains(driver).move_to_element(headerYou)
    hoverYou.perform()
    photoStream = driver.find_element_by_xpath(locatorsPhase3.photoStreamXpath)
    photoStream.click()
    time.sleep(2)
    uploadIcon=driver.find_element_by_xpath(locatorsPhase3.uploadIconXpath)
    uploadIcon.click()
    time.sleep(2)
    pageURL = driver.current_url
    expectedPageURL = "https://www.flickrclone.tech/upload"
    assert pageURL == expectedPageURL, "failed to redirect to upload page"
    time.sleep(2)
    #chosePhotoOrVideoButton = driver.find_element_by_xpath(locatorsPhase3.chosePhotoOrVideoButtonXpath).click()
    #my wait
    time.sleep(15)
    uploadFinalButton = driver.find_element_by_xpath(locatorsPhase3.uploadFinalButtonXpath)
    uploadFinalButton.click()
    time.sleep(1)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath(locatorsPhase3.headerYouXpath)).perform()
    photoStream=driver.find_element_by_xpath(locatorsPhase3.photoStreamXpath)
    photoStream.click()
    time.sleep(15)
    driver.refresh()
    time.sleep(2)
    photoUploaded=False
    try:
        newPhoto=driver.find_element_by_xpath(locatorsPhase3.expectedPicTest2PlaceXplath)
        photoUploaded=True
    except NoSuchElementException:
        photoUploaded=False

    assert photoUploaded==True,"failed to upload photo,check in Photostream,No count to check the photos or unique name for the picture"

    cameraRoll = driver.find_element_by_xpath(locatorsPhase3.cameraroll)
    cameraRoll.click()
    time.sleep(5)

    newPhotoCameraroll=False
    try:
        newPhoto=driver.find_element_by_xpath(locatorsPhase3.camerarollPic2Xpath)
        newPhotoCameraroll=True
    except NoSuchElementException:
        newPhotoCameraroll=False

    assert newPhotoCameraroll==True,"failed to appear in cameraroll"

