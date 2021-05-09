import os
from selenium import webdriver
import time
from scrapy.selector import Selector
import re
from shutil import which
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
    
from stem import Signal
from stem.control import Controller
import requests
import socks, socket
import time
'''
滑动拼图验证码
1、打开selenum
2、点击滑块，出现缺口和移动缺口的css里的left，可以计算滑动距离
3、滑动滑块
'''
img_abs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
class TestCase(object):
 
    def __init__(self):
        self.url = 'https://www.hermes.com/fr/fr'
 
    def get_verification_code_img(self):
        self.driver = webdriver.Chrome()
 
        self.driver.maximize_window()
        self.driver.get(self.url)
        try:
            iframe = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe")))
            self.driver.switch_to.frame(iframe)
            verify = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "geetest_radar_tip")))
            verify.click()
            print("Anti-robot program triggered")
        except Exception as e:
            print(e)
            print("Anti-robot not found")
        canvas = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//canvas[@class='geetest_canvas_bg geetest_absolute']")))
        action = webdriver.ActionChains(self.driver)
        action.click_and_hold(canvas).perform() # 点击并保持不松开
        html = self.driver.page_source
        print(html)
        miss_style = Selector(text=html).xpath("//div[@class='missblock']/@style").extract_first()
        print(miss_style)
        miss_left = re.match(r'.*left: (.*?)px;.*',miss_style).group(1)
 
        block_style = Selector(text=html).xpath("//div[@class='targetblock']/@style").extract_first()
        block_left = re.match(r'.*left: (.*?)px;.*',block_style).group(1)
        left = int(float(block_left))-int(miss_left)
        action.move_by_offset(left,0)# 根据css宽度查出340
        action.release().perform() # 松开鼠标
        time.sleep(10)
 
    def run(self):
        self.get_verification_code_img()
if __name__ == '__main__':
    TestCase().run()
