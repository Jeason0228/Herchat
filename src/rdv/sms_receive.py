import pandas as pd
import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

def receive_msg(number):
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get(f"https://receive-smss.com/sms/{number}/")
    soup = BeautifulSoup(driver.page_source)
    table = soup.find('table')
    rows = table.find_all('tr')

    data = []

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            data.append({
                "sender": cols[1],
                "msg": cols[3],
                "time": cols[4]
            }) # Get rid of empty values
    # print(data[:3])

    for d in data[:3]:
        if d["sender"] == "HERMES RDV":
            return re.findall(r'\d+', d["msg"])[0]
    
# elements = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/table')
# for inc, element in enumerate(elements):
#     print(inc, element.text)

# driver.quit()

