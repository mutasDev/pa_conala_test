#add one to the hidden web element with id 'XYZ' with selenium python script


from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

element = driver.find_element_by_id("XYZ")

element.send_keys(1)