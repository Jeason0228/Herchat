import pandas as pd
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

def get_numbers():
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get("https://receive-smss.com")
    soup = BeautifulSoup(driver.page_source)
    numbers = soup.find_all("h4", attrs={"class": "number-boxes-itemm-number"})
    for n in numbers:
        print(n.get_text())

get_numbers()