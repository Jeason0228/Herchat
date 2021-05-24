# coding:utf-8
# 等待时间 产生随机数
import time
# Geettest 验证码
import geecrack
# web测试
from selenium import webdriver
# 鼠标操作
# 预期条件
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from param import get_track

driver = webdriver.Firefox()
driver.get("https://www.hermes.com/fr/fr/")
iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe")))
driver.switch_to.frame(iframe)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "geetest_radar_tip"))).click()
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_radar_tip')))

submit_btn = driver.find_element_by_class_name('geetest_radar_tip')

submit_btn.click()

# 加载 Geetest 验证码
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_slice')))
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_fullbg')))

# 保存包含缺口的页面截图
bg_path = geecrack.save_bg(driver)
# 保存完整背景图
full_bg_path = geecrack.save_full_bg(driver)
# 移动距离
distance = geecrack.get_offset(full_bg_path, bg_path, offset=35)
# 获取移动轨迹
track = geecrack.get_track(distance)
# 滑动圆球至缺口处
geecrack.drag_the_ball(driver, track)
# 到此就完成滑动验证码啦~
time.sleep(10)
driver.close()
