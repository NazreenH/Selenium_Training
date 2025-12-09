# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('file:///C:/Users/HP/Desktop/demo.html')
# time.sleep(2)
# driver.maximize_window()
# time.sleep(1)
# driver.find_element('class name','c1').send_keys('nazreen')
# time.sleep(1)
# driver.find_element('class name','c2').send_keys('naz@345')
# time.sleep(1)
# driver.find_element('tag name','a').click()
# time.sleep(2)
#
# ##################################################################################################
import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/register')
time.sleep(2)
driver.maximize_window()
time.sleep(1)
driver.find_element('id','gender-female').click()
time.sleep(1)
driver.find_element('class name','text-box.single-line').send_keys('abc')
time.sleep(1)
driver.find_element('id','LastName').send_keys('xyz')
time.sleep(1)
driver.find_element('id','Email').send_keys('abc@gmail.com')
time.sleep(1)
driver.find_element('id','Password').send_keys('abc@123')
time.sleep(1)
driver.find_element('id','ConfirmPassword').send_keys('abc@123')
time.sleep(1)
driver.find_element('id','register-button').click()
time.sleep(1)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# driver.find_element('class name','youtube').click()
# time.sleep(2)