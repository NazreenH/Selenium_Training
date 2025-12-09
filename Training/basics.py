# import time
#
# from selenium import webdriver
# c_driver = webdriver.Chrome()
# time.sleep(10)

# from selenium import webdriver
# f_driver = webdriver.Firefox()

# import time
# from selenium import webdriver
# e_driver = webdriver.Edge()
# time.sleep(10)

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# c_driver = webdriver.Chrome(opts)


from selenium import webdriver

opts = webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)

e_driver = webdriver.Edge(opts)