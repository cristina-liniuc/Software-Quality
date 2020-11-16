# Lab5 - automation test for aiexpress.com

from selenium import webdriver

driver = webdriver.Firefox() 
# Open Aliexpress 
driver.get("https://aliexpress.com") 
#Find the serach field, sent "computer" and submit  
search_field = driver.find_element_by_name("SearchText")  
search_field.send_keys("computer") 
submit_button = driver.find_element_by_xpath("//input[@type ='submit']") 
submit_button.click()  
#Chack if the header is displayed
if driver.find_element_by_css_selector('#header'):
	print("Header found")
else: 
	print("Header not found") 