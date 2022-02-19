from selenium import webdriver
import time
#获取数据 解析数据

driver = webdriver.Chrome()

driver.get('http://taobao.com')

driver.find_element_by_id('q').send_keys('python')

driver.find_element_by_class_name("btn-search").click()
time.sleep(10)

