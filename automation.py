from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time


SID = input("put your student ID ? ")
password = input("put your password ? ")
SSN = input("put your SSN ? ")
num_sbject = input("How many subjects do you have this semester? ")

driver = webdriver.Chrome(ChromeDriverManager().install())

reaslt = driver.get("https://app2.bau.edu.jo:7799/eval/Login.jsp")


print(driver.title)
searchnum = driver.find_element_by_name("tbstdno")
searchnum.clear()
searchnum.send_keys(SID)


searchpass = driver.find_element_by_name("tbstdpass")
searchpass.clear()
searchpass.send_keys(password)


searchssn = driver.find_element_by_name("tbstdnatno")
searchssn.clear()
searchssn.send_keys(SSN)
driver.find_element_by_class_name("btn1").click()

time.sleep(3)
for i in range(int(num_sbject)):
    for i in range(19):

        driver.find_element_by_name("evalans").click()
        time.sleep(0.5)

        driver.find_element_by_id("btnNext").click()
    soup = BeautifulSoup(reaslt.content, "html.parser")
    print(soup)
    time.sleep(12)
