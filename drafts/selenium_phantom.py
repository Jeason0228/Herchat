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
    chrome_options.add_argument('Connection=keep-alive')
    chrome_options.add_argument('Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    chrome_options.add_argument('Cache-Control=max-age=0')
    chrome_options.add_argument('Accept-Encoding=gzip, deflate, br')
    chrome_options.add_argument('Accept-Language=zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2')
    chrome_options.add_argument('If-None-Match="1620505827-0-gzip"')
    chrome_options.add_argument('Upgrade-Insecure-Requests=1')
    chrome_options.add_argument('User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0')
    # chrome_options.add_argument('Cookie=Cookie: OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+22%3A46%3A28+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=1c1dd886-b387-40d4-a3d9-9b043800f7d8&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; has_js=1; datadome=A4l3iIndV2~VhcJqkhJW~2Fl06aLeEy8Y6FdFbWGcETItP_VSaXEr4zQS9UrE~qLmjGuzpXzkp_iDAHnvEg5Tf3LGNOOUP463Thydokqa6')
    chrome_options.add_argument('Host=www.hermes.com')
    

    # chrome_options.add_argument("--headless")
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