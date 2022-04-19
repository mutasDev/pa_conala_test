#click a href button 'Send' with selenium


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")

elem = driver.find_element_by_xpath("//a[@href='http://www.google.com/send']")
elem.click()