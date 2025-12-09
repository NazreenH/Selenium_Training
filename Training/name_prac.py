# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(1)
#
# driver.find_element('name','firstname').send_keys('nazreen')
# time.sleep(1)
# driver.find_element('name','lastname').send_keys('Hirekudi')
# time.sleep(1)
# driver.find_element('name','reg_email__').send_keys('nazreen@gmail.com')
# time.sleep(1)
# driver.find_element('name','reg_passwd__').send_keys('nazreen@8765')
# time.sleep(1)

###################################################################################################
import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.amazon.com/')
time.sleep(1)

# driver.find_element('name','firstname').send_keys('nazreen')
# time.sleep(1)