from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import string
import random
import time
import requests

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.sogeti.com/")
driver.implicitly_wait(2)

# Find Button "Decline Optional Cookies"
btn_declineOptCookies = driver.find_element(By.XPATH, '''//html[@id='ng-app']//div[@id='CookieConsent']/div[@class='consentcontent']//div[@class='buttons']/button[3]''')
driver.implicitly_wait(2)

# Click "Decline Optional Cookies"
btn_declineOptCookies.click()
print("cookies declined")
driver.implicitly_wait(2)

# Get dropdown Worldwide
dropdown_worldwide = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[2]/div[2]/div[2]")
print("dropdown worldwide found")

# Click & extend dropdown Worldwide menu
dropdown_worldwide.click()
print("dropdown worldwide clicked and expanded")

# Get list of links
worldwide_ul = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[2]/div[2]/div[4]/ul")

# Get number of elements in dropdown by finding all elements in link list 'worldwide_ul'
worldwide_ul_elements = worldwide_ul.find_elements(By.TAG_NAME, "li")

# COULD NOT GET THE LINKS INTO A LIST SO THAT I CAN LOOP THOUGH THE LIST TO VERIFY EACH LINK
""" Because of this program will just manipulate Xpath by adding 1 in the li[..] number """
liNumber = 1
for i in worldwide_ul_elements:
    xpathOfElement = "/html/body/div[1]/header/div[2]/div/div[2]/div[2]/div[4]/ul/li[" + str(liNumber) + "]/a"
    linkToVerify = driver.find_element(By.XPATH, xpathOfElement).get_attribute("href")
    print("Verifying following link: ", linkToVerify)
    request_head = requests.head(linkToVerify)

    # VERIFYING LINK STATUS
    """If status code of the head request is greater than '400' the link has an error"""
    if request_head.status_code >= 400:
        print("(!) LINK HAS AN ERROR - Status = ", request_head.status_code)
    else:
        print("Link is working - Status = ", request_head.status_code)
    liNumber += 1


time.sleep(3)

# END OF PROGRAM

#######################################################################
# worldwide_ul = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[2]/div[2]/div[4]/ul")
# print("found worldwide UL")
#
# worldwide_ul_elements = worldwide_ul.find_elements(By.TAG_NAME, "li")
# print("found IL elements in worldwide UL")
#
# print(worldwide_ul_elements)

# for i in worldwide_ul_elements:
#     print(i.get_attribute("href"))
#     #print(lnk.get_attribute("href"))

# for j in worldwide_ul.find_elements(By.TAG_NAME, "href"):
#     print("j = ", j.
#     for k in j.find_elements(By.TAG_NAME, "a"):
#         print(k.get_attribute("href"))

# select = Select(driver.find_elements(By.ID, "country-list-id"))
# options = select.all_selected_options
# print(select)
# print(options)

#################################
### GET LINKS BY USING SELECT ###
#################################
# select = Select(driver.find_element(By.ID, "country-list-id"))
# allOptions = select.options
# optionsList = []
#
# singleElement = driver.find_element(By.TAG_NAME, "a")    # find_elements_by_class_name('select-wrapper')[0].click()
# addToListAction = ActionChains(driver)
# addToListAction.move_to_element(singleElement).perform()
#
# for singleOption in allOptions:
#     optionsList.append(singleOption.get_attribute("href"))
#
# for optionValue in optionsList:
#     print("starting loop on option %s" % optionValue)
#     select.select_by_value(optionValue)

