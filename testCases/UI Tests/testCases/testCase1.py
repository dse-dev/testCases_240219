from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.sogeti.com/")
driver.implicitly_wait(3)

btn_declineOptCookies = driver.find_element(By.XPATH, '''//html[@id='ng-app']//div[@id='CookieConsent']/div[@class='consentcontent']//div[@class='buttons']/button[3]''')
driver.implicitly_wait(3)

btn_declineOptCookies.click()
driver.implicitly_wait(3)

btn_services = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[3]')
#//*[@id="main-menu"]/ul/li[3]/div[1]/span/text()
#/html/body/div[1]/header/div[2]/nav/ul/li[3]
#//html[@id='ng-app']//nav[@id='main-menu']/ul/li[3]/div[@class='wrapper']/span[.='Services']
driver.implicitly_wait(3)

# HOVER
hover_btn_services_1 = ActionChains(driver)
hover_btn_services_1.move_to_element(btn_services).perform()
driver.implicitly_wait(3)

# Find an element by its ID
btn_automation = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[3]/div[2]/ul/li[4]/a')
# /html/body/div[1]/header/div[2]/nav/ul/li[3]/div[2]/ul/li[4]/a

# CLICK AUTOMATION
btn_automation.click()
driver.implicitly_wait(3)

# check if Automation Title is visible
span_automation = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div[2]/div/h1/span')
# /html/body/div[1]/main/div[3]/div/div[2]/div/h1/span

# Print state of visability for element "Automation"
if span_automation.is_displayed():
    print("The element 'Automation' is visible.")
else:
    print("The element 'Automation' is not visible.")
driver.implicitly_wait(3)


# Refresh
""" refreshing page because 'Services' button's state is stale after clicking button 'Automation'"""
driver.refresh()
print("refresh done")
time.sleep(1)
driver.implicitly_wait(3)

# Get 'Services' button again
"""because old xpath is stale after clicking automation"""
btn_services_2 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[3]')
print("service button found again")
driver.implicitly_wait(3)

# Get button 'About us'
"""for clicking different button than 'services' to refresh navigation bar state"""
btn_aboutUs = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/nav/ul/li[1]')
# /html/body/div[1]/header/div[2]/nav/ul/li[1]
print("'About us' button found")
driver.implicitly_wait(3)

# click button 'About us'
"""clicking to expand navigation bar on a different location"""
btn_aboutUs.click()
print("about us button clicked")
driver.implicitly_wait(3)

# click button 'About us' again
"""clicking this button again to close navigation bar"""
btn_aboutUs.click()
print("about us button clicked again")
time.sleep(3)
driver.implicitly_wait(3)

# Create ActionChain for hover action
hover_btn_services_2 = ActionChains(driver)
print("new hover actions driver")

# Hover on button 'Services' in navigation bar to expand it
hover_btn_services_2.move_to_element(btn_services_2).perform()
print("hover on services done")
time.sleep(1.0)
driver.implicitly_wait(3)

# Verify if 'Services' button in NavBar is selected
print("Check if 'Services button' is selected: ", btn_services_2.is_selected())
    # (!) Selection should be true but is false, altough it is visibly selected in browser and menu is extended

time.sleep(3)

# Verify if 'Automation' button in NavBar's menu is selected
    # (!) Selection should be true but will throw error because element already got stale
print("Check if Automation button is selected: ", btn_automation.is_selected())

# some other verification I wanted to try
    #cssValue = btn_services_2.value_of_css_property('background-color')

time.sleep(3)

# END OF PROGRAM

