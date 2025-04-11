from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

firstname=driver.find_element(By.NAME,value="fName")
firstname.send_keys("Dongari")

lastname=driver.find_element(By.NAME, value="lName")
lastname.send_keys("Sri Kashyap")

email=driver.find_element(By.NAME, value="email")
email.send_keys("kashyap@gmail.com")

signup=driver.find_element(By.CLASS_NAME, value="btn")
signup.click()