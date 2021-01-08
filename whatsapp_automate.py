from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


contact_list = ('Robo', 'Test',)
message = 'Hi This is a Automated WhatsApp Message'


chrome_options = Options()
chrome_options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
WebDriverWait(driver, 20)
driver.implicitly_wait(20)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()


# //*[@id="side"]/div[1]/div/label/div/div[2] # Step 1

# //span[@title='Test 2'] # Step 2

# //*[@id="main"]/footer/div[1]/div[2]/div/div[2] # Step 3

# //span[@data-icon='send']/parent::* # Step 4

for names in contact_list:
    sleep(2)
    search_field = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_field.click()
    sleep(2)
    search_field.send_keys(names)
    sleep(2)

    driver.find_element_by_xpath(f'//span[@title="{names}"]').click()
    sleep(2)
    msg_field = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_field.click()
    sleep(2)
    msg_field.send_keys(message)
    sleep(2)
    driver.find_element_by_xpath("//span[@data-icon='send']/parent::*").click()
    sleep(2)

# driver.quit()



