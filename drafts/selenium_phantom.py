from shutil import which
from selenium import webdriver
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
import pprint
BACK = "https://bck.hermes.com/products?locale=fr_fr&category=WOMENBAGSBAGSCLUTCHES&sort=relevance"
PROXY="socks5://127.0.0.1:9050"

def init_webdriver():
    """Simple Function to initialize and configure Webdriver"""
    # options = Options()
    # options.add_argument("-headless")
    # profile = webdriver.FirefoxProfile()
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)

    chrome = webdriver.Chrome(options=chrome_options)
    return chrome


# with Controller.from_port(port=9051) as controller:
#     controller.authenticate()

#     controller.signal(Signal.NEWNYM)
driver = init_webdriver()

time.sleep(3)

driver.get("https://www.hermes.com")

# print(driver.page_source)
# 获取cookie列表
cookie_list=driver.get_cookies()
print(cookie_list)
# 格式化打印cookie
cookie_dict = {}
# print(cookie_list)
for cookie in cookie_list:
    cookie_dict[cookie['name']]=cookie['value']
pprint.pprint(cookie_dict)
time.sleep(3)
# driver.get(BACK)

# try:
#     iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe")))
#     driver.switch_to.frame(iframe)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "geetest_radar_tip"))).click()
#     # driver.find_element_by_class_name("geetest_radar_tip").click()
#     print("Anti-robot program triggered")
# except Exception as e:
#     print(e)
#     print("Anti-robot not found")
# driver.switch_to.default_content()
# print(driver.title)
# print(driver.page_source)
# # driver.find_element_by_class_name("load-more-button").click()
# search = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "block-hermes-commerce-nav-search")))
# # time.sleep(2)
# # search = driver.find_element_by_id('search-suggestion-field')
# search.send_keys("garden party")
# search.send_keys(Keys.RETURN) # hit return after you enter search text
# time.sleep(2)
# elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//h3[@class='product-item-name']")))
# # elements = driver.find_elements_by_xpath('/html/body/h-root/div/h-shell/div/main/div/h-main-content/div/h-grid-page/div/div/div[2]/h-grid-results/ul/li[5]/h-grid-result-item/div/a/div[2]/h3')
# for inc, element in enumerate(elements):
#     print(inc, element.text)

driver.quit()