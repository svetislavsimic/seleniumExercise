from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
import threading

def skipAdFunction(skipAd):
    threading.Timer(10,skipAdFunction).start()
    if(skipAd.is_enabled() or skipAd.is_displayed()):
        skipAd.click()

def youtube():
    driver = webdriver.Chrome()
    driver.implicitly_wait(50)
    driver.get("https://www.youtube.com/watch?v=4Tz4Yky9MRA")
    driver.refresh()
    driver.maximize_window()
    time.sleep(5)

    #-----Skip dugme----
    skipAd = driver.find_element_by_xpath("//div[contains(@class,'ytp-ad-text ytp-ad-skip-button-text')]")
    skipAdFunction(skipAd)
    #----Neki od elemenata(Play dugme i Video ekran)----
    videoClip = driver.find_element_by_xpath("//video[@tabindex='-1']")
    play_button = driver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
    #----Slider Volume elementi----
    volume_button = driver.find_element_by_xpath("//button[@class='ytp-mute-button ytp-button']")
    slider = driver.find_element_by_xpath("//div[@class='ytp-volume-slider-handle']")
    #----Slider2 elementi----
    slider_traka = driver.find_element_by_xpath("//div[@class='ytp-load-progress']")
    slider2 = driver.find_element_by_xpath("//div[@class='ytp-scrubber-pull-indicator']")

    #----Time value----
    time_value = driver.find_element_by_xpath("//span[@class='ytp-time-current']")
    actions = ActionChains(driver)
    time.sleep(3)

    if time_value.text == "0:00" :
        actions.move_to_element(play_button).click().perform()
        time.sleep(3)
    else:
        pass

    #----Slider Volume----
    actions = ActionChains(driver)
    time.sleep(3)
    actions.move_to_element(videoClip)
    actions.move_to_element(volume_button).perform()
    time.sleep(2)
    actions.click_and_hold(slider).move_by_offset(-5,0).release().perform()
    time.sleep(5)

    #----Slider2----
    actions = ActionChains(driver)
    actions.move_to_element(videoClip)
    actions.move_to_element(slider_traka).perform()
    time.sleep(2)
    actions.click_and_hold(slider2).move_by_offset(95,0).release().perform()
    time.sleep(30)

if __name__=="__main__":
    youtube()

