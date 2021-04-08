from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


import os
os.environ["LANG"] = "en_US.UTF-8"


driver = webdriver.Chrome(executable_path='E:\Download\chromedriver_win32\chromedriver.exe')
driver.get('https://www.spectrum.com/mobile')


timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "Level_1_Category_No1")))
except TimeoutException:
    driver.quit()


category_element = driver.find_element(By.ID,'Level_1_Category_No1').text
#result -- Electronic Devices as the first category listing

list_category_elements = driver.find_element(By.XPATH,'//*[@id="J_icms-5000498-1511516689962"]/div/ul')
links = list_category_elements.find_elements(By.CLASS_NAME,"lzd-site-menu-root-item")
for i in range(len(links)):
    print("element in list ",links[i].text)
#result {Electronic Devices, Electronic Accessories, etc}


element = driver.find_elements_by_class_name('J_ChannelsLink')[1]
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()


head = driver.find_elements_by_tag_name('head')
for word in head:
    if word.text != "":
        print(word.text)


words = driver.find_elements_by_tag_name('h2')
for count, w in enumerate(words):
    if count <= 1000:
        if w.text != "":   
            print(w.text)