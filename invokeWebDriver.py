from selenium import webdriver
#Download the chrome driver and mention the path were the driver is saved
#Download webdriver-   https://www.selenium.dev/downloads/
#Download gekodriver- https://github.com/mozilla/geckodriver/releases
driver = webdriver.Chrome(executable_path="WebDrivers/chromedriver1.exe")
#driver = webdriver.Firefox(executable_path="WebDrivers/geckodriver.exe")
driver.maximize_window()
#driver.get("https://facebook.com")
#print(driver.title)
#print(driver.current_url)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

name = 'name'
email = 'email'
password = 'exampleInputPassword1'

driver.implicitly_wait(5000)
driver.find_element_by_name(name).send_keys("Abhimanyu")
driver.implicitly_wait(5000)
driver.find_element_by_name(email).send_keys("Abhimanyu@gmail.com")
driver.implicitly_wait(5000)
driver.find_element_by_id(password).send_keys("abcd")
driver.implicitly_wait(5000)
driver.find_element_by_id("exampleCheck1").click()
driver.implicitly_wait(5000)
driver.find_element_by_id("exampleFormControlSelect1").click()
driver.implicitly_wait(5000)
driver.find_element_by_xpath("//select/option[text()='Female']").click()
driver.implicitly_wait(5000)

#driver.back()

#driver.close()    #Only current window will close

#driver.quit()    #It will close all the opened windows i.e multiple opened window close