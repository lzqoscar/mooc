from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re,time

driver=webdriver.Chrome(executable_path="C:/python3.8/chromedriver")
driver.get("https://www.icourse163.org/spoc/university/SEU?_trace_c_p_k2_=714ebe082b464ec385e1d9f428ea1846#/c")
time.sleep(10)
driver.find_element_by_xpath("//div[@id='newCourseList']/div/div/div/div/div[2]").click()
time.sleep(10)
list1=[]
list2=[]
for _ in range(23):
    time.sleep(1)
    html=driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    text_div = soup.find_all('div', {"class": "u-courseCardWithTime-teacher"})
    a_href = soup.find_all('a',{"href":re.compile("//www.icourse163.org/spoc/course")})
    for a in a_href:
        url=a['href']
        list1.append(url)
    for text in text_div:
        list2.append(text.get_text())
    for i in range(-1,-21,-1):
        with open("C:/img/c.txt","a") as f:
            f.write(list2[i]+list1[i])
    if _==22:
        break
    else:
        driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()#对于auto-id使用contains(a,b)
print("over")