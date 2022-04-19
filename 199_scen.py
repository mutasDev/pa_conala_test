#click a href button having text `Send InMail` with selenium


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

button = driver.find_element_by_link_text("Send InMail")
button.click()