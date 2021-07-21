# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
# driver.get("https://jqueryui.com/droppable/")
# driver.implicitly_wait(30)
#
# var=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
# driver.switch_to_frame(var)
# src=driver.find_element_by_id("draggable")
# dest=driver.find_element_by_id("droppable")
# a1=ActionChains(driver)
# driver.implicitly_wait(200)
# a1.drag_and_drop(src,dest).perform()


from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
driver.implicitly_wait(30)
var=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to_frame(var)
src=driver.find_element_by_id("draggable")
dest=driver.find_element_by_id("droppable")
a1=ActionChains(driver)
a1.drag_and_drop(src,dest).perform()
# Puneeth is bad boy

