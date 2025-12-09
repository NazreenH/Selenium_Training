# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)

# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(2)
#
# driver.find_element('xpath','(//div[@id="ai-chat-bubble-close"])[2]').click()
# time.sleep(3)
#
# gold_sellprice=driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[2]')
# gold_buyprice=driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[3]' )
#
# print(f"The sellprice is {gold_sellprice.text}")
# print(f"The buyprice is{gold_buyprice.text}")

# --------------------------------------------------------------------------------------------------------------
# 17/11
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# footer_elements=driver.find_elements('xpath','//div[@class="footer-menu-wrapper"]//a')
# print(footer_elements)
#
# for ele in footer_elements:
#     print(ele.text)


# -------------------------------------------------------------------
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# footer_elements=driver.find_elements('xpath','//div[@class="block block-category-navigation"]//a')
# print(footer_elements)
#
# for ele in footer_elements:
#     print(ele.text)

# ......................................................................................................................

# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)



# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# all_links=driver.find_elements('tag name','a')
#
# for link in all_links:
#     print(link.get_attribute('href'))



# ------------------------------------------------------------------------------------

# driver.get('https://testautomationpractice.blogspot.com')
# time.sleep(2)

# driver.get('https://the-internet.herokuapp.com/basic_auth')
# time.sleep(3)

# =================================================================================================
# file upload
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(3)
#
# file1=r'C:\Users\HP\Desktop\demo.html'
# file2=r'C:\Users\HP\Desktop\Study\IntraEdge.txt'
#
# driver.find_element('xpath','//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}')

# =============================================================================================================
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj=ActionChains(driver)

driver.get('https://www.myntra.com/')
time.sleep(3)

# wemen=driver.find_element('xpath','(//a[text()="Women"])[1]')
# ac_obj.move_to_element(wemen).perform()

# =========================================================================================

