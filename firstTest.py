from selenium import webdriver
from selenium.webdriver.common.keys import Keys

myDriver = webdriver.Chrome("E://GMtes//Santubhau//Drivers//chromedriver.exe")

myDriver.get("https://www.google.com")
myDriver.maximize_window()
myEdit = myDriver.find_element_by_name("q")
myEdit.send_keys("Queue Codes Technology")

#myButton = myDriver.find_element_by_name("btnK")
myEdit.send_keys(Keys.ENTER)

print ("GM Push Test")
