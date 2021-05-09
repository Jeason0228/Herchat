base_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

r = requests.get(
    "https://ecp.hermes.com/is-logged-in?country=fr&locale=fr_fr",
    cookies={
        "datadome": ".oEOMO4Rijc_1GfgsOk3icx9M_tKH4nSKHJL-nOReHeB3Z9MHKfnv6v-XpN0mn8hJ38MNVW3TWv4KWIGRpMrlgtOSYgzSij-rQxgL0pau~"
    },
    headers={
        **base_headers,
        "Host": "ecp.hermes.com",
        "Accept": "*/*",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
        "Cookie": "datadome=.oEOMO4Rijc_1GfgsOk3icx9M_tKH4nSKHJL-nOReHeB3Z9MHKfnv6v-XpN0mn8hJ38MNVW3TWv4KWIGRpMrlgtOSYgzSij-rQxgL0pau~",
        "Cache-Control": "max-age=0",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/api/banners",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sun+May+09+2021+00:37:45+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=6841dbdf-05c7-449f-bd2b-c92d4a32e33f&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "has_js": "1",
        "datadome": "ZPWcpTYOOglAq7~perq39OcMLgbqRZmKtmXjFcU1V_~6yW2P.WX8_R._rq.yuCI9B.dPpQ_Ap2PfGAQOz7T6uAq1srZK4YJW-3czDRHOcN",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-NewRelic-ID": "VQUDVl9VDBAFUVdVAQMFUlc=",
        "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEzNDc5NjQiLCJhcCI6IjU5NTE0MTI0MiIsImlkIjoiNzdhZjE1NWE0NjhjY2QyNyIsInRyIjoiZTJlYThlMmU1ODRhMjU0OGUyMWVhZjhhNDJmMWNhYzAiLCJ0aSI6MTYyMDUxMzQ2NjM0NH19",
        "traceparent": "00-e2ea8e2e584a2548e21eaf8a42f1cac0-77af155a468ccd27-01",
        "tracestate": "1347964@nr=0-1-1347964-595141242-77af155a468ccd27----1620513466344",
        "X-Hermes-Request-ID": "firefox_0dfe783002aa0078b3db38ac64b69b68",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.hermes.com/fr/fr/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sun+May+09+2021+00%3A37%3A45+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=6841dbdf-05c7-449f-bd2b-c92d4a32e33f&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; has_js=1; datadome=ZPWcpTYOOglAq7~perq39OcMLgbqRZmKtmXjFcU1V_~6yW2P.WX8_R._rq.yuCI9B.dPpQ_Ap2PfGAQOz7T6uAq1srZK4YJW-3czDRHOcN",
        "Cache-Control": "max-age=0",
    },
)


r = requests.options(
    "https://cde.hermes.com/personalize/campaign?cid=FR_PS_HP_Selection_Homme,FR_PS_HP_ZH_PE21,FR_PS_HP_Selection_Femme",
    headers={
        **base_headers,
        "Host": "cde.hermes.com",
        "Accept": "*/*",
        "Access-Control-Request-Method": "POST",
        "Access-Control-Request-Headers": "content-type,x-hermes-request-id",
        "Referer": "https://www.hermes.com/",
        "Origin": "https://www.hermes.com",
        "Cache-Control": "max-age=0",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/content/hermesedito/V_169_SELLIER_MSILK_12sec-AVS.m3u8",
    headers={
        **base_headers,
        "Host": "assets.hermes.com",
        "Accept": "*/*",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
        "Cache-Control": "max-age=0",
        "If-Modified-Since": "Mon, 01 Feb 2021 16:36:43 GMT",
        "If-None-Match": '"84a979039137b86a1b8adf87de9c3bda"',
    },
)


# These variables probably come from the result of the request above
Host_1 = "stream.hermes.cn"


r = requests.post(
    "https://cde.hermes.com/personalize/campaign?cid=FR_PS_HP_Selection_Homme,FR_PS_HP_ZH_PE21,FR_PS_HP_Selection_Femme",
    cookies={
        "datadome": "ZPWcpTYOOglAq7~perq39OcMLgbqRZmKtmXjFcU1V_~6yW2P.WX8_R._rq.yuCI9B.dPpQ_Ap2PfGAQOz7T6uAq1srZK4YJW-3czDRHOcN"
    },
    headers={
        **base_headers,
        "Host": "cde.hermes.com",
        "Accept": "*/*",
        "X-Hermes-Request-ID": "firefox_f665235e6f8bfa3e16d8a39233ea1139",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
        "Cookie": "datadome=ZPWcpTYOOglAq7~perq39OcMLgbqRZmKtmXjFcU1V_~6yW2P.WX8_R._rq.yuCI9B.dPpQ_Ap2PfGAQOz7T6uAq1srZK4YJW-3czDRHOcN",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
    json='{"locale":"fr_fr","url_locale":"fr/fr"}',
)


# These variables probably come from the result of the request above
Host_2 = "stream.hermes.cn"


r = requests.get(
    "https://cdn-ukwest.onetrust.com/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/870afb0c-7f7a-4f57-a8d9-a461bd01c779.json",
    headers={
        **base_headers,
        "Host": "cdn-ukwest.onetrust.com",
        "Accept": "*/*",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
        "If-Modified-Since": "Mon, 03 May 2021 12:35:52 GMT",
        "If-None-Match": "0x8D90E2FFCFA9FEA",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


# These variables probably come from the result of the request above
Host_3 = "cdn-ukwest.onetrust.com"


r = requests.get(
    "https://stream.hermes.cn/hls-vod/hermesedito/_media_/673/6739f81c-60a3-4d98-b75a-6c1525235a9e.mp4.m3u8",
    headers={
        **base_headers,
        "Host": Host_2,
        "Accept": "*/*",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
        "Cache-Control": "max-age=0",
        "If-Modified-Since": "Thu, 01 Jan 1970 00:00:00 GMT",
    },
)


r = requests.post(
    "https://api-js.datadome.co/js/",
    headers={
        **base_headers,
        "Host": "api-js.datadome.co",
        "Accept": "*/*",
        "Content-type": "application/x-www-form-urlencoded",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
        "Cache-Control": "max-age=0",
    },
    json="jsData=%7B%22ttst%22%3A31%2C%22ifov%22%3Afalse%2C%22wdifts%22%3Afalse%2C%22wdifrm%22%3Afalse%2C%22wdif%22%3Afalse%2C%22br_h%22%3A340%2C%22br_w%22%3A1440%2C%22br_oh%22%3A900%2C%22br_ow%22%3A1440%2C%22nddc%22%3A1%2C%22rs_h%22%3A900%2C%22rs_w%22%3A1440%2C%22rs_cd%22%3A24%2C%22phe%22%3Afalse%2C%22nm%22%3Afalse%2C%22jsf%22%3Afalse%2C%22ua%22%3A%22Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A88.0)%20Gecko%2F20100101%20Firefox%2F88.0%22%2C%22lg%22%3A%22zh-CN%22%2C%22pr%22%3A2%2C%22hc%22%3A4%2C%22ars_h%22%3A900%2C%22ars_w%22%3A1440%2C%22tz%22%3A-120%2C%22str_ss%22%3Atrue%2C%22str_ls%22%3Atrue%2C%22str_idb%22%3Atrue%2C%22str_odb%22%3Afalse%2C%22plgod%22%3Afalse%2C%22plg%22%3A0%2C%22plgne%22%3A%22NA%22%2C%22plgre%22%3A%22NA%22%2C%22plgof%22%3A%22NA%22%2C%22plggt%22%3A%22NA%22%2C%22pltod%22%3Afalse%2C%22lb%22%3Afalse%2C%22eva%22%3A37%2C%22lo%22%3Afalse%2C%22ts_mtp%22%3A0%2C%22ts_tec%22%3Afalse%2C%22ts_tsa%22%3Afalse%2C%22vnd%22%3A%22%22%2C%22bid%22%3A%2220181001000000%22%2C%22mmt%22%3A%22empty%22%2C%22plu%22%3A%22empty%22%2C%22hdn%22%3Afalse%2C%22awe%22%3Afalse%2C%22geb%22%3Afalse%2C%22dat%22%3Afalse%2C%22med%22%3A%22defined%22%2C%22aco%22%3A%22probably%22%2C%22acots%22%3Afalse%2C%22acmp%22%3A%22maybe%22%2C%22acmpts%22%3Afalse%2C%22acw%22%3A%22probably%22%2C%22acwts%22%3Afalse%2C%22acma%22%3A%22maybe%22%2C%22acmats%22%3Afalse%2C%22acaa%22%3A%22maybe%22%2C%22acaats%22%3Afalse%2C%22ac3%22%3A%22%22%2C%22ac3ts%22%3Afalse%2C%22acf%22%3A%22maybe%22%2C%22acfts%22%3Afalse%2C%22acmp4%22%3A%22maybe%22%2C%22acmp4ts%22%3Atrue%2C%22acmp3%22%3A%22maybe%22%2C%22acmp3ts%22%3Afalse%2C%22acwm%22%3A%22maybe%22%2C%22acwmts%22%3Atrue%2C%22ocpt%22%3Afalse%2C%22vco%22%3A%22probably%22%2C%22vcots%22%3Afalse%2C%22vch%22%3A%22probably%22%2C%22vchts%22%3Atrue%2C%22vcw%22%3A%22probably%22%2C%22vcwts%22%3Atrue%2C%22vc3%22%3A%22%22%2C%22vc3ts%22%3Afalse%2C%22vcmp%22%3A%22%22%2C%22vcmpts%22%3Afalse%2C%22vcq%22%3A%22maybe%22%2C%22vcqts%22%3Afalse%2C%22vc1%22%3A%22probably%22%2C%22vc1ts%22%3Afalse%2C%22dvm%22%3A%22NA%22%2C%22sqt%22%3Afalse%2C%22so%22%3A%22landscape-primary%22%2C%22wbd%22%3Afalse%2C%22wbdm%22%3Atrue%2C%22wdw%22%3Atrue%2C%22ecpc%22%3Afalse%2C%22lgs%22%3Atrue%2C%22lgsod%22%3Afalse%2C%22bcda%22%3Afalse%2C%22idn%22%3Atrue%2C%22capi%22%3Afalse%2C%22svde%22%3Afalse%2C%22vpbq%22%3Atrue%2C%22xr%22%3Afalse%2C%22bgav%22%3Afalse%2C%22rri%22%3Atrue%2C%22idfr%22%3Afalse%2C%22ancs%22%3Atrue%2C%22inlc%22%3Atrue%2C%22cgca%22%3Afalse%2C%22inlf%22%3Atrue%2C%22tecd%22%3Afalse%2C%22sbct%22%3Atrue%2C%22aflt%22%3Atrue%2C%22rgp%22%3Atrue%2C%22bint%22%3Atrue%2C%22spwn%22%3Afalse%2C%22emt%22%3Afalse%2C%22bfr%22%3Afalse%2C%22dbov%22%3Afalse%2C%22glvd%22%3A%22ATI%20Technologies%20Inc.%22%2C%22glrd%22%3A%22AMD%20Radeon%20R9%20M370X%20OpenGL%20Engine%22%2C%22tagpu%22%3A8%2C%22prm%22%3Atrue%2C%22tzp%22%3A%22Europe%2FParis%22%2C%22cvs%22%3Atrue%2C%22usb%22%3A%22NA%22%7D&events=%5B%5D&eventCounters=%5B%5D&jsType=ch&cid=JH37jJlL5penSTC~cSUpi9tGwx3PW1BBjWsyicLBQYopJFXKWgKHvjJIUt8CS.9ZF~4eQRGW~IJB8pMvxBPUP6qKA5k5Wl~jjwhhiyMxOY&ddk=2211F522B61E269B869FA6EAFFB5E1&Referer=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252F&request=%252Ffr%252Ffr%252F&responsePage=origin&ddv=4.1.48",
)


r = requests.get(
    "https://cdn-ukwest.onetrust.com/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/a7ef0083-2008-4b25-9b1b-24fd6359406e/fr.json",
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/",
        "Origin": "https://www.hermes.com",
        "If-Modified-Since": "Mon, 03 May 2021 12:35:54 GMT",
        "If-None-Match": "0x8D90E2FFE64C127",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


# These variables probably come from the result of the request above
Referer_1 = "https://www.hermes.com/"
Origin_1 = "https://www.hermes.com"
Host_4 = "bam-cell.nr-data.net"


r = requests.get(
    "https://cdn-ukwest.onetrust.com/scripttemplates/6.17.0/assets/otCenterRounded.json",
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "*/*",
        "Referer": Referer_1,
        "Origin": Origin_1,
        "If-Modified-Since": "Tue, 27 Apr 2021 21:18:56 GMT",
        "If-None-Match": "0x8D909C21159C880",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://cdn-ukwest.onetrust.com/scripttemplates/6.17.0/assets/otPcCenter.json",
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "*/*",
        "Referer": Referer_1,
        "Origin": Origin_1,
        "If-Modified-Since": "Tue, 27 Apr 2021 21:18:56 GMT",
        "If-None-Match": "0x8D909C2113F0E09",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.post(
    "https://bam-cell.nr-data.net/events/1/5ca1a0d07f?a=556762243&v=1208.49599aa&to=ZVJbN0EFC0FQU0VQWVwYeABHDQpcHkBQXlNtWlgNUgMAQG5eXl1TbUFQBkQ7FVNWVQ%3D%3D&rst=2748&ck=1&ref=https://www.hermes.com/fr/fr/",
    headers={
        **base_headers,
        "Host": Host_4,
        "Accept": "*/*",
        "content-type": "text/plain",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json="bel.7;1,j,,243,243,86,'initialPageLoad,'https://www.hermes.com/fr/fr/,1,1,,,,151,!!'f3348d84-dcff-4022-8e67-3eb87e41f8ae,'1,!ce;5,'title,'Boutique en ligne officielle d'Hermès | Hermès France;5,'referer;5,'page_type,'front page;9,'department_code;5,'perfect_partner,'null;5,'perfect_partner_nb,'0;8,'stock_ecommerce;8,'stock_retail;5,'stock,'No Stock at all;a,'SRVYQQkfGE8=;2,1,vu,6g,q,2,'GET,5k,'assets.hermes.com:443,'/is/content/hermesedito/V_169_SELLIER_MSILK_12sec-AVS.m3u8,,d1,,'7,!!!;2,,12i,9d,m,8,j,5k,'stream.hermes.cn:443,'/hls-vod/hermesedito/_media_/673/6739f81c-60a3-4d98-b75a-6c1525235a9e.mp4.m3u8,,6w,,'9,!!!;2,,mo,gc,1,1,j,5k,'www.hermes.com:443,'/fr/fr/api/banners,,3f,,'5,'77af155a468ccd27,'e2ea8e2e584a2548e21eaf8a42f1cac0,kogbvl60;2,,k9,it,2,2,j,5k,'ecp.hermes.com:443,'/is-logged-in,,la,,'4,!!!;2,,wx,67,1,1,j,5k,'cdn-ukwest.onetrust.com:443,'/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/870afb0c-7f7a-4f57-a8d9-a461bd01c779.json,,21i,,'8,!!!;2,,ms,ge,n,n,'POST,5k,'cde.hermes.com:443,'/personalize/campaign,13,byr,,'6,!!!;2,,151,3d,1,,j,5k,y,'/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/a7ef0083-2008-4b25-9b1b-24fd6359406e/fr.json,,7lr,1,'11,!!!;2,,12m,7x,,1,11,5k,'api-js.datadome.co:443,'/js/,2gx,5t,,'10,!!!;2,,18x,3j,1,,j,5k,y,'/scripttemplates/6.17.0/assets/otCenterRounded.json,,1zf,1,'12,!!!;2,,18y,3i,3,1,j,5k,y,'/scripttemplates/6.17.0/assets/otPcCenter.json,,bdv,1,'13,!!!;b,96,!3,!-8v,1h,2d,1,1k,1n,,1l,,5,al,7,1u,qb,,2",
)


r = requests.post(
    "https://bam-cell.nr-data.net/events/1/5ca1a0d07f?a=556762243&v=1208.49599aa&to=ZVJbN0EFC0FQU0VQWVwYeABHDQpcHkBQXlNtWlgNUgMAQG5eXl1TbUFQBkQ7FVNWVQ%3D%3D&rst=11785&ck=1&ref=https://www.hermes.com/fr/fr/",
    headers={
        **base_headers,
        "Host": Host_4,
        "Accept": "*/*",
        "content-type": "text/plain",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json="bel.6;e,'fcp,ce,9;5,'title,'Boutique en ligne officielle d'Hermès | Hermès France;5,'referer;5,'page_type,'front page;9,'department_code;5,'perfect_partner,'null;5,'perfect_partner_nb,'0;8,'stock_ecommerce;8,'stock_retail;5,'stock,'No Stock at all;e,'load,1c4,9;5,1,2;5,3;5,4,5;9,6;5,7,8;5,9,a;8,b;8,c;5,d,e",
)


r = requests.post(
    "https://bam-cell.nr-data.net/events/1/5ca1a0d07f?a=556762243&v=1208.49599aa&to=ZVJbN0EFC0FQU0VQWVwYeABHDQpcHkBQXlNtWlgNUgMAQG5eXl1TbUFQBkQ7FVNWVQ%3D%3D&rst=42233&ck=1&ref=https://www.hermes.com/fr/fr/",
    headers={
        **base_headers,
        "Host": Host_4,
        "Accept": "*/*",
        "content-type": "text/plain",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json="bel.6;e,'pageHide,v1h,9;5,'title,'Boutique en ligne officielle d'Hermès | Hermès France;5,'referer;5,'page_type,'front page;9,'department_code;5,'perfect_partner,'null;5,'perfect_partner_nb,'0;8,'stock_ecommerce;8,'stock_retail;5,'stock,'No Stock at all",
)
