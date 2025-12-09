import time

from selenium import webdriver
from ddt_try.read_ex import read_data

path=r'C:\Users\HP\PycharmProjects\Selenium_training\Training\ddt_try\demo_data.xlsx'
data=read_data(path,'reg')

# data={}

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)


driver.find_element('xpath','//a[text()="Register"]').click()
time.sleep(2)
driver.find_element('id', 'gender-female').click()
driver.find_element('id','FirstName').send_keys(data['firstname'])
driver.find_element('id','LastName').send_keys(data['lastname'])
driver.find_element('id','Email').send_keys(data['email_id'])
driver.find_element('id','Password').send_keys(data['pwd'])
driver.find_element('id','ConfirmPassword').send_keys(data['confirm_pwd'])

