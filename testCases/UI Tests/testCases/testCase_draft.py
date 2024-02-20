from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#width = 1280
#height = 720
#driver.set_window_size(width, height)
driver.maximize_window()

driver.get("https://www.sogeti.com/")
    #("https://www.selenium.dev/selenium/web/web-form.html")
    #("https://www.sogeti.com/")

driver.implicitly_wait(3.0)

btn_declineOptCookies = driver.find_element(By.XPATH, '''//html[@id='ng-app']//div[@id='CookieConsent']/div[@class='consentcontent']//div[@class='buttons']/button[3]''')

#btn_declineOptCookies = driver.find_element(By.PARTIAL_LINK_TEXT, 'Decline optional cookies')
#"button.declineCookie"
#.buttons > button:nth-of-type(3)
#//html[@id='ng-app']//div[@id='CookieConsent']/div[@class='consentcontent']//div[@class='buttons']/button[3]

driver.implicitly_wait(0.5)

btn_declineOptCookies.click()

driver.implicitly_wait(2.5)
btn_services = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[3]')
#//*[@id="main-menu"]/ul/li[3]/div[1]/span/text()
#/html/body/div[1]/header/div[2]/nav/ul/li[3]
#//html[@id='ng-app']//nav[@id='main-menu']/ul/li[3]/div[@class='wrapper']/span[.='Services']

driver.implicitly_wait(0.5)

# HOVER
hover_btn_services_1 = ActionChains(driver)
hover_btn_services_1.move_to_element(btn_services).perform()
#time.sleep(3)

driver.implicitly_wait(3.0)

# Find an element by its ID
btn_automation = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[3]/div[2]/ul/li[4]/a')
# /html/body/div[1]/header/div[2]/nav/ul/li[3]/div[2]/ul/li[4]/a

# CLICK AUTOMATION
btn_automation.click()
#time.sleep(3)

driver.implicitly_wait(3.0)
# check if Automation Title is visible
span_automation = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div/h1/span')
# /html/body/div[1]/main/div[3]/div/div[2]/div/h1/span


if span_automation.is_displayed():
    print("The element 'Automation' is visible.")
else:
    print("The element 'Automation' is not visible.")

# driver.implicitly_wait(3.0)
# time.sleep(5.0)
#
# logo_sogeti = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div[1]/div/a/img')
# # /html/body/div[1]/header/div[2]/div/div[1]/div/a/img
# print("Sogeti Logo found")


time.sleep(1.0)
driver.implicitly_wait(3.0)

driver.refresh()
print("refresh done")

time.sleep(1.0)
driver.implicitly_wait(3.0)

# HOVER SERVICES

# my_element_id = 'something123'
# ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
# your_element = WebDriverWait(your_driver, some_timeout,ignored_exceptions=ignored_exceptions)\
#                         .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))

btn_services_2 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[3]')
print("service button found again")

time.sleep(1.0)
driver.implicitly_wait(1.0)

# btn_services_2 = driver.find_element(By.CSS_SELECTOR, 'li.selected.has-children.expanded.level2.focus-style')
# #main-menu > ul > li.selected.has-children.expanded.level2.focus-style.hover
# nav#main-menu > .level0 > .expanded.has-children.level2 > .wrapper > span
# /html/body/div[1]/header/div[2]/nav/ul/li[3]
# /html/body/div[1]/header/div[2]/nav/ul/li[3]/div[1]
# /html/body/div[1]/header/div[2]/nav/ul/li[3]/div[1]/span/text()
# #main-menu > ul > li.selected.has-children.expanded.level2.focus-style
# class="selected has-children expanded level2 focus-style"

btn_aboutUs = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[1]')
# /html/body/div[1]/header/div[2]/nav/ul/li[1]
print("about us button found")

time.sleep(1.0)
driver.implicitly_wait(1.0)

btn_aboutUs.click()
print("about us button clicked")

btn_aboutUs.click()
print("about us button clicked again")

time.sleep(1.0)
driver.implicitly_wait(1.0)

# btn_services_2.click()
# print("services clicked again")

time.sleep(1.0)
driver.implicitly_wait(1.0)

hover_btn_services_2 = ActionChains(driver)
print("new hover actions driver")

hover_btn_services_2.move_to_element(btn_services_2).perform()
print("hover on services done")

time.sleep(1.0)
driver.implicitly_wait(1.0)

#cssValue = btn_services_2.value_of_css_property('background-color')

##print(btn_automation.is_enabled())
print("Check if 'Services button' is selected: ", btn_services_2.is_selected())
#print(btn_services_2.is_selected())
print("Check if Automation button is selected: ", btn_automation.is_selected())
#print(btn_automation.is_selected())


time.sleep(3)

# # Check if the element is visible
# if element.is_displayed():
#     print("The element is visible.")
# else:
#     print("The element is not visible.")

title = driver.title

# driver.implicitly_wait(500.0)
#
# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
# text_box.send_keys("Selenium")
# submit_button.click()
#
# message = driver.find_element(by=By.ID, value="message")
# text = message.text

driver.quit()

