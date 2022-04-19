#click a href button with text 'Send InMail' with selenium


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

button = driver.find_element_by_xpath("//a[text()='Send InMail']")
button.click()