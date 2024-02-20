from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import string
import random
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.sogeti.com/")

driver.implicitly_wait(2)

# Find Button "Decline Optional Cookies"
btn_declineOptCookies = driver.find_element(By.XPATH, '''//html[@id='ng-app']//div[@id='CookieConsent']/div[@class='consentcontent']//div[@class='buttons']/button[3]''')
driver.implicitly_wait(2)

# Click "Decline Optional Cookies"
btn_declineOptCookies.click()
driver.implicitly_wait(2)

# Find Button "Services"
btn_services = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[3]')
driver.implicitly_wait(2)

# Hover over "Services"
hover_btn_services_1 = ActionChains(driver)
hover_btn_services_1.move_to_element(btn_services).perform()
driver.implicitly_wait(2)

# Find Button 'Automation'
btn_automation = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[3]/div[2]/ul/li[4]/a')
driver.implicitly_wait(2)

# Click Button 'Automation'
btn_automation.click()
driver.implicitly_wait(2)
print("Get Element 'contact' us")

# Get Element "contact us"
label_contactUs = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/h2')
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/h2
print("Get Element 'contact' us")

# Scroll to 'contact us'
label_contactUs.location_once_scrolled_into_view
# driver.execute_script("arguments[0].scrollIntoView()")
print("Scroll to 'contact us'")

# Get Element "First Name"
input_name_first = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[1]/div/div/input')
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[1]/div/div/input

# Fill 'First Name'
name_first = ''.join(random.choices(string.ascii_uppercase, k=5))
print("Random First Name = ", name_first)
input_name_first.send_keys(name_first)
print("Filled 'First Name'")
time.sleep(0.1)

# Get Element 'Last Name'
input_name_last = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[2]/div/div/input')
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[2]/div/div/input

# Fill 'Last Name'
name_last = ''.join(random.choices(string.ascii_uppercase, k=7))
print("Random Last Name = ", name_last)
input_name_last.send_keys(name_last)
print("Filled 'Last Name'")
time.sleep(0.1)

# Get Element 'Email'
input_email = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[3]/div/div/input')
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[3]/div/div/input

# Fill 'Email'
email = ''.join(random.choices(string.ascii_lowercase, k=8))
email = email + "@"
email = email + ''.join(random.choices(string.ascii_lowercase, k=4))
email = email + ".com"
print("Random Email = ", email)
input_email.send_keys(email)
print("Filled 'Email'")
time.sleep(0.1)

# Get Element "Phone"
input_phone = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[4]/div/div/input')
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[4]/div/div/input

# Fill 'Phone'
# Telephone numbers 00498999998-000 to 00498999998-999 are not connected to service by network provider
phone = "00498999998"
phone = phone + ''.join(random.choices(string.digits, k=3))
print("Random Email = ", phone)
input_phone.send_keys(phone)
print("Filled 'Phone'")
time.sleep(0.1)

# Get Element 'Company'
input_company = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[5]/div/div/input')
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[5]/div/div/input

# Fill 'Company'
company = ''.join(random.choices(string.ascii_uppercase, k=7))
print("Random Company Name = ", company)
input_company.send_keys(company)
print("Filled 'Company'")
time.sleep(0.1)

# Get Select Element 'Country'
select_country = Select(driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[6]/div/div/div/select'))

# Select 'Country'
# not a random selection
select_country.select_by_value('Argentina')
print("Selected 'Country': Argentina")
time.sleep(0.1)


# Get Element "Message"
input_message = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[7]/div/div/textarea')
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[7]/div/div/textarea

# Fill 'Message'
submit_msg = ''.join(random.choices(string.ascii_letters, k=32))
print("Random Email = ", submit_msg)
input_message.send_keys(submit_msg)
print("Filled Submit 'Message'")
time.sleep(0.1)

input_message.location_once_scrolled_into_view
time.sleep(1)

# Get Check Box "I Agree"
input_agree = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[9]/div/div/fieldset/span/label')
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[9]/div/div/fieldset/span/input
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[9]/div/div/fieldset/span/label
print("Found checkbox 'I agree'")

# Click checkbox 'I agree'
tick_checkbox = ActionChains(driver)
print("new actions chains driver")
tick_checkbox.move_to_element(input_agree).click().perform()
print("actions chains clicked checkbox")

# Get reCAPTCHA label
time.sleep(1)
label_captcha = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[10]/div/div/div/div/div/iframe')
time.sleep(1)

# Hover over "Services"
hover_captcha = ActionChains(driver)
hover_captcha.move_to_element(label_captcha).perform()
time.sleep(1)

label_captcha.click()
time.sleep(2)

# Get submit button
btn_submit = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[11]/div/button")
# /html/body/div[1]/main/div[3]/div/div[3]/div/div[3]/div[2]/div[6]/div[3]/form/div[2]/section/div[11]/div/button
print("got submit button")

# click submit button
btn_submit.click()

time.sleep(3)

# END OF PROGRAM