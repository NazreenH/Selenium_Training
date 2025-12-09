from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

# xpath :
#     xpath is used to find the location of a webelement in a html tree structure or in DOM(Document object Model)

# xpath classified into two types:
# 1.Absolute xpath
# 2.Relative xpath

# 1.Absolute xpath
#     -->It will traverse from parent to its own child
#     -->It is Denoted as (/)
# Drawbacks of Absolute xpath
#     -->Absolute xpath is very lengthy comparing to relative xpath
#     --> Always it will traverse from parent to its own child
# 2.Relative xpath
#     -->It will traverse from parent to any of the child
#     -->It is Denoted as (//)

# Sample for Absolute xpath
"""
driver = http://webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[1]/input[1]").send_keys("Username1")

"""
"""
driver = webdriver.Chrome(opts)
driver.get("file:///C:/Users/Admin/Desktop/A2_Selenium/xpath.html")
time.sleep(3)
driver.find_element("xpath","html/body/div[2]/input[2]").send_keys("Username4")


driver = webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)
driver.find_element("xpath","html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
"""
# Xpath By Attribute:(imp)
#     Finding the location of a web element by using attributes is called xpath by attribute
#     Including id,name,class etc... you can use as a attributes in xpath by attribute


# Sample html code:

# <a href="https://www.amazon.in/" id="a1" name="n1" class="c1">Amazon</a>

# Syntax:

# //tagname[@attribute_name='attribute value']

# //a[@href='https://www.amazon.in/']


# driver = webdriver.Chrome(opts)
# driver.get("https://www.amazon.com/")
# time.sleep(3)
# driver.find_element("xpath",'''//a[text()="Today's Deals"]''').click()
# time.sleep(3)


# driver = webdriver.Chrome(opts)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(3)
# driver.find_element("xpath",'(//input[@type="text"])[1]').send_keys('abc')
# time.sleep(2)
# driver.find_element("xpath",'(//input[@type="text"])[2]').send_keys('xyz')
# time.sleep(2)
# driver.find_element("xpath",'(//input[@type="text"])[5]').send_keys('9876543217')
# time.sleep(1)
#
# driver.find_element("xpath",'//span[contains(text(),"GIVA Gift Card")]').click()

#.........................................................................................

driver = webdriver.Chrome(opts)
driver.get("https://www.flipkart.com/")
time.sleep(3)
driver.find_element("xpath",'//span[text()="TVs & Appliances"]').click()
time.sleep(2)
driver.find_element("xpath",'//span[text()="Become a Seller"]').click()
time.sleep(2)
driver.find_element("xpath",'//button[text()="Start Selling"]').click()
time.sleep(2)
driver.find_element("xpath",'//input[@name="mobileNumber"]').send_keys('9876543217')
time.sleep(2)
driver.find_element("xpath",'//input[@name="email"]').send_keys('abc@gmail.com')
time.sleep(2)
driver.find_element("xpath",'//span[text()="Register & Continue"]').click()
time.sleep(2)

