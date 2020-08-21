import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = r'D:\chromedriver_win32\chromedriver.exe')
driver.get("https://myonlineservices.students.yorku.ca/")
driver.find_element_by_xpath('//*[@id="mos"]/div[3]/ul/li[2]/a').click()
#second page
time.sleep(2)
login_username = '/html/body/div[3]/div[2]/div[1]/form/div[1]/div[2]/p/input'
login_password = '/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[1]/input'
login_button = '/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input'
#enter ur login name here
driver.find_element_by_xpath(login_username).send_keys("")
time.sleep(1)
#enter ur login password here
driver.find_element_by_xpath(login_password).send_keys("")
time.sleep(1)
driver.find_element_by_xpath(login_button).click()
#selection page(third)
time.sleep(5)
s1 = Select(driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/span/select'))
s1.select_by_value('2')
button_continue = '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input'
driver.find_element_by_xpath(button_continue).click()
#add courses page
time.sleep(2)
add_courses = '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[4]/tbody/tr[1]/td[1]/div/input'
driver.find_element_by_xpath(add_courses).click()
#enter course code page
time.sleep(2)
course_code = '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[1]'
#enter ur course keys here
driver.find_element_by_xpath(course_code).send_keys("")
time.sleep(1)
addcourse_button = '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[2]'
driver.find_element_by_xpath(addcourse_button).click()
#confirmpage
yes_button = '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[6]/td[2]/input[1]'
driver.find_element_by_xpath(yes_button).click()
time.sleep(3)
driver.quit()


        
