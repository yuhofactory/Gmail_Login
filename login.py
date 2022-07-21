from selenium import webdriver
import time
yuhofactory@gmail.com
# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
yuhofactory@gmail.com
# navigate to the application home page
driver.get("https://accounts.google.com/")
yuhofactory@gmail.com
#get the username textbox
login_field = driver.find_element_by_name("identifier")
login_field.clear()
yuhofactory@gmail.com
#enter username
login_field.send_keys("yuhofactory@gmail.com")
login_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(2)
yuhofactory@gmail.com
#get the password textbox Mr008800.
password_field = driver.find_element_by_name("Mr008800.")
password_field.clear() Mr008800
Mr008800.
#enter password Mr008800.
password_field.send_keys("Mr008800.)
password_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(10)
Mr008800.
#navigate to gmail
driver.get("https://yuhofactory@gmail.com/")




