from time import sleep
import requests
import json
import re
import sys
import execjs
import urllib.parse as urlparse
from urllib.parse import parse_qs, urlencode
from pprint import pprint
from urllib import parse
import pickle

import urllib
from requests import cookies
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from twocaptcha import TwoCaptcha
from anticaptchaofficial.geetestproxyon import *

DATADOME_API = "https://api-js.datadome.co/js/"
ECOM_URL = "https://bck.hermes.com/customer-session?locale=fr_fr"
BACK_END_URL = "https://bck.hermes.com/products?locale=fr_fr&category=WOMENBAGSBAGSCLUTCHES&sort=relevance"


DATA = {
	"jsData": "{\"ttst\":78,\"ifov\":false,\"wdifts\":false,\"wdifrm\":false,\"wdif\":false,\"br_h\":256,\"br_w\":1440,\"br_oh\":900,\"br_ow\":1440,\"nddc\":1,\"rs_h\":900,\"rs_w\":1440,\"rs_cd\":24,\"phe\":false,\"nm\":false,\"jsf\":false,\"ua\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0\",\"lg\":\"zh-CN\",\"pr\":2,\"hc\":4,\"ars_h\":900,\"ars_w\":1440,\"tz\":-120,\"str_ss\":true,\"str_ls\":true,\"str_idb\":true,\"str_odb\":false,\"plgod\":false,\"plg\":0,\"plgne\":\"NA\",\"plgre\":\"NA\",\"plgof\":\"NA\",\"plggt\":\"NA\",\"pltod\":false,\"lb\":false,\"eva\":37,\"lo\":false,\"ts_mtp\":0,\"ts_tec\":false,\"ts_tsa\":false,\"vnd\":\"\",\"bid\":\"20181001000000\",\"mmt\":\"empty\",\"plu\":\"empty\",\"hdn\":false,\"awe\":false,\"geb\":false,\"dat\":false,\"med\":\"defined\",\"aco\":\"probably\",\"acots\":false,\"acmp\":\"maybe\",\"acmpts\":false,\"acw\":\"probably\",\"acwts\":false,\"acma\":\"maybe\",\"acmats\":false,\"acaa\":\"maybe\",\"acaats\":false,\"ac3\":\"\",\"ac3ts\":false,\"acf\":\"maybe\",\"acfts\":false,\"acmp4\":\"maybe\",\"acmp4ts\":true,\"acmp3\":\"maybe\",\"acmp3ts\":false,\"acwm\":\"maybe\",\"acwmts\":true,\"ocpt\":false,\"vco\":\"probably\",\"vcots\":false,\"vch\":\"probably\",\"vchts\":true,\"vcw\":\"probably\",\"vcwts\":true,\"vc3\":\"\",\"vc3ts\":false,\"vcmp\":\"\",\"vcmpts\":false,\"vcq\":\"maybe\",\"vcqts\":false,\"vc1\":\"probably\",\"vc1ts\":false,\"dvm\":\"NA\",\"sqt\":false,\"so\":\"landscape-primary\",\"wbd\":false,\"wbdm\":true,\"wdw\":true,\"ecpc\":false,\"lgs\":true,\"lgsod\":false,\"bcda\":false,\"idn\":true,\"capi\":false,\"svde\":false,\"vpbq\":true,\"xr\":false,\"bgav\":false,\"rri\":true,\"idfr\":false,\"ancs\":true,\"inlc\":true,\"cgca\":false,\"inlf\":true,\"tecd\":false,\"sbct\":true,\"aflt\":true,\"rgp\":true,\"bint\":true,\"spwn\":false,\"emt\":false,\"bfr\":false,\"dbov\":false,\"glvd\":\"ATI Technologies Inc.\",\"glrd\":\"AMD Radeon R9 M370X OpenGL Engine\",\"tagpu\":5,\"prm\":true,\"tzp\":\"Europe/Paris\",\"cvs\":true,\"usb\":\"NA\"}",
	"events": "[]",
	"eventCounters": "[]",
	"jsType": "ch",
	"ddk": "2211F522B61E269B869FA6EAFFB5E1",
	"Referer": "https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F",
	"request": "%2Ffr%2Ffr%2F",
	"responsePage": "origin",
	"ddv": "4.1.48"
}
 
base_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}


def get_datadome(cid="null"):
    DATA.update({
        "cid": cid,
    })
    datadome_api_data = parse.urlencode(DATA)

    datadome_api_request = requests.post(
        DATADOME_API,
        headers={
            **base_headers,
            "Host": "api-js.datadome.co",
            "Accept": "*/*",
            "Content-type": "application/x-www-form-urlencoded",
            "Origin": "https://www.hermes.com",
            "Referer": "https://www.hermes.com/",
        },
        data = datadome_api_data
        # data="jsData=%7B%22ttst%22%3A1231%2C%22ifov%22%3Afalse%2C%22wdifts%22%3Afalse%2C%22wdifrm%22%3Afalse%2C%22wdif%22%3Afalse%2C%22br_h%22%3A391%2C%22br_w%22%3A1440%2C%22br_oh%22%3A900%2C%22br_ow%22%3A1440%2C%22nddc%22%3A1%2C%22rs_h%22%3A900%2C%22rs_w%22%3A1440%2C%22rs_cd%22%3A24%2C%22phe%22%3Afalse%2C%22nm%22%3Afalse%2C%22jsf%22%3Afalse%2C%22ua%22%3A%22Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A88.0)%20Gecko%2F20100101%20Firefox%2F88.0%22%2C%22lg%22%3A%22zh-CN%22%2C%22pr%22%3A2%2C%22hc%22%3A4%2C%22ars_h%22%3A900%2C%22ars_w%22%3A1440%2C%22tz%22%3A-120%2C%22str_ss%22%3Atrue%2C%22str_ls%22%3Atrue%2C%22str_idb%22%3Atrue%2C%22str_odb%22%3Afalse%2C%22plgod%22%3Afalse%2C%22plg%22%3A0%2C%22plgne%22%3A%22NA%22%2C%22plgre%22%3A%22NA%22%2C%22plgof%22%3A%22NA%22%2C%22plggt%22%3A%22NA%22%2C%22pltod%22%3Afalse%2C%22lb%22%3Afalse%2C%22eva%22%3A37%2C%22lo%22%3Afalse%2C%22ts_mtp%22%3A0%2C%22ts_tec%22%3Afalse%2C%22ts_tsa%22%3Afalse%2C%22vnd%22%3A%22%22%2C%22bid%22%3A%2220181001000000%22%2C%22mmt%22%3A%22empty%22%2C%22plu%22%3A%22empty%22%2C%22hdn%22%3Afalse%2C%22awe%22%3Afalse%2C%22geb%22%3Afalse%2C%22dat%22%3Afalse%2C%22med%22%3A%22defined%22%2C%22aco%22%3A%22probably%22%2C%22acots%22%3Afalse%2C%22acmp%22%3A%22maybe%22%2C%22acmpts%22%3Afalse%2C%22acw%22%3A%22probably%22%2C%22acwts%22%3Afalse%2C%22acma%22%3A%22maybe%22%2C%22acmats%22%3Afalse%2C%22acaa%22%3A%22maybe%22%2C%22acaats%22%3Afalse%2C%22ac3%22%3A%22%22%2C%22ac3ts%22%3Afalse%2C%22acf%22%3A%22maybe%22%2C%22acfts%22%3Afalse%2C%22acmp4%22%3A%22maybe%22%2C%22acmp4ts%22%3Atrue%2C%22acmp3%22%3A%22maybe%22%2C%22acmp3ts%22%3Afalse%2C%22acwm%22%3A%22maybe%22%2C%22acwmts%22%3Atrue%2C%22ocpt%22%3Afalse%2C%22vco%22%3A%22probably%22%2C%22vcots%22%3Afalse%2C%22vch%22%3A%22probably%22%2C%22vchts%22%3Atrue%2C%22vcw%22%3A%22probably%22%2C%22vcwts%22%3Atrue%2C%22vc3%22%3A%22%22%2C%22vc3ts%22%3Afalse%2C%22vcmp%22%3A%22%22%2C%22vcmpts%22%3Afalse%2C%22vcq%22%3A%22maybe%22%2C%22vcqts%22%3Afalse%2C%22vc1%22%3A%22probably%22%2C%22vc1ts%22%3Afalse%2C%22dvm%22%3A%22NA%22%2C%22sqt%22%3Afalse%2C%22so%22%3A%22landscape-primary%22%2C%22wbd%22%3Afalse%2C%22wbdm%22%3Atrue%2C%22wdw%22%3Atrue%2C%22ecpc%22%3Afalse%2C%22lgs%22%3Atrue%2C%22lgsod%22%3Afalse%2C%22bcda%22%3Afalse%2C%22idn%22%3Atrue%2C%22capi%22%3Afalse%2C%22svde%22%3Afalse%2C%22vpbq%22%3Atrue%2C%22xr%22%3Afalse%2C%22bgav%22%3Afalse%2C%22rri%22%3Atrue%2C%22idfr%22%3Afalse%2C%22ancs%22%3Atrue%2C%22inlc%22%3Atrue%2C%22cgca%22%3Afalse%2C%22inlf%22%3Atrue%2C%22tecd%22%3Afalse%2C%22sbct%22%3Atrue%2C%22aflt%22%3Atrue%2C%22rgp%22%3Atrue%2C%22bint%22%3Atrue%2C%22spwn%22%3Afalse%2C%22emt%22%3Afalse%2C%22bfr%22%3Afalse%2C%22dbov%22%3Afalse%2C%22glvd%22%3A%22ATI%20Technologies%20Inc.%22%2C%22glrd%22%3A%22AMD%20Radeon%20R9%20M370X%20OpenGL%20Engine%22%2C%22tagpu%22%3A6%2C%22prm%22%3Atrue%2C%22tzp%22%3A%22Europe%2FParis%22%2C%22cvs%22%3Atrue%2C%22usb%22%3A%22NA%22%7D&events=%5B%5D&eventCounters=%5B%5D&jsType=ch&cid={}&ddk=2211F522B61E269B869FA6EAFFB5E1&Referer=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&request=%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&responsePage=origin&ddv=4.1.48"
    )
    if datadome_api_request.status_code == 200:
        # print(datadome_api_request.text)
        datadome = datadome_api_request.json()["cookie"].split(";")[0]
        return datadome.split("=")[1]
    else:
        raise Exception("Datadome api error with status code {}".format(
            datadome_api_request.status_code))

def get_js_object(js_file_path):
    """获取js可执行对象"""
    with open(js_file_path, encoding='GBK') as f:
        js_file = f.read()
        return execjs.compile(js_file)

def get_ecom_sess(datadome):
    ecom_request = requests.get(
        ECOM_URL,
        cookies={
            "datadome": datadome
        },
        headers={
            **base_headers,
            "Host": "bck.hermes.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Cookie": "datadome=%s" % datadome,
            "Upgrade-Insecure-Requests": "1",
        },
    )
    if ecom_request.status_code == 200:
        # print(ecom_request.text)
        ecom_sess = ecom_request.cookies["ECOM_SESS"]
        new_datadome = ecom_request.cookies.get("datadome")

        return {
            "datadome": new_datadome,
            "ecom_sess": ecom_sess
        }
    else:
        # print(ecom_request.text)
        challenge = get_captcha_challenge_api()
        # print(captcha_url)
        print(challenge)
        captcha_pass_anti(challenge)
        # captcha_pass(ecom_request.json()["url"])

        # raise Exception("Get ECOM_SESS cookies error with status code {}".format(
        #     ecom_request.status_code))

def get_captcha_challenge_api():
    # driver = init_webdriver()
    # driver.get(url)
    # captcha_url = driver.find_element_by_xpath("//iframe").get_attribute("src")
    # # captcha_url = None

    # iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe")))
    # driver.switch_to.frame(iframe)
    # html = driver.page_source
    # # print(html)
    # driver.quit()
    cap_url = "https://api-na.geetest.com/register.php?client_type=web&digestmod=md5&gt=1e505deed3832c02c96ca5abe70df9ab&json_format=1"
    response = requests.get(cap_url)
    data = response.json()
    # req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
    # req.add_header("User-Agent", base_headers['User-Agent'])
    # res = urllib.request.urlopen(req)
    # print(data)
    return data["challenge"]

def get_captcha_challenge_sel(url):
    driver = init_webdriver()
    driver.get(url)
    cookies = driver.get_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get(url)


    sleep(5)
    # print(cookies)
    # pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    # driver.add_cookie
    # print(driver.page_source)
    # captcha_url = driver.find_element_by_xpath("//iframe").get_attribute("src")
    # # captcha_url = None
    # print(captcha_url)
    # sleep(5)

    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe")))
    driver.switch_to.frame(iframe)
    # iframe2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//iframe")))
    # driver.switch_to.frame(iframe2)
    html = driver.page_source
    # print(html)
    # driver.quit()
    # cap_url = "https://api-na.geetest.com/register.php?client_type=web&digestmod=md5&gt=1e505deed3832c02c96ca5abe70df9ab&json_format=1"
    # response = requests.get(cap_url)
    # data = response.json()
    # req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
    # req.add_header("User-Agent", base_headers['User-Agent'])
    # res = urllib.request.urlopen(req)
    # print(data)
    # return data["challenge"]

    return re.search("challenge: '(\w*)'", html).group(1)

def init_webdriver():
    """Simple Function to initialize and configure Webdriver"""
    # options = Options()
    # options.add_argument("-headless")
    # profile = webdriver.FirefoxProfile()
    firefox_options = webdriver.FirefoxOptions()

    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--enable-javascript")
    # firefox_options.add_argument("user-data-dir=selenium")
    profile = webdriver.FirefoxProfile("/Users/PENGHanyuan/Documents/Programs/Herchat/Herchat/selenium")
    profile.set_preference("general.useragent.override", base_headers["User-Agent"])
    
    # firefox_options.add_argument('--proxy-server=%s' % PROXY)

    firefox = webdriver.Firefox(options=firefox_options, firefox_profile=profile)
    return firefox

def save_cookies(cookies, path=None):
    with open('../json/ecom_sess.json', 'w') as outfile:
        json.dump(cookies, outfile)


def request_ecom_cookies(path="../json/ecom_sess.json"):
    with open(path, 'r') as outfile:
        cid = json.load(outfile)["datadome"]

    datadome = get_datadome(cid=cid)

    ecom_cookie = get_ecom_sess(datadome=datadome)
    save_cookies(cookies=ecom_cookie, path=path)


# print(datadome_api_data)
def get_captcha_challenge():
    captcha_request = requests.get(
        "https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAMtIGyAu0fZMAsKxZNA%3D%3D&hash=2211F522B61E269B869FA6EAFFB5E1&cid=_l_rzzjFbp6FvR.2cssuYfSwZJLmWkRz7VI_beddw.Hfy3oXpcIlSVmcy_t2CoJv6.RRPICzAHDN9jL3MWIn1JrH9k903SzqC2DYfb.5nt&t=fe&referer=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&s=13461",
        cookies={
            "_ga": "GA1.2.2092610686.1620480215",
            "_gid": "GA1.2.1828156247.1620686654",
            "datadome": "21S.fJsCFr9Xnynz-tl8ZwljUVe857C~BWeD4~9IYV4YutlKXSCWwB_ULIu8202nCgZ4ikgRJKMdTX0Gts3R1Ynqe.EqBFWyM3diy4HlGz",
            "_cs_mk": "0.5568712272477504_1620759956558",
        },
        headers={
            **base_headers,
            "Host": "geo.captcha-delivery.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Cookie": "_ga=GA1.2.2092610686.1620480215; _gid=GA1.2.1828156247.1620686654; datadome=21S.fJsCFr9Xnynz-tl8ZwljUVe857C~BWeD4~9IYV4YutlKXSCWwB_ULIu8202nCgZ4ikgRJKMdTX0Gts3R1Ynqe.EqBFWyM3diy4HlGz; _cs_mk=0.5568712272477504_1620759956558",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0",
        },
    )
    # print(captcha_request.text)
    return captcha_request.text[-400:-100].strip().split("\n")[3].strip().split(":")[1].strip()[1:-2]

def captcha_pass_anti(challenge, url, cap_url):
    solver = geetestProxyon()
    solver.set_verbose(1)
    solver.set_key("cda594b619433a2b0d5a04971da967bf")
    print(url)
    solver.set_website_url(url)
    solver.set_gt_key("1e505deed3832c02c96ca5abe70df9ab")
    solver.set_challenge_key(challenge)
    solver.set_js_api_domain("api-na.geetest.com")
    solver.set_proxy_type("http")
    solver.set_proxy_address("35.181.48.9")
    solver.set_proxy_port(3128)
    solver.set_user_agent(base_headers["User-Agent"])
    token = solver.solve_and_return_solution()
    if token != 0:
        print("result tokens: ")
        print(token)
        check_challenge(cap_url, challenge, token["validate"], token["seccode"])
    else:
        print("task finished with error "+solver.error_code)

def captcha_pass(challenge, url):
    api_key = "b2097c17b72dc4323d74ca09834a7c8d"
    solver = TwoCaptcha(api_key)
    print("Checking captcha...")

    try:
        result = solver.geetest(gt='1e505deed3832c02c96ca5abe70df9ab',
                                apiServer='api-na.geetest.com',
                                challenge=challenge,
                                url=BACK_END_URL)

    except Exception as e:
        print(e)
    else:
        # sys.exit('result: ' + str(result))
        print(result)
        geetest = json.loads(result["code"])
        check_challenge(url, challenge, geetest["geetest_validate"], geetest["geetest_seccode"])

def get_magic_number(r, t, ua, ul):
    full_page_t1_js = get_js_object("./js/hermes_w1.js")
    val = full_page_t1_js.call('ddExecuteCaptchaChallenge', r, t, ua, ul)
    print(val)
    return val

def make_js_request(url):
    js_request = get_js_object("./js/request.js")
    val = js_request.call('send_check', url)
    return val
    
def check_challenge(url, challenge, validate, seccode):
    datadome = get_datadome()
    parsed = urlparse.urlparse(url)
    cid = parse_qs(parsed.query)['cid'][0]
    s = parse_qs(parsed.query)['s'][0]
    print(cid)
    print(s)
    magic_number = get_magic_number(cid, 10, base_headers["User-Agent"], "zh-cn")
    data = {
        "cid": cid,
        "icid": "AHrlqAAAAAMAZKzVCYKMqIYAsKxZNA==",
        "ccid": datadome,
        "geetest-response-challenge": challenge,
        "geetest-response-validate": validate,
        "geetest-response-seccode": seccode,
        "hash": "2211F522B61E269B869FA6EAFFB5E1",
        "ua": base_headers["User-Agent"],
        "referer": BACK_END_URL,
        "parent_url": "https://bck.hermes.com/",
        "x-forwarded-for": "",
        "captchaChallenge": magic_number,
        "s": s
    }
    decoded_data = parse.urlencode(data)
    req = urllib.request.Request("https://geo.captcha-delivery.com/captcha/check?" + decoded_data, method="GET")
    req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
    req.add_header("User-Agent", base_headers['User-Agent'])
    req.add_header("Referer", url)
    res = urllib.request.urlopen(req)
    print(res)
    # print("https://geo.captcha-delivery.com/captcha/check?" + data)
    # r = make_js_request("https://geo.captcha-delivery.com/captcha/check?" + data)
    # r = requests.get(
    #     "https://geo.captcha-delivery.com/captcha/check?" + data,
    # headers={
    #     "Accept": "*/*",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    #     "Connection": "keep-alive",
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "Host": "geo.captcha-delivery.com",
    #     "User-Agent": base_headers['User-Agent'],
    #     "Referer": url,
    # },
    # # params=data
    # )
    # print("check:", r)
    # print("check:", r.text)
    # print("new sess:", r.cookies)

def test():
    datadome = get_datadome()

    # ecom_cookie = get_ecom_sess(datadome=datadome)
    get_captcha_challenge_sel(BACK_END_URL)
    # captcha_pass("2e3333c02746fd190f7d02a0d233f9ba", "https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAdYRZBkoLQPYAjWlBjw==&cid=ITS670mQSdV.w~beohDabc17fMKUB9o6PEVoA701..H2LX3uGIAnztRBNZavOcPFQTGFlSfUoy2btG6jTHE~qapNbQxGwl0KjCe8IIkKPh&referer=http%3A%2F%2Fbck.hermes.com%2Fproducts%3Fcategory%3DWOMENBAGSBAGSCLUTCHES%26locale%3Dfr_fr%26sort%3Drelevance&hash=2211F522B61E269B869FA6EAFFB5E1&t=fe&s=8945")
    # print(ecom_cookie)
    # make_js_request("https://geo.captcha-delivery.com/captcha/check?cid=A2.nfaIbEjVuBpIRcexa9ujcpC_6kn03O.FdDlnJe4pX-QInXSzBbUCpbdP..AWCyAt0A_F.Fl5MdlhFXFbGCUzdwUxpL._ZiFW0L-lwct&icid=AHrlqAAAAAMAZKzVCYKMqIYAsKxZNA%3D%3D&ccid=null&geetest-response-challenge=bf4d479d07431ba3793fa9e397633ddc&geetest-response-validate=9bbde1fab83de3dc02a8755cac2fe0f8&geetest-response-seccode=9bbde1fab83de3dc02a8755cac2fe0f8%7Cjordan&hash=2211F522B61E269B869FA6EAFFB5E1&ua=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10.15%3B+rv%3A88.0%29+Gecko%2F20100101+Firefox%2F88.0&referer=https%3A%2F%2Fbck.hermes.com%2Fcustomer-session%3Flocale%3Dfr_fr&parent_url=https%3A%2F%2Fbck.hermes.com%2F&x-forwarded-for=&captchaChallenge=963508&s=8945")
    # save_cookies(ecom_cookie)
    # text = get_captcha_challenge()
    # print(text)
    
if __name__ == "__main__":
    test()