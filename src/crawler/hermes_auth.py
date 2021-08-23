import requests
import json
from pprint import pprint



DATADOME_API = "https://api-js.datadome.co/js/"
ECOM_URL = "https://ecp.hermes.com/is-logged-in?country=fr&locale=fr_fr"


base_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
}

def get_datadome():
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
    data="jsData=%7B%22ttst%22%3A1231%2C%22ifov%22%3Afalse%2C%22wdifts%22%3Afalse%2C%22wdifrm%22%3Afalse%2C%22wdif%22%3Afalse%2C%22br_h%22%3A391%2C%22br_w%22%3A1440%2C%22br_oh%22%3A900%2C%22br_ow%22%3A1440%2C%22nddc%22%3A1%2C%22rs_h%22%3A900%2C%22rs_w%22%3A1440%2C%22rs_cd%22%3A24%2C%22phe%22%3Afalse%2C%22nm%22%3Afalse%2C%22jsf%22%3Afalse%2C%22ua%22%3A%22Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A88.0)%20Gecko%2F20100101%20Firefox%2F88.0%22%2C%22lg%22%3A%22zh-CN%22%2C%22pr%22%3A2%2C%22hc%22%3A4%2C%22ars_h%22%3A900%2C%22ars_w%22%3A1440%2C%22tz%22%3A-120%2C%22str_ss%22%3Atrue%2C%22str_ls%22%3Atrue%2C%22str_idb%22%3Atrue%2C%22str_odb%22%3Afalse%2C%22plgod%22%3Afalse%2C%22plg%22%3A0%2C%22plgne%22%3A%22NA%22%2C%22plgre%22%3A%22NA%22%2C%22plgof%22%3A%22NA%22%2C%22plggt%22%3A%22NA%22%2C%22pltod%22%3Afalse%2C%22lb%22%3Afalse%2C%22eva%22%3A37%2C%22lo%22%3Afalse%2C%22ts_mtp%22%3A0%2C%22ts_tec%22%3Afalse%2C%22ts_tsa%22%3Afalse%2C%22vnd%22%3A%22%22%2C%22bid%22%3A%2220181001000000%22%2C%22mmt%22%3A%22empty%22%2C%22plu%22%3A%22empty%22%2C%22hdn%22%3Afalse%2C%22awe%22%3Afalse%2C%22geb%22%3Afalse%2C%22dat%22%3Afalse%2C%22med%22%3A%22defined%22%2C%22aco%22%3A%22probably%22%2C%22acots%22%3Afalse%2C%22acmp%22%3A%22maybe%22%2C%22acmpts%22%3Afalse%2C%22acw%22%3A%22probably%22%2C%22acwts%22%3Afalse%2C%22acma%22%3A%22maybe%22%2C%22acmats%22%3Afalse%2C%22acaa%22%3A%22maybe%22%2C%22acaats%22%3Afalse%2C%22ac3%22%3A%22%22%2C%22ac3ts%22%3Afalse%2C%22acf%22%3A%22maybe%22%2C%22acfts%22%3Afalse%2C%22acmp4%22%3A%22maybe%22%2C%22acmp4ts%22%3Atrue%2C%22acmp3%22%3A%22maybe%22%2C%22acmp3ts%22%3Afalse%2C%22acwm%22%3A%22maybe%22%2C%22acwmts%22%3Atrue%2C%22ocpt%22%3Afalse%2C%22vco%22%3A%22probably%22%2C%22vcots%22%3Afalse%2C%22vch%22%3A%22probably%22%2C%22vchts%22%3Atrue%2C%22vcw%22%3A%22probably%22%2C%22vcwts%22%3Atrue%2C%22vc3%22%3A%22%22%2C%22vc3ts%22%3Afalse%2C%22vcmp%22%3A%22%22%2C%22vcmpts%22%3Afalse%2C%22vcq%22%3A%22maybe%22%2C%22vcqts%22%3Afalse%2C%22vc1%22%3A%22probably%22%2C%22vc1ts%22%3Afalse%2C%22dvm%22%3A%22NA%22%2C%22sqt%22%3Afalse%2C%22so%22%3A%22landscape-primary%22%2C%22wbd%22%3Afalse%2C%22wbdm%22%3Atrue%2C%22wdw%22%3Atrue%2C%22ecpc%22%3Afalse%2C%22lgs%22%3Atrue%2C%22lgsod%22%3Afalse%2C%22bcda%22%3Afalse%2C%22idn%22%3Atrue%2C%22capi%22%3Afalse%2C%22svde%22%3Afalse%2C%22vpbq%22%3Atrue%2C%22xr%22%3Afalse%2C%22bgav%22%3Afalse%2C%22rri%22%3Atrue%2C%22idfr%22%3Afalse%2C%22ancs%22%3Atrue%2C%22inlc%22%3Atrue%2C%22cgca%22%3Afalse%2C%22inlf%22%3Atrue%2C%22tecd%22%3Afalse%2C%22sbct%22%3Atrue%2C%22aflt%22%3Atrue%2C%22rgp%22%3Atrue%2C%22bint%22%3Atrue%2C%22spwn%22%3Afalse%2C%22emt%22%3Afalse%2C%22bfr%22%3Afalse%2C%22dbov%22%3Afalse%2C%22glvd%22%3A%22ATI%20Technologies%20Inc.%22%2C%22glrd%22%3A%22AMD%20Radeon%20R9%20M370X%20OpenGL%20Engine%22%2C%22tagpu%22%3A6%2C%22prm%22%3Atrue%2C%22tzp%22%3A%22Europe%2FParis%22%2C%22cvs%22%3Atrue%2C%22usb%22%3A%22NA%22%7D&events=%5B%5D&eventCounters=%5B%5D&jsType=ch&cid=2Mrn1w66vj7VA50TVmEpz-u9O3duAD6lJZLaQ32FZKduc4tAGrlJF~nGbCABit7RmvxvdQRT1NMNPZU8iSppLAOFlg1JrxLB7vGac9Mf9Q&ddk=2211F522B61E269B869FA6EAFFB5E1&Referer=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&request=%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&responsePage=origin&ddv=4.1.48"
    )
    if datadome_api_request.status_code == 200:
        datadome = datadome_api_request.json()["cookie"].split(";")[0]
        return datadome
    else:
        raise Exception("Datadome api error with status code {}".format(datadome_api_request.status_code))

def get_ecom_sess(datadome):
    datadome_val = datadome.split("=")[1]
    ecom_request = requests.get(
        ECOM_URL,
        cookies={
            "datadome": datadome_val
        },
        headers={
            **base_headers,
            "Host": "ecp.hermes.com",
            "Accept": "*/*",
            "Origin": "https://www.hermes.com",
            "Referer": "https://www.hermes.com/",
            "Cookie": datadome,
            "TE": "Trailers"
        },
    )
    if ecom_request.status_code == 200:
        ecom_sess = ecom_request.cookies["ECOM_SESS"]
        new_datadome = ecom_request.cookies["datadome"]

        return {
            "datadome": new_datadome,
            "ecom_sess": ecom_sess
        }
    else:
        raise Exception("Get ECOM_SESS cookies error with status code {}".format(ecom_request.status_code))

def save_cookies(cookies):
    with open('../json/ecom_sess.json', 'w') as outfile:
        json.dump(cookies, outfile)

datadome = get_datadome()

ecom_cookie = get_ecom_sess(datadome=datadome)
save_cookies(cookies=ecom_cookie)