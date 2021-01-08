# How to install python --- 
# Install selenium --- # pip install selenium
# Download Chorme Driver # https://selenium-python.readthedocs.io/installation.html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
WebDriverWait(driver, 20)
driver.implicitly_wait(20)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()


contacts = (
    'Test', 'Test Group',
)
message = 'Hi This is a Automated Message!!!'
for name in contacts:
    search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    sleep(2)
    search.send_keys(name)
    sleep(2)
    driver.find_element_by_xpath(f"//span[@title='{name}']").click()
    sleep(2)
    msg_type= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    sleep(2)
    msg_type.send_keys(message)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

# sleep(20)
# driver.quit()

#//*[@id="side"]/div[1]/div/label/div/div[2]
# //*[@id="pane-side"]/div[1]/div/div/div[3]/div/div/div[2]/div[1]/div[1]/span/span
# //*[@id="main"]/footer/div[1]/div[2]/div/div[2]
# //*[@id="main"]/footer/div[1]/div[3]/button