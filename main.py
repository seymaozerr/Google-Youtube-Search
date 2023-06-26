from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)

time.sleep(2) 
driver.maximize_window()

def perform_google_search(driver):
    """
    Google'da bir arama yapar.
    
    Argümanlar:
    - driver: Selenium WebDriver nesnesi
    
    """
    search = driver.find_element(By.XPATH, '//*[@name="q"]')
    time.sleep(2)
    search.send_keys("youtube")
    time.sleep(2)
    search.send_keys(Keys.ENTER)
    time.sleep(2)


def perform_youtube_search(driver, query):
    """
    YouTube'da bir arama yapar.
    
    Argümanlar:
    - driver: Selenium WebDriver nesnesi
    - query: Arama sorgusu
    
    """
    youtube_link = driver.find_element(By.XPATH, '//h3[text()="YouTube"]//ancestor::a')
    youtube_link.click()
    time.sleep(2)
    youtube_search = driver.find_element(By.XPATH, '//*[@name="search_query"]')
    time.sleep(2)
    youtube_search.clear()
    youtube_search.send_keys(query)
    time.sleep(2)
    youtube_search.send_keys(Keys.ENTER)
    time.sleep(4)

    screenshot  = "VNL.png"
    driver.save_screenshot(screenshot)

perform_google_search(driver)
perform_youtube_search(driver, "VNL")

driver.close() 