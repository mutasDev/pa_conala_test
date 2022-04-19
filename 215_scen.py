#get the html from the current web page of a Selenium driver


driver.get("http://www.google.com")

html = driver.page_source

print(html)