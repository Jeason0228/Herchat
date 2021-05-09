base_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

r = requests.post(
    "https://privacyportal-uk.onetrust.com/request/v1/consentreceipts",
    headers={
        **base_headers,
        "Host": "privacyportal-uk.onetrust.com",
        "Accept": "*/*",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
        "TE": "Trailers",
    },
    json='{"requestInformation":"eyJhbGciOiJSUzUxMiJ9.eyJvdEp3dFZlcnNpb24iOjEsInByb2Nlc3NJZCI6ImZlOGU1MjYxLTYzMTEtNDZkMS1hMTUwLWEyMWJkNDA0Y2RkMCIsInByb2Nlc3NWZXJzaW9uIjo1MSwiaWF0IjoiMjAyMC0xMC0wNVQxMjoxMToyNi4yMDciLCJtb2MiOiJDT09LSUUiLCJzdWIiOiJDb29raWUgVW5pcXVlIElkIiwiaXNzIjpudWxsLCJ0ZW5hbnRJZCI6IjliYzc2ZTM5LWEzNTAtNDk1YS1iMTc1LTk4OTVjZWU3NzMxNyIsImRlc2NyaXB0aW9uIjoiVGhpcyBjb2xsZWN0aW9uIHBvaW50IGNhcHR1cmVzIHRoZSBjdXJyZW50IHNpdGUgdmlzaXRvciBjb25zZW50IHByZWZlcmVuY2VzIGZvciB0aGUgZG9tYWluOiBoZXJtZXMuY29tL2ZyL2ZyLy1lbiBzcGVjaWZpZWQuIiwiY29uc2VudFR5cGUiOiJDT09LSUVCQU5ORVIiLCJkb3VibGVPcHRJbiI6ZmFsc2UsInJlY29uZmlybUFjdGl2ZVB1cnBvc2UiOmZhbHNlLCJkeW5hbWljQ29sbGVjdGlvblBvaW50IjpmYWxzZSwiYXV0aGVudGljYXRpb25SZXF1aXJlZCI6ZmFsc2UsInBvbGljeV91cmkiOiJoZXJtZXMuY29tL2ZyL2ZyLyIsImFsbG93Tm90R2l2ZW5Db25zZW50cyI6ZmFsc2UsInB1cnBvc2VzIjpbeyJpZCI6IjliNDg5ZWMzLWI4OTUtNDFlZi1iNmNmLWI2ZDA4ZjI2NDU4YiIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjkwZWQ0NmZlLTA2YzAtNDViOS1hZTUzLTJjYTc4OWU3ZDNiZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjU5Y2E2MTYyLTI5NTEtNDBmZC05NGU5LWIwNTA2YzExZDVmZCIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjA4ZTFlNWY0LWVkZmQtNDU2MS1hNmNlLTM5OGNkMGEyZGYyZiIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImRiYjJjMjQ1LTE1MTAtNDlmMi1iOTdjLTliNjM0Y2E0YTFjMyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjgxY2FjZWNiLTZlYTMtNGYzZC04YTkwLTc4NDY4Yzg4YmIxOCIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjY3YTFmNGQyLWRiM2QtNGQ1YS1hZDQ3LTFmZDYzN2ZmYjkwNiIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImE4YTlmNDliLTNjMTAtNDAzNy04NjMxLWY5NzZhMGI0OWNiNSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImI0M2Q1YTBiLTBlODMtNDlmMi1hZjIyLWI2ZGU5ZTZjOWU5OCIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjhkNWNhMmIwLTgxYmUtNDQ0MS1iNjgwLWZkMTcyM2IzNjZjMSIsInZlcnNpb24iOjIsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjhkMDAxZjI2LWE5MWItNDViYi04ZGNiLTEyZGUxYzBjNWNmOSIsInZlcnNpb24iOjIsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjUwYzUzYjZlLThiMjktNDdlZC04OTNiLWY2MWY0ODdmM2VhZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjNiYzAyOWRmLWM1YzctNGVhZC1hMmY1LTE3Y2E4ZjBmNzM3OCIsInZlcnNpb24iOjIsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjFmOTU3NzhlLTU3NGUtNDgwMS1hMTBhLTFlZjYxNjI5ZTMxZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImE5N2U2MGIxLTFjMTYtNGRkMC04ZjYxLTFmZWUxY2Y3YzdjYSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImMxYzRjMWQ5LWVmODQtNGRmMS1hODE5LWFjMzcyZDU1MWY2MCIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjNkYTYyOTUxLTk3MDEtNGNjYS05ZGViLTZjYzMxYzM1MDlhZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjM4ZDI5YmE2LWNiMjItNDA0Ny05MDdlLTFhOGNmNmIxZDIwMiIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjkwOTA4MDdkLTQ1ODktNDNhNS04MDE1LWM5Mzc1NWQ0OGJhMSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjEwNGRkM2RjLTI2YzktNDhmMy1iNDNhLTJkYzBmNDE2ZTBkNSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6Ijk1YzViZjVlLWQxNzctNDM0NC1iZmI5LTRlYWQxZTk0NGQ2MyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImNiYmU2ZGVjLWJkNWItNDVjNi1hNjYyLTUwNjFhMjZlZTAzZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6Ijg0MDI4ZTA1LTY3MGQtNGIyNy04YWM0LWQyYzAxYjY0Mzg1MyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjZlNWQwODliLTk3MjUtNDQ5ZC1iNWJlLTNlMWQ1YTYxMjIzNyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjYzYTYxNWU4LWJjOWMtNGIxYS04MTMwLWFhOTQ1ODlmMDVhOCIsInZlcnNpb24iOjIsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImM5ODVjOGFhLWNmMGYtNDI4ZS1hZDk5LWYwYzQyMGM5ZGIyNyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImQ0OGZiNzAzLWQzYjAtNDE3ZS04NTc4LTgzN2FjN2M0NjkzNSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6Ijk1Nzg3NmNlLTU3ODgtNDQxMi1iN2RiLTM5OGU5YjIzM2RlNSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjIyMTBiMTM3LTBjMDMtNDhmNC04ZjlkLTI3Mjg0MzNiYTU2ZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX1dLCJub3RpY2VzIjpbXSwiZHNEYXRhRWxlbWVudHMiOlsiVXNlckFnZW50IiwiQ291bnRyeSIsIkludGVyYWN0aW9uVHlwZSJdfQ.Nlkh1C9HzKenjutAhtyvgNMvwQicgKtN8lhOKZBQ4MMtbIPpGxjX8aYK4B7HkgR7k0KKQEioMmzMmamJzC584EZtm-AeUfXMrQ-GhPf5-jCXEylvw86t7a9b-4Hh7IqqyDMc1IrWlHvSm5q3tUfVw9JuJOQW3qSI-GeN5pK8nrGbF32YUHpgTNopwbO_xfdouMFHuxiJ0x4kS5aXINIP0zbHkx7NM7iLUNnQiS0UXWxrmX3cTAwac2EE6C-zOpgYh2Hp0Kc00jCWEJGpJAlQkjVa2u6dlNo7KGW_xbhSIu8l5sMx3mVOay4-_g1qPTCU--VFDM_ccNDYTtEoOQaOdW5rW5ZT7GYsK-JznhgM9ltkF8t-pmz_fQN8t_nT9rkmSjRZTEZQzY6cLEhOwjBuQ5wLY7ucht1GhhzWODpTbBrA8W52Dbw0Vv0WQLLVTTcybGG_8TCo_Qoyh3Y4yJQBYgKSK1FpytaHOMeATVE5iW90z4rmbjyeoXoxAuhK-QATFJ4o8vqVxx9kwppIhIQ_SyBmX4J5XhpPoblG6nqZVjAmecT8vzj_Zs8xXDWDnJsXULcUHvQuyxIO0RO2rZ3eoCQAqQg-bDHnLo-KT5PGcIiiJPnwfTj1Cw-nJ9eDW0J2fJD-Sr6YtL3dgjua42IQx880X0OlZCjIiejhDlQdu_E","identifier":"84285c39-6a42-48e3-9b28-b3a7921abd69","customPayload":{"Interaction":1,"AddDefaultInteraction":false},"isAnonymous":true,"test":false,"purposes":[{"Id":"3BC029DF-C5C7-4EAD-A2F5-17CA8F0F7378","TransactionType":"NO_CHOICE"},{"Id":"8D5CA2B0-81BE-4441-B680-FD1723B366C1","TransactionType":"NOTGIVEN"},{"Id":"63A615E8-BC9C-4B1A-8130-AA94589F05A8","TransactionType":"NOTGIVEN"},{"Id":"8D001F26-A91B-45BB-8DCB-12DE1C0C5CF9","TransactionType":"NOTGIVEN"}],"dsDataElements":{}}',
)


r = requests.post(
    "https://api-js.datadome.co/js/",
    headers={
        **base_headers,
        "Host": "api-js.datadome.co",
        "Accept": "*/*",
        "Origin": "https://geo.captcha-delivery.com",
        "Referer": "https://geo.captcha-delivery.com/",
    },
    json="jsData=%7B%22ttst%22%3A73%2C%22ifov%22%3Afalse%2C%22wdifts%22%3Afalse%2C%22wdifrm%22%3Afalse%2C%22wdif%22%3Afalse%2C%22br_h%22%3A340%2C%22br_w%22%3A1440%2C%22br_oh%22%3A900%2C%22br_ow%22%3A1440%2C%22nddc%22%3A0%2C%22rs_h%22%3A900%2C%22rs_w%22%3A1440%2C%22rs_cd%22%3A24%2C%22phe%22%3Afalse%2C%22nm%22%3Afalse%2C%22jsf%22%3Afalse%2C%22ua%22%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10.15%3B+rv%3A88.0%29+Gecko%2F20100101+Firefox%2F88.0%22%2C%22lg%22%3A%22zh-CN%22%2C%22pr%22%3A2%2C%22hc%22%3A4%2C%22ars_h%22%3A900%2C%22ars_w%22%3A1440%2C%22tz%22%3A-120%2C%22str_ss%22%3Atrue%2C%22str_ls%22%3Atrue%2C%22str_idb%22%3Atrue%2C%22str_odb%22%3Afalse%2C%22plgod%22%3Afalse%2C%22plg%22%3A0%2C%22plgne%22%3A%22NA%22%2C%22plgre%22%3A%22NA%22%2C%22plgof%22%3A%22NA%22%2C%22plggt%22%3A%22NA%22%2C%22pltod%22%3Afalse%2C%22lb%22%3Afalse%2C%22eva%22%3A37%2C%22lo%22%3Afalse%2C%22ts_mtp%22%3A0%2C%22ts_tec%22%3Afalse%2C%22ts_tsa%22%3Afalse%2C%22vnd%22%3A%22%22%2C%22bid%22%3A%2220181001000000%22%2C%22mmt%22%3A%22empty%22%2C%22plu%22%3A%22empty%22%2C%22hdn%22%3Afalse%2C%22awe%22%3Afalse%2C%22geb%22%3Afalse%2C%22dat%22%3Afalse%2C%22med%22%3A%22defined%22%2C%22aco%22%3A%22probably%22%2C%22acots%22%3Afalse%2C%22acmp%22%3A%22maybe%22%2C%22acmpts%22%3Afalse%2C%22acw%22%3A%22probably%22%2C%22acwts%22%3Afalse%2C%22acma%22%3A%22maybe%22%2C%22acmats%22%3Afalse%2C%22acaa%22%3A%22maybe%22%2C%22acaats%22%3Afalse%2C%22ac3%22%3A%22%22%2C%22ac3ts%22%3Afalse%2C%22acf%22%3A%22maybe%22%2C%22acfts%22%3Afalse%2C%22acmp4%22%3A%22maybe%22%2C%22acmp4ts%22%3Atrue%2C%22acmp3%22%3A%22maybe%22%2C%22acmp3ts%22%3Afalse%2C%22acwm%22%3A%22maybe%22%2C%22acwmts%22%3Atrue%2C%22ocpt%22%3Afalse%2C%22vco%22%3A%22probably%22%2C%22vcots%22%3Afalse%2C%22vch%22%3A%22probably%22%2C%22vchts%22%3Atrue%2C%22vcw%22%3A%22probably%22%2C%22vcwts%22%3Atrue%2C%22vc3%22%3A%22%22%2C%22vc3ts%22%3Afalse%2C%22vcmp%22%3A%22%22%2C%22vcmpts%22%3Afalse%2C%22vcq%22%3A%22maybe%22%2C%22vcqts%22%3Afalse%2C%22vc1%22%3A%22probably%22%2C%22vc1ts%22%3Afalse%2C%22dvm%22%3A%22NA%22%2C%22sqt%22%3Afalse%2C%22so%22%3A%22landscape-primary%22%2C%22wbd%22%3Afalse%2C%22wbdm%22%3Atrue%2C%22wdw%22%3Atrue%2C%22ecpc%22%3Afalse%2C%22lgs%22%3Atrue%2C%22lgsod%22%3Afalse%2C%22bcda%22%3Afalse%2C%22idn%22%3Atrue%2C%22capi%22%3Afalse%2C%22svde%22%3Afalse%2C%22vpbq%22%3Atrue%2C%22xr%22%3Afalse%2C%22bgav%22%3Afalse%2C%22rri%22%3Atrue%2C%22idfr%22%3Afalse%2C%22ancs%22%3Atrue%2C%22inlc%22%3Atrue%2C%22cgca%22%3Afalse%2C%22inlf%22%3Atrue%2C%22tecd%22%3Afalse%2C%22sbct%22%3Atrue%2C%22aflt%22%3Atrue%2C%22rgp%22%3Atrue%2C%22bint%22%3Atrue%2C%22spwn%22%3Afalse%2C%22emt%22%3Afalse%2C%22bfr%22%3Afalse%2C%22dbov%22%3Afalse%2C%22glvd%22%3A%22ATI+Technologies+Inc.%22%2C%22glrd%22%3A%22AMD+Radeon+R9+M370X+OpenGL+Engine%22%2C%22tagpu%22%3A6%2C%22prm%22%3Atrue%2C%22tzp%22%3A%22Europe%2FParis%22%2C%22cvs%22%3Atrue%2C%22usb%22%3A%22NA%22%2C%22dcok%22%3A%22.captcha-delivery.com%22%2C%22mp_cx%22%3A700%2C%22mp_cy%22%3A183%2C%22mp_tr%22%3Atrue%2C%22mp_mx%22%3A-2%2C%22mp_my%22%3A-19%2C%22mp_sx%22%3A700%2C%22mp_sy%22%3A285%2C%22ewsi%22%3Afalse%2C%22tbce%22%3A72%7D&events=%5B%7B%22source%22%3A%7B%22x%22%3A669%2C%22y%22%3A278%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508622434%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A705%2C%22y%22%3A196%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508622626%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A0%2C%22y%22%3A1%7D%2C%22message%22%3A%22scroll%22%2C%22date%22%3A1620508622718%2C%22id%22%3A2%7D%2C%7B%22source%22%3A%7B%22x%22%3A0%2C%22y%22%3A58%7D%2C%22message%22%3A%22scroll%22%2C%22date%22%3A1620508622818%2C%22id%22%3A2%7D%2C%7B%22source%22%3A%7B%22x%22%3A705%2C%22y%22%3A196%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508623135%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A706%2C%22y%22%3A213%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508623252%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A0%2C%22y%22%3A59%7D%2C%22message%22%3A%22scroll%22%2C%22date%22%3A1620508623452%2C%22id%22%3A2%7D%2C%7B%22source%22%3A%7B%22x%22%3A0%2C%22y%22%3A66%7D%2C%22message%22%3A%22scroll%22%2C%22date%22%3A1620508623552%2C%22id%22%3A2%7D%2C%7B%22source%22%3A%7B%22x%22%3A704%2C%22y%22%3A231%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508623720%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A701%2C%22y%22%3A158%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508623835%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A708%2C%22y%22%3A135%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508623935%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A710%2C%22y%22%3A130%7D%2C%22message%22%3A%22mouse+click%22%2C%22date%22%3A1620508624088%2C%22id%22%3A1%7D%2C%7B%22source%22%3A%7B%22x%22%3A710%2C%22y%22%3A130%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508624451%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A631%2C%22y%22%3A137%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508624552%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A621%2C%22y%22%3A139%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508624653%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A622%2C%22y%22%3A141%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508624769%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A624%2C%22y%22%3A144%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508625119%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A613%2C%22y%22%3A159%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508625219%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A610%2C%22y%22%3A160%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508625319%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A608%2C%22y%22%3A159%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508625434%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A607%2C%22y%22%3A159%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508625585%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A608%2C%22y%22%3A161%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508625885%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A641%2C%22y%22%3A185%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508625986%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A646%2C%22y%22%3A189%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508626101%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A650%2C%22y%22%3A191%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508626201%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A715%2C%22y%22%3A192%7D%2C%22message%22%3A%22mouse+click%22%2C%22date%22%3A1620508627165%2C%22id%22%3A1%7D%2C%7B%22source%22%3A%7B%22x%22%3A699%2C%22y%22%3A232%7D%2C%22message%22%3A%22mouse+move%22%2C%22date%22%3A1620508627353%2C%22id%22%3A0%7D%5D&eventCounters=%7B%22mouse+move%22%3A21%2C%22mouse+click%22%3A2%2C%22scroll%22%3A4%2C%22touch+start%22%3A0%2C%22touch+end%22%3A0%2C%22touch+move%22%3A0%2C%22key+press%22%3A0%2C%22key+down%22%3A0%2C%22key+up%22%3A0%7D&jsType=le&cid=null&ddk=2211F522B61E269B869FA6EAFFB5E1&Referer=https%253A%252F%252Fgeo.captcha-delivery.com%252Fcaptcha%252F%253FinitialCid%253DAHrlqAAAAAMAxO4p3ztuw6sA2Nq-Ng%253D%253D%2526cid%253DYv-A0py-MiofcZ5FJzDnKDZ.Kut9RjTOxea.%7EB%7E9qM711tSD%7EgC%7EaQKrtfBwkTzM_KEJi59dT21NXpf71VnK0lblkWvHJStHYcjhtkKcw3%2526referer%253Dhttp%25253A%25252F%25252Fbck.hermes.com%25252Fcategories%25253Flocale%25253Dfr_fr%2526hash%253D2211F522B61E269B869FA6EAFFB5E1%2526t%253Dfe%2526s%253D8945%2526cid%253DYv-A0py-MiofcZ5FJzDnKDZ.Kut9RjTOxea.%7EB%7E9qM711tSD%7EgC%7EaQKrtfBwkTzM_KEJi59dT21NXpf71VnK0lblkWvHJStHYcjhtkKcw3&request=%252Fcaptcha%252F%253FinitialCid%253DAHrlqAAAAAMAxO4p3ztuw6sA2Nq-Ng%253D%253D%2526cid%253DYv-A0py-MiofcZ5FJzDnKDZ.Kut9RjTOxea.%7EB%7E9qM711tSD%7EgC%7EaQKrtfBwkTzM_KEJi59dT21NXpf71VnK0lblkWvHJStHYcjhtkKcw3%2526referer%253Dhttp%25253A%25252F%25252Fbck.hermes.com%25252Fcategories%25253Flocale%25253Dfr_fr%2526hash%253D2211F522B61E269B869FA6EAFFB5E1%2526t%253Dfe%2526s%253D8945%2526cid%253DYv-A0py-MiofcZ5FJzDnKDZ.Kut9RjTOxea.%7EB%7E9qM711tSD%7EgC%7EaQKrtfBwkTzM_KEJi59dT21NXpf71VnK0lblkWvHJStHYcjhtkKcw3&responsePage=captcha&ddv=4.1.48",
)


r = requests.get(
    "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://www.hermes.com/fr/fr/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "Upgrade-Insecure-Requests": "1",
        "If-None-Match": 'W/"4793f-QKY3CnJ2Ys6WGJX69JNoxbX27C0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.googletagmanager.com/a?id=GTM-W39B2P&cv=847&v=3&t=t&pid=1590290177&rv=4s0&es=1&e=*&eid=367&u=C&tc=168&tr=1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1html.5html.5tg.5tg.5tg.5tg.5tg.5tg.5tg.5tg.5tg.5tg.5tg.5tg.5tg.5tg&ti=1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1html.1html.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg.1tg&z=0",
    headers={
        **base_headers,
        "Host": "www.googletagmanager.com",
        "Accept": "image/webp,*/*",
        "Referer": "https://www.hermes.com/",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"d9f-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/polyfills-es2015.2b516c6d2858f0db3ab0.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"1f08c-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"2eb474-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.googletagmanager.com/gtm.js?id=GTM-W39B2P",
    headers={
        **base_headers,
        "Host": "www.googletagmanager.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://js.datadome.co/tags.js",
    headers={
        **base_headers,
        "Host": "js.datadome.co",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/",
        "If-Modified-Since": "Wed, 05 May 2021 08:48:22 GMT",
        "If-None-Match": '"37ee2-5c19141d47a87-gzip"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.post(
    "https://bam.nr-data.net/events/1/5ca1a0d07f?a=274419876&sa=1&v=1198.fe6ec20&t=Unnamed%20Transaction&rst=12152&ck=1&ref=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
    headers={
        **base_headers,
        "Host": "bam.nr-data.net",
        "Accept": "*/*",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
    },
    json="bel.6;e,'unload,9dj,",
)


r = requests.post(
    "https://bam.nr-data.net/jserrors/1/5ca1a0d07f?a=274419876&sa=1&v=1198.fe6ec20&t=Unnamed%20Transaction&rst=12153&ck=1&ref=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
    headers={
        **base_headers,
        "Host": "bam.nr-data.net",
        "Accept": "*/*",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
    },
    json='{"ierr":[{"params":{"stackHash":389037123,"exceptionClass":"TypeError","request_uri":"/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/","message":"can\'t convert null to object","stack_trace":"r@<inline>:35:24231\\n__nr_require<[6]</<@<inline>:35:5719\\nn@<inline>:35:23396\\nu@<inline>:35:22628\\nZ/<@https://www.hermes.com/fr/fr/polyfills-es2015.2b516c6d2858f0db3ab0.js:1:108381\\nf/<@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:2557646\\nf@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:2557752\\nu47x@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:2962663\\nd@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:552\\niTwO@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:2248349\\nd@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:552\\n0@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:66207\\nd@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:552\\na@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:421\\nc@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:293\\n@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:47","releaseIds":"{}","pageview":1,"browserInteractionId":"1ecab917-ac10-4823-a1fa-638d9daa9fb4"},"custom":{},"metrics":{"count":1,"time":{"t":1195}}}],"xhr":[{"params":{"method":"GET","host":"cdn-ukwest.onetrust.com:443","pathname":"/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/870afb0c-7f7a-4f57-a8d9-a461bd01c779.json","status":200},"metrics":{"count":1,"rxSize":{"t":2646},"duration":{"t":355},"cbTime":{"t":4},"time":{"t":1236}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/categories","status":403},"metrics":{"count":1,"rxSize":{"t":320},"duration":{"t":663},"cbTime":{"t":23},"time":{"t":1585}}},{"params":{"method":"POST","host":"api-js.datadome.co:443","pathname":"/js/","status":200},"metrics":{"count":1,"txSize":{"t":3356},"rxSize":{"t":209},"duration":{"t":998},"cbTime":{"t":0},"time":{"t":1504}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/feature-flag","status":403},"metrics":{"count":1,"rxSize":{"t":1441},"duration":{"t":1821},"cbTime":{"t":1},"time":{"t":1285}}},{"params":{"method":"POST","host":"bam.nr-data.net:443","pathname":"/events/1/5ca1a0d07f","status":200},"metrics":{"count":1,"txSize":{"t":689},"rxSize":{"t":24},"duration":{"t":245},"cbTime":{"t":0},"time":{"t":4460}}}]}',
)


r = requests.options(
    "https://bck.hermes.com/feature-flag?locale=fr_fr&features=open_product_locator_tray_using_angular&features=apple_watch_animations&features=product_page_sticky&features=grid_page_sticky&features=grid_alternative_views&features=grid_filters_mobile&features=grid_display_mode_mobile&features=beltkits_personalization&features=smallleathergoods_personalization&features=silk_personalization&features=silk_personalization_v2&features=dac_checkout_new_flat&features=product_locator_display_map&features=address_verification&features=ereservation_light_account_captcha&features=angular_spa_links_activation_on_menu&features=angular_spa_activation_on_product_page_back_cta&features=adyen_latest_sdk&features=adyen_oneclick&features=order_confirmation_angular&values=false&values=true&values=false&values=true&values=false&values=false&values=false&values=false&values=false&values=false&values=false&values=false&values=false&values=false&values=true&values=false&values=false&values=false&values=false&values=false",
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "*/*",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "content-type",
        "Referer": "https://www.hermes.com/",
        "Origin": "https://www.hermes.com",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/1-es2015.e43c0db3b010d43a145c.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"38c1-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/4-es2015.54d03ccb1e9d100c166d.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"23dd-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/5-es2015.be56b5b23c0c2a9d1642.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"fa96-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/6-es2015.400b947a332449e5a9d9.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"41c3-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/common-es2015.23da0adef1d2edc22748.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"6ba7-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/13-es2015.cc38b6759b8f0136c4e9.js",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:09+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A09+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"32bc4-7438674ba0"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
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
    json="jsData=%7B%22ttst%22%3A49%2C%22ifov%22%3Afalse%2C%22wdifts%22%3Afalse%2C%22wdifrm%22%3Afalse%2C%22wdif%22%3Afalse%2C%22br_h%22%3A340%2C%22br_w%22%3A1440%2C%22br_oh%22%3A900%2C%22br_ow%22%3A1440%2C%22nddc%22%3A1%2C%22rs_h%22%3A900%2C%22rs_w%22%3A1440%2C%22rs_cd%22%3A24%2C%22phe%22%3Afalse%2C%22nm%22%3Afalse%2C%22jsf%22%3Afalse%2C%22ua%22%3A%22Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A88.0)%20Gecko%2F20100101%20Firefox%2F88.0%22%2C%22lg%22%3A%22zh-CN%22%2C%22pr%22%3A2%2C%22hc%22%3A4%2C%22ars_h%22%3A900%2C%22ars_w%22%3A1440%2C%22tz%22%3A-120%2C%22str_ss%22%3Atrue%2C%22str_ls%22%3Atrue%2C%22str_idb%22%3Atrue%2C%22str_odb%22%3Afalse%2C%22plgod%22%3Afalse%2C%22plg%22%3A0%2C%22plgne%22%3A%22NA%22%2C%22plgre%22%3A%22NA%22%2C%22plgof%22%3A%22NA%22%2C%22plggt%22%3A%22NA%22%2C%22pltod%22%3Afalse%2C%22lb%22%3Afalse%2C%22eva%22%3A37%2C%22lo%22%3Afalse%2C%22ts_mtp%22%3A0%2C%22ts_tec%22%3Afalse%2C%22ts_tsa%22%3Afalse%2C%22vnd%22%3A%22%22%2C%22bid%22%3A%2220181001000000%22%2C%22mmt%22%3A%22empty%22%2C%22plu%22%3A%22empty%22%2C%22hdn%22%3Afalse%2C%22awe%22%3Afalse%2C%22geb%22%3Afalse%2C%22dat%22%3Afalse%2C%22med%22%3A%22defined%22%2C%22aco%22%3A%22probably%22%2C%22acots%22%3Afalse%2C%22acmp%22%3A%22maybe%22%2C%22acmpts%22%3Afalse%2C%22acw%22%3A%22probably%22%2C%22acwts%22%3Afalse%2C%22acma%22%3A%22maybe%22%2C%22acmats%22%3Afalse%2C%22acaa%22%3A%22maybe%22%2C%22acaats%22%3Afalse%2C%22ac3%22%3A%22%22%2C%22ac3ts%22%3Afalse%2C%22acf%22%3A%22maybe%22%2C%22acfts%22%3Afalse%2C%22acmp4%22%3A%22maybe%22%2C%22acmp4ts%22%3Atrue%2C%22acmp3%22%3A%22maybe%22%2C%22acmp3ts%22%3Afalse%2C%22acwm%22%3A%22maybe%22%2C%22acwmts%22%3Atrue%2C%22ocpt%22%3Afalse%2C%22vco%22%3A%22probably%22%2C%22vcots%22%3Afalse%2C%22vch%22%3A%22probably%22%2C%22vchts%22%3Atrue%2C%22vcw%22%3A%22probably%22%2C%22vcwts%22%3Atrue%2C%22vc3%22%3A%22%22%2C%22vc3ts%22%3Afalse%2C%22vcmp%22%3A%22%22%2C%22vcmpts%22%3Afalse%2C%22vcq%22%3A%22maybe%22%2C%22vcqts%22%3Afalse%2C%22vc1%22%3A%22probably%22%2C%22vc1ts%22%3Afalse%2C%22dvm%22%3A%22NA%22%2C%22sqt%22%3Afalse%2C%22so%22%3A%22landscape-primary%22%2C%22wbd%22%3Afalse%2C%22wbdm%22%3Atrue%2C%22wdw%22%3Atrue%2C%22ecpc%22%3Afalse%2C%22lgs%22%3Atrue%2C%22lgsod%22%3Afalse%2C%22bcda%22%3Afalse%2C%22idn%22%3Atrue%2C%22capi%22%3Afalse%2C%22svde%22%3Afalse%2C%22vpbq%22%3Atrue%2C%22xr%22%3Afalse%2C%22bgav%22%3Afalse%2C%22rri%22%3Atrue%2C%22idfr%22%3Afalse%2C%22ancs%22%3Atrue%2C%22inlc%22%3Atrue%2C%22cgca%22%3Afalse%2C%22inlf%22%3Atrue%2C%22tecd%22%3Afalse%2C%22sbct%22%3Atrue%2C%22aflt%22%3Atrue%2C%22rgp%22%3Atrue%2C%22bint%22%3Atrue%2C%22spwn%22%3Afalse%2C%22emt%22%3Afalse%2C%22bfr%22%3Afalse%2C%22dbov%22%3Afalse%2C%22glvd%22%3A%22ATI%20Technologies%20Inc.%22%2C%22glrd%22%3A%22AMD%20Radeon%20R9%20M370X%20OpenGL%20Engine%22%2C%22tagpu%22%3A6%2C%22prm%22%3Atrue%2C%22tzp%22%3A%22Europe%2FParis%22%2C%22cvs%22%3Atrue%2C%22usb%22%3A%22NA%22%7D&events=%5B%5D&eventCounters=%5B%5D&jsType=ch&cid=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN&ddk=2211F522B61E269B869FA6EAFFB5E1&Referer=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F&request=%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F&responsePage=origin&ddv=4.1.48",
)


r = requests.get(
    "https://cdn-ukwest.onetrust.com/scripttemplates/otSDKStub.js",
    headers={
        **base_headers,
        "Host": "cdn-ukwest.onetrust.com",
        "Accept": "*/*",
        "Referer": "https://www.hermes.com/",
        "If-Modified-Since": "Tue, 27 Apr 2021 21:19:23 GMT",
        "If-None-Match": "0x8D909C220F323C7",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://bck.hermes.com/categories?locale=fr_fr",
    cookies={
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.hermes.com",
        "Referer": "https://www.hermes.com/",
        "Cookie": "datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


# These variables probably come from the result of the request above
Origin_1 = "https://www.hermes.com"
Referer_1 = "https://www.hermes.com/"


r = requests.get(
    "https://cdn-ukwest.onetrust.com/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/870afb0c-7f7a-4f57-a8d9-a461bd01c779.json",
    headers={
        **base_headers,
        "Host": "cdn-ukwest.onetrust.com",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "If-Modified-Since": "Mon, 03 May 2021 12:35:52 GMT",
        "If-None-Match": "0x8D90E2FFCFA9FEA",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


# These variables probably come from the result of the request above
Host_1 = "cdn-ukwest.onetrust.com"


r = requests.get(
    "https://bck.hermes.com/feature-flag?locale=fr_fr&features=open_product_locator_tray_using_angular&features=apple_watch_animations&features=product_page_sticky&features=grid_page_sticky&features=grid_alternative_views&features=grid_filters_mobile&features=grid_display_mode_mobile&features=beltkits_personalization&features=smallleathergoods_personalization&features=silk_personalization&features=silk_personalization_v2&features=dac_checkout_new_flat&features=product_locator_display_map&features=address_verification&features=ereservation_light_account_captcha&features=angular_spa_links_activation_on_menu&features=angular_spa_activation_on_product_page_back_cta&features=adyen_latest_sdk&features=adyen_oneclick&features=order_confirmation_angular&values=false&values=true&values=false&values=true&values=false&values=false&values=false&values=false&values=false&values=false&values=false&values=false&values=false&values=false&values=true&values=false&values=false&values=false&values=false&values=false",
    cookies={
        "datadome": "Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=Yv-A0py-MiofcZ5FJzDnK4Y3VPC5Tpl0EYtaE~M1DTg.Yo6GHYYEjCU6VW1~UAvXnVNp_g.2r2O2RUGuq.81lwaLxaL85Kf_1G1fS_VmCN; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.options(
    "https://bck.hermes.com/customer-session?locale=fr_fr",
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "*/*",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "cache-control",
        "Referer": Referer_1,
        "Origin": Origin_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://cdn-ukwest.onetrust.com/scripttemplates/6.17.0/otBannerSdk.js",
    headers={**base_headers, "Host": Host_1, "Accept": "*/*", "Referer": Referer_1},
)


r = requests.get(
    "https://cdn-ukwest.onetrust.com/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/a7ef0083-2008-4b25-9b1b-24fd6359406e/fr.json",
    headers={
        **base_headers,
        "Host": Host_1,
        "Accept": "*/*",
        "Referer": Referer_1,
        "Origin": Origin_1,
    },
)


r = requests.get(
    "https://cdn-ukwest.onetrust.com/scripttemplates/6.17.0/assets/otCenterRounded.json",
    headers={
        **base_headers,
        "Host": Host_1,
        "Accept": "*/*",
        "Referer": Referer_1,
        "Origin": Origin_1,
    },
)


r = requests.get(
    "https://cdn-ukwest.onetrust.com/scripttemplates/6.17.0/assets/otPcCenter.json",
    headers={
        **base_headers,
        "Host": Host_1,
        "Accept": "*/*",
        "Referer": Referer_1,
        "Origin": Origin_1,
    },
)


r = requests.get(
    "https://bck.hermes.com/customer-session?locale=fr_fr",
    cookies={
        "datadome": "_FrTpq4gVbnlkxduoSa_VOFotz62G.YCB9ZWG6yLQzk8lsy0bxKzX8w0s2pemjgSOtg1nvpwJA.i9rIhdjqTChzUAOKHfpRGHVAafetQDM",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Cache-Control": "max-age=0",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=_FrTpq4gVbnlkxduoSa_VOFotz62G.YCB9ZWG6yLQzk8lsy0bxKzX8w0s2pemjgSOtg1nvpwJA.i9rIhdjqTChzUAOKHfpRGHVAafetQDM; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://js-agent.newrelic.com/nr-spa-1198.min.js",
    headers={
        **base_headers,
        "Host": "js-agent.newrelic.com",
        "Accept": "*/*",
        "Referer": Referer_1,
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/assets/images/favicon/apple-touch-icon-144x144.png",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:11+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "_FrTpq4gVbnlkxduoSa_VOFotz62G.YCB9ZWG6yLQzk8lsy0bxKzX8w0s2pemjgSOtg1nvpwJA.i9rIhdjqTChzUAOKHfpRGHVAafetQDM",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "image/webp,*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A11+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=_FrTpq4gVbnlkxduoSa_VOFotz62G.YCB9ZWG6yLQzk8lsy0bxKzX8w0s2pemjgSOtg1nvpwJA.i9rIhdjqTChzUAOKHfpRGHVAafetQDM; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/assets/images/favicon/favicon-48x48.png",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:11+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "_FrTpq4gVbnlkxduoSa_VOFotz62G.YCB9ZWG6yLQzk8lsy0bxKzX8w0s2pemjgSOtg1nvpwJA.i9rIhdjqTChzUAOKHfpRGHVAafetQDM",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "image/webp,*/*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A11+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=_FrTpq4gVbnlkxduoSa_VOFotz62G.YCB9ZWG6yLQzk8lsy0bxKzX8w0s2pemjgSOtg1nvpwJA.i9rIhdjqTChzUAOKHfpRGHVAafetQDM; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0",
    },
)


r = requests.get(
    "https://bam.nr-data.net/1/5ca1a0d07f?a=274419876&sa=1&v=1198.fe6ec20&t=Unnamed%20Transaction&rst=2051&ck=1&ref=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&be=260&fe=1279&dc=893&af=err,xhr,stn,ins,spa&perf=%7B%22timing%22:%7B%22of%22:1620508629669,%22n%22:0,%22u%22:224,%22ue%22:228,%22f%22:14,%22dn%22:14,%22dne%22:14,%22c%22:14,%22s%22:14,%22ce%22:14,%22rq%22:71,%22rp%22:219,%22rpe%22:219,%22dl%22:224,%22di%22:297,%22ds%22:887,%22de%22:960,%22dc%22:1278,%22l%22:1278,%22le%22:1279%7D,%22navigation%22:%7B%22ty%22:1%7D%7D&fcp=332&jsonp=NREUM.setToken",
    headers={
        **base_headers,
        "Host": "bam.nr-data.net",
        "Accept": "*/*",
        "Referer": Referer_1,
    },
)


r = requests.get(
    "https://bck.hermes.com/products?locale=fr_fr&category=WOMENBAGSBAGSCLUTCHES&sort=relevance",
    cookies={
        "datadome": "m1SaEbBfZhBPckwABzm9AZ1AgIfIK8AViGeBk.EGRenRgomnE_v9huxYDBsob1gwGXVKm_.UwULRcq07xNHA.Qc1fWrT9~QduskxF2dsu",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=m1SaEbBfZhBPckwABzm9AZ1AgIfIK8AViGeBk.EGRenRgomnE_v9huxYDBsob1gwGXVKm_.UwULRcq07xNHA.Qc1fWrT9~QduskxF2dsu; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://bck.hermes.com/editorial?locale=fr_fr&storyids=%5B282893,281135%5D",
    cookies={
        "datadome": "PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.hermes.com/fr/fr/assets/i18n/fr-FR.json",
    cookies={
        "OptanonConsent": "isIABGlobal=false&datestamp=Sat+May+08+2021+23:17:11+GMT+0200+(ä¸\xadæ¬§å¤\x8fä»¤æ\x97¶é\x97´)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/&groups=C0001:1,C0002:0,C0003:0,C0004:0",
        "datadome": "PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": "www.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
        "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Sat+May+08+2021+23%3A17%3A11+GMT%2B0200+(%E4%B8%AD%E6%AC%A7%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&consentId=84285c39-6a42-48e3-9b28-b3a7921abd69&interactionCount=1&landingPath=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; datadome=PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "If-Modified-Since": "Sat, 26 Oct 1985 08:15:00 GMT",
        "If-None-Match": 'W/"27b9-7438674ba0"',
        "TE": "Trailers",
    },
)


# These variables probably come from the result of the request above
Host_2 = "assets.hermes.com"


r = requests.get(
    "https://bck.hermes.com/editorial/banners?locale=fr_fr",
    cookies={
        "datadome": "PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://bck.hermes.com/footer-items?locale=fr_fr",
    cookies={
        "datadome": "PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
    },
)


# These variables probably come from the result of the request above
Host_3 = "assets.hermes.com"


r = requests.get(
    "https://bck.hermes.com/category/WOMENBAGSBAGSCLUTCHES?locale=fr_fr",
    cookies={
        "datadome": "PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://bck.hermes.com/category/WOMENBAGSBAGSCLUTCHES?locale=fr_fr",
    cookies={
        "datadome": "PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/content/hermesedito//Loader/loader-4.gif",
    cookies={
        "datadome": "PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=PwEwO9N36j1o3FhVcy8~gNCf7L2fiG2VgoEVlB~tOnxnP5mg93oL6UlBwzkasJ1G20BENOqd.8d1kcSChG_g_R0KSa4Bm8sh15aFR~jALl; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "If-Modified-Since": "Wed, 30 Oct 2019 04:48:58 GMT",
        "Cache-Control": "max-age=0",
    },
)


r = requests.get(
    "https://bck.hermes.com/category/WOMENBAGSBAGSCLUTCHES?locale=fr_fr",
    cookies={
        "datadome": "AQwU7t2-C6vBx-6sdoNuu6khkaomaC8SZqUmu1J4YYOrB.WdazuYS-0dy6KzHTZWtGyY-ORKDlVahij4_ZnHKTJLbOOn6CVFP50rBZ-KaA",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": "bck.hermes.com",
        "Accept": "application/json, text/plain, */*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "Cookie": "datadome=AQwU7t2-C6vBx-6sdoNuu6khkaomaC8SZqUmu1J4YYOrB.WdazuYS-0dy6KzHTZWtGyY-ORKDlVahij4_ZnHKTJLbOOn6CVFP50rBZ-KaA; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073540CTAA_front_1?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&wid=300&hei=300",
    cookies={
        "datadome": "AQwU7t2-C6vBx-6sdoNuu6khkaomaC8SZqUmu1J4YYOrB.WdazuYS-0dy6KzHTZWtGyY-ORKDlVahij4_ZnHKTJLbOOn6CVFP50rBZ-KaA",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=AQwU7t2-C6vBx-6sdoNuu6khkaomaC8SZqUmu1J4YYOrB.WdazuYS-0dy6KzHTZWtGyY-ORKDlVahij4_ZnHKTJLbOOn6CVFP50rBZ-KaA; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073419CKM3_front_1?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&wid=300&hei=300",
    cookies={
        "datadome": "AQwU7t2-C6vBx-6sdoNuu6khkaomaC8SZqUmu1J4YYOrB.WdazuYS-0dy6KzHTZWtGyY-ORKDlVahij4_ZnHKTJLbOOn6CVFP50rBZ-KaA",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=AQwU7t2-C6vBx-6sdoNuu6khkaomaC8SZqUmu1J4YYOrB.WdazuYS-0dy6KzHTZWtGyY-ORKDlVahij4_ZnHKTJLbOOn6CVFP50rBZ-KaA; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/076143CKM3_front_1?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&wid=300&hei=300",
    cookies={
        "datadome": "AQwU7t2-C6vBx-6sdoNuu6khkaomaC8SZqUmu1J4YYOrB.WdazuYS-0dy6KzHTZWtGyY-ORKDlVahij4_ZnHKTJLbOOn6CVFP50rBZ-KaA",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=AQwU7t2-C6vBx-6sdoNuu6khkaomaC8SZqUmu1J4YYOrB.WdazuYS-0dy6KzHTZWtGyY-ORKDlVahij4_ZnHKTJLbOOn6CVFP50rBZ-KaA; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3",
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.options(
    "https://privacyportal-uk.onetrust.com/request/v1/consentreceipts",
    headers={
        **base_headers,
        "Host": "privacyportal-uk.onetrust.com",
        "Accept": "*/*",
        "Access-Control-Request-Method": "POST",
        "Access-Control-Request-Headers": "content-type",
        "Referer": Referer_1,
        "Origin": Origin_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://2292824.fls.doubleclick.net/activityi;src=2292824;type=hermes;cat=rubrique;ord=1691937381844;gtm=2wg4s0;auiddc=324567000.1620508634;u13=undefined;~oref=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F?",
    headers={
        **base_headers,
        "Host": "2292824.fls.doubleclick.net",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": Referer_1,
        "Upgrade-Insecure-Requests": "1",
    },
)


r = requests.get(
    "https://www.googletagmanager.com/gtag/js?id=G-Y862HCHCQ7&l=dataLayer&cx=c",
    headers={
        **base_headers,
        "Host": "www.googletagmanager.com",
        "Accept": "*/*",
        "Referer": Referer_1,
    },
)


r = requests.get(
    "https://2292824.fls.doubleclick.net/activityi;src=2292824;type=hermes;cat=rubrique;ord=6633002248200;gtm=2wg4s0;auiddc=324567000.1620508634;u13=undefined;~oref=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F?",
    headers={
        **base_headers,
        "Host": "2292824.fls.doubleclick.net",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": Referer_1,
        "Upgrade-Insecure-Requests": "1",
    },
)


r = requests.get(
    "https://try.abtasty.com/2ba80386b56e4a2e33307bf9a949fb88.js",
    headers={
        **base_headers,
        "Host": "try.abtasty.com",
        "Accept": "*/*",
        "Referer": Referer_1,
        "If-Modified-Since": "Thu, 06 May 2021 08:34:19 GMT",
        "If-None-Match": 'W/"6f29b053d059e76c88ac7052af488140"',
    },
)


r = requests.get(
    "https://t.contentsquare.net/uxa/4c542426f49a4.js",
    headers={
        **base_headers,
        "Host": "t.contentsquare.net",
        "Accept": "*/*",
        "Referer": Referer_1,
        "If-Modified-Since": "Tue, 04 May 2021 15:17:17 GMT",
        "If-None-Match": '"693e86bb020504686b9d1ed9ced41227"',
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073419CKM3_worn_6?a=a&size=3000,3000&extend=0,0,0,0&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "WGSaPbsSLyMj7w6N8.MzRqd-yaGp0VJoGOGI76J6QfoGIt~SAexmKhvT6hfDs2Mkv9SpQGY_~c_h6awWhHdheZCq.1xBFfTc4kqBQhB2t_",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=WGSaPbsSLyMj7w6N8.MzRqd-yaGp0VJoGOGI76J6QfoGIt~SAexmKhvT6hfDs2Mkv9SpQGY_~c_h6awWhHdheZCq.1xBFfTc4kqBQhB2t_; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146",
        "If-Modified-Since": "Tue, 29 Oct 2019 22:00:57 GMT",
        "If-None-Match": '"616b1b22b49f11650f09ed50fa497184"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073419CKM3_front_1?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "WGSaPbsSLyMj7w6N8.MzRqd-yaGp0VJoGOGI76J6QfoGIt~SAexmKhvT6hfDs2Mkv9SpQGY_~c_h6awWhHdheZCq.1xBFfTc4kqBQhB2t_",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=WGSaPbsSLyMj7w6N8.MzRqd-yaGp0VJoGOGI76J6QfoGIt~SAexmKhvT6hfDs2Mkv9SpQGY_~c_h6awWhHdheZCq.1xBFfTc4kqBQhB2t_; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146",
        "If-Modified-Since": "Tue, 29 Oct 2019 22:00:57 GMT",
        "If-None-Match": '"8b188f87cb00ff722820a06fbdc27d25"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073419CKM3_side_2?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "WGSaPbsSLyMj7w6N8.MzRqd-yaGp0VJoGOGI76J6QfoGIt~SAexmKhvT6hfDs2Mkv9SpQGY_~c_h6awWhHdheZCq.1xBFfTc4kqBQhB2t_",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508617.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=WGSaPbsSLyMj7w6N8.MzRqd-yaGp0VJoGOGI76J6QfoGIt~SAexmKhvT6hfDs2Mkv9SpQGY_~c_h6awWhHdheZCq.1xBFfTc4kqBQhB2t_; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508617.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146",
        "If-Modified-Since": "Tue, 29 Oct 2019 22:00:57 GMT",
        "If-None-Match": '"926e987f48123874f284c8ea473cdfec"',
        "Cache-Control": "max-age=0",
        "TE": "Trailers",
    },
)


r = requests.post(
    "https://privacyportal-uk.onetrust.com/request/v1/consentreceipts",
    headers={
        **base_headers,
        "Host": "privacyportal-uk.onetrust.com",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "TE": "Trailers",
    },
    json='{"requestInformation":"eyJhbGciOiJSUzUxMiJ9.eyJvdEp3dFZlcnNpb24iOjEsInByb2Nlc3NJZCI6ImZlOGU1MjYxLTYzMTEtNDZkMS1hMTUwLWEyMWJkNDA0Y2RkMCIsInByb2Nlc3NWZXJzaW9uIjo1MSwiaWF0IjoiMjAyMC0xMC0wNVQxMjoxMToyNi4yMDciLCJtb2MiOiJDT09LSUUiLCJzdWIiOiJDb29raWUgVW5pcXVlIElkIiwiaXNzIjpudWxsLCJ0ZW5hbnRJZCI6IjliYzc2ZTM5LWEzNTAtNDk1YS1iMTc1LTk4OTVjZWU3NzMxNyIsImRlc2NyaXB0aW9uIjoiVGhpcyBjb2xsZWN0aW9uIHBvaW50IGNhcHR1cmVzIHRoZSBjdXJyZW50IHNpdGUgdmlzaXRvciBjb25zZW50IHByZWZlcmVuY2VzIGZvciB0aGUgZG9tYWluOiBoZXJtZXMuY29tL2ZyL2ZyLy1lbiBzcGVjaWZpZWQuIiwiY29uc2VudFR5cGUiOiJDT09LSUVCQU5ORVIiLCJkb3VibGVPcHRJbiI6ZmFsc2UsInJlY29uZmlybUFjdGl2ZVB1cnBvc2UiOmZhbHNlLCJkeW5hbWljQ29sbGVjdGlvblBvaW50IjpmYWxzZSwiYXV0aGVudGljYXRpb25SZXF1aXJlZCI6ZmFsc2UsInBvbGljeV91cmkiOiJoZXJtZXMuY29tL2ZyL2ZyLyIsImFsbG93Tm90R2l2ZW5Db25zZW50cyI6ZmFsc2UsInB1cnBvc2VzIjpbeyJpZCI6IjliNDg5ZWMzLWI4OTUtNDFlZi1iNmNmLWI2ZDA4ZjI2NDU4YiIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjkwZWQ0NmZlLTA2YzAtNDViOS1hZTUzLTJjYTc4OWU3ZDNiZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjU5Y2E2MTYyLTI5NTEtNDBmZC05NGU5LWIwNTA2YzExZDVmZCIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjA4ZTFlNWY0LWVkZmQtNDU2MS1hNmNlLTM5OGNkMGEyZGYyZiIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImRiYjJjMjQ1LTE1MTAtNDlmMi1iOTdjLTliNjM0Y2E0YTFjMyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjgxY2FjZWNiLTZlYTMtNGYzZC04YTkwLTc4NDY4Yzg4YmIxOCIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjY3YTFmNGQyLWRiM2QtNGQ1YS1hZDQ3LTFmZDYzN2ZmYjkwNiIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImE4YTlmNDliLTNjMTAtNDAzNy04NjMxLWY5NzZhMGI0OWNiNSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImI0M2Q1YTBiLTBlODMtNDlmMi1hZjIyLWI2ZGU5ZTZjOWU5OCIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjhkNWNhMmIwLTgxYmUtNDQ0MS1iNjgwLWZkMTcyM2IzNjZjMSIsInZlcnNpb24iOjIsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjhkMDAxZjI2LWE5MWItNDViYi04ZGNiLTEyZGUxYzBjNWNmOSIsInZlcnNpb24iOjIsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjUwYzUzYjZlLThiMjktNDdlZC04OTNiLWY2MWY0ODdmM2VhZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjNiYzAyOWRmLWM1YzctNGVhZC1hMmY1LTE3Y2E4ZjBmNzM3OCIsInZlcnNpb24iOjIsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjFmOTU3NzhlLTU3NGUtNDgwMS1hMTBhLTFlZjYxNjI5ZTMxZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImE5N2U2MGIxLTFjMTYtNGRkMC04ZjYxLTFmZWUxY2Y3YzdjYSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImMxYzRjMWQ5LWVmODQtNGRmMS1hODE5LWFjMzcyZDU1MWY2MCIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjNkYTYyOTUxLTk3MDEtNGNjYS05ZGViLTZjYzMxYzM1MDlhZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjM4ZDI5YmE2LWNiMjItNDA0Ny05MDdlLTFhOGNmNmIxZDIwMiIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjkwOTA4MDdkLTQ1ODktNDNhNS04MDE1LWM5Mzc1NWQ0OGJhMSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjEwNGRkM2RjLTI2YzktNDhmMy1iNDNhLTJkYzBmNDE2ZTBkNSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6Ijk1YzViZjVlLWQxNzctNDM0NC1iZmI5LTRlYWQxZTk0NGQ2MyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImNiYmU2ZGVjLWJkNWItNDVjNi1hNjYyLTUwNjFhMjZlZTAzZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6Ijg0MDI4ZTA1LTY3MGQtNGIyNy04YWM0LWQyYzAxYjY0Mzg1MyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjZlNWQwODliLTk3MjUtNDQ5ZC1iNWJlLTNlMWQ1YTYxMjIzNyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjYzYTYxNWU4LWJjOWMtNGIxYS04MTMwLWFhOTQ1ODlmMDVhOCIsInZlcnNpb24iOjIsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImM5ODVjOGFhLWNmMGYtNDI4ZS1hZDk5LWYwYzQyMGM5ZGIyNyIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6ImQ0OGZiNzAzLWQzYjAtNDE3ZS04NTc4LTgzN2FjN2M0NjkzNSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6Ijk1Nzg3NmNlLTU3ODgtNDQxMi1iN2RiLTM5OGU5YjIzM2RlNSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX0seyJpZCI6IjIyMTBiMTM3LTBjMDMtNDhmNC04ZjlkLTI3Mjg0MzNiYTU2ZSIsInZlcnNpb24iOjEsInRvcGljcyI6W10sImN1c3RvbVByZWZlcmVuY2VzIjpbXX1dLCJub3RpY2VzIjpbXSwiZHNEYXRhRWxlbWVudHMiOlsiVXNlckFnZW50IiwiQ291bnRyeSIsIkludGVyYWN0aW9uVHlwZSJdfQ.Nlkh1C9HzKenjutAhtyvgNMvwQicgKtN8lhOKZBQ4MMtbIPpGxjX8aYK4B7HkgR7k0KKQEioMmzMmamJzC584EZtm-AeUfXMrQ-GhPf5-jCXEylvw86t7a9b-4Hh7IqqyDMc1IrWlHvSm5q3tUfVw9JuJOQW3qSI-GeN5pK8nrGbF32YUHpgTNopwbO_xfdouMFHuxiJ0x4kS5aXINIP0zbHkx7NM7iLUNnQiS0UXWxrmX3cTAwac2EE6C-zOpgYh2Hp0Kc00jCWEJGpJAlQkjVa2u6dlNo7KGW_xbhSIu8l5sMx3mVOay4-_g1qPTCU--VFDM_ccNDYTtEoOQaOdW5rW5ZT7GYsK-JznhgM9ltkF8t-pmz_fQN8t_nT9rkmSjRZTEZQzY6cLEhOwjBuQ5wLY7ucht1GhhzWODpTbBrA8W52Dbw0Vv0WQLLVTTcybGG_8TCo_Qoyh3Y4yJQBYgKSK1FpytaHOMeATVE5iW90z4rmbjyeoXoxAuhK-QATFJ4o8vqVxx9kwppIhIQ_SyBmX4J5XhpPoblG6nqZVjAmecT8vzj_Zs8xXDWDnJsXULcUHvQuyxIO0RO2rZ3eoCQAqQg-bDHnLo-KT5PGcIiiJPnwfTj1Cw-nJ9eDW0J2fJD-Sr6YtL3dgjua42IQx880X0OlZCjIiejhDlQdu_E","identifier":"84285c39-6a42-48e3-9b28-b3a7921abd69","customPayload":{"Interaction":2,"AddDefaultInteraction":false},"isAnonymous":true,"test":false,"purposes":[{"Id":"3BC029DF-C5C7-4EAD-A2F5-17CA8F0F7378","TransactionType":"NO_CHOICE"},{"Id":"8D5CA2B0-81BE-4441-B680-FD1723B366C1","TransactionType":"CONFIRMED"},{"Id":"63A615E8-BC9C-4B1A-8130-AA94589F05A8","TransactionType":"CONFIRMED"},{"Id":"8D001F26-A91B-45BB-8DCB-12DE1C0C5CF9","TransactionType":"CONFIRMED"}],"dsDataElements":{}}',
)


r = requests.post(
    "https://bam.nr-data.net/events/1/5ca1a0d07f?a=274419876&sa=1&v=1198.fe6ec20&t=Unnamed%20Transaction&rst=4912&ck=1&ref=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
    headers={
        **base_headers,
        "Host": "bam.nr-data.net",
        "Accept": "*/*",
        "content-type": "text/plain",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json="bel.7;1,f,,3s4,3bz,8a,'initialPageLoad,'https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/,1,'https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/#||Ligne,,,!!!!'b9d0f419-8580-4211-8027-0783c3b77039,'1,!98;5,'title,'Nouveaux sacs et pochettes pour femme à découvrir | Hermès France;5,'referer,'https://www.hermes.com/fr/fr/;5,'page_type,'product grid;9,'department_code;5,'perfect_partner,'null;5,'perfect_partner_nb,'0;8,'stock_ecommerce;8,'stock_retail;5,'stock,'No Stock at all;2,,t8,6t,1,1,'POST,5k,'api-js.datadome.co:443,'/js/,2l7,5s,,'3,!!!;2,1,x6,aj,15,15,'GET,5k,'bck.hermes.com:443,'/categories,,mzx,,'4,!!!;2,1,18q,r6,8,9,o,5k,p,'/customer-session,,la,,'6,!!!;2,6,202,ak,gt,bm,o,5k,p,'/products,,1gsj,,'9,!!!;2,,2dw,c9,k,p,o,5k,'www.hermes.com:443,'/fr/fr/assets/i18n/fr-FR.json,,7qi,,'11,!!!;2,1,2dj,k1,5e,5f,o,5k,p,'/editorial,,1p4,,'10,!!!;2,,2xt,tk,r,11,o,5k,p,'/category/WOMENBAGSBAGSCLUTCHES,,2fy,,'16,!!!;2,,2fu,nt,o,w,o,5k,p,'/editorial/banners,,1v,,'12,!!!;2,,2gk,o6,1q,1y,o,5k,p,'/footer-items,,35u,,'13,!!!;2,,2l6,ot,s,11,o,5k,p,11,,2fy,,'15,!!!;2,,2kq,rp,x,18,o,5k,p,11,,2fy,,'14,!!!;2,,zf,b3,4,5,o,5k,'cdn-ukwest.onetrust.com:443,'/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/870afb0c-7f7a-4f57-a8d9-a461bd01c779.json,,21i,,'5,!!!;2,,1c6,g,,,o,5k,w,'/fr/fr/h,,1zf,1,'7,!!!;2,,1c7,r,-1,,o,5k,w,1c,,bdv,1,'8,!!!;2,,q3,wg,2,2,o,5k,p,'/feature-flag,,ri,,'2,!!!;b,68,!4,!-5y,,,,,,1l,44,,5,21,ge,21,8u,,1",
)


r = requests.get(
    "https://t.contentsquare.net/uxa/4c542426f49a4.js",
    headers={
        **base_headers,
        "Host": "t.contentsquare.net",
        "Accept": "*/*",
        "Referer": Referer_1,
        "If-Modified-Since": "Tue, 04 May 2021 15:17:17 GMT",
        "If-None-Match": '"693e86bb020504686b9d1ed9ced41227"',
        "TE": "Trailers",
    },
)


r = requests.post(
    "https://dcinfos-cache.abtasty.com/v1/geoip",
    headers={
        **base_headers,
        "Host": "dcinfos-cache.abtasty.com",
        "Accept": "*/*",
        "Referer": Referer_1,
        "Origin": Origin_1,
    },
    json='{"weather":true}',
)


r = requests.post(
    "https://dcinfos-cache.abtasty.com/v1/ua-parser",
    headers={
        **base_headers,
        "Host": "dcinfos-cache.abtasty.com",
        "Accept": "*/*",
        "Referer": Referer_1,
        "Origin": Origin_1,
    },
    json='{"ua":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0"}',
)


r = requests.post(
    "https://ariane.abtasty.com/",
    headers={
        **base_headers,
        "Host": "ariane.abtasty.com",
        "Accept": "*/*",
        "Referer": Referer_1,
        "Content-type": "text/plain",
        "Origin": Origin_1,
    },
    json='{"c":{},"cid":"2ba80386b56e4a2e33307bf9a949fb88","vid":"en75kr5epn6qpbxw","dr":"https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F","vp":"1440x340","sr":"1440x900","pt":"Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France","de":"UTF-8","sd":"24-bits","ul":"zh-CN","je":false,"dl":"https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne","cst":0,"sn":0,"sen":0,"lv":"YOvLC04p","h":[{"co":"yes","qt":1620508634902,"sen":0,"t":"CONSENT","ts":1620508634903,"ct":"https://www.hermes.com","pu":"AB+perso","me":"","op":"disabled","om":"permissiveMode"}],"t":"BATCH"}',
)


r = requests.get(
    "https://c.contentsquare.net/pageview?pid=4384&uu=0a06f4ea-99ab-a170-d6c9-0d77378fb788&sn=1&lv=1620508634&lhd=1620508634&hd=1620508634&pn=1&dw=1440&dh=6887&ww=1440&wh=340&sw=1440&sh=900&dr=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&url=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%3F__%7C%7CLigne&uc=1&la=zh-CN&cvars=%7B%221%22%3A%5B%22clienttype%22%2C%22non-connected%22%5D%2C%222%22%3A%5B%22pagetype%22%2C%22product%20grid%22%5D%2C%223%22%3A%5B%22pagename%22%2C%22Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France%22%5D%2C%224%22%3A%5B%22menu_lv1%22%2C%22WOMEN%22%5D%2C%225%22%3A%5B%22menu_lv2%22%2C%22WOMENBAGSSMALLLEATHERGOODS%22%5D%2C%227%22%3A%5B%22departmentcode%22%2C%22C%22%5D%2C%229%22%3A%5B%22category%22%2C%22C%2FC03%22%5D%7D&cvarp=%7B%221%22%3A%5B%22clienttype%22%2C%22non-connected%22%5D%2C%222%22%3A%5B%22pagetype%22%2C%22product%20grid%22%5D%2C%223%22%3A%5B%22pagename%22%2C%22Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France%22%5D%2C%224%22%3A%5B%22menu_lv1%22%2C%22WOMEN%22%5D%2C%225%22%3A%5B%22menu_lv2%22%2C%22WOMENBAGSSMALLLEATHERGOODS%22%5D%2C%227%22%3A%5B%22departmentcode%22%2C%22C%22%5D%2C%229%22%3A%5B%22category%22%2C%22C%2FC03%22%5D%7D&v=10.8.6&r=221373",
    headers={
        **base_headers,
        "Host": "c.contentsquare.net",
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://c.contentsquare.net/dvar?v=10.8.6&pid=4384&uu=0a06f4ea-99ab-a170-d6c9-0d77378fb788&sn=1&pn=1&dv=N4IgxgzgsghgLmAFgSwHYHMDSBTAniALhAAYA6ATgBZzyB2GgZgdoDYWmAOWgfQEYWATMQCsxDu0q9KLEAF8gA%3D%3D&r=939434",
    headers={
        **base_headers,
        "Host": "c.contentsquare.net",
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://adservice.google.com/ddm/fls/i/src=2292824;type=hermes;cat=rubrique;ord=1691937381844;gtm=2wg4s0;auiddc=324567000.1620508634;u13=undefined;~oref=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F",
    headers={
        **base_headers,
        "Host": "adservice.google.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://2292824.fls.doubleclick.net/",
        "Upgrade-Insecure-Requests": "1",
    },
)


r = requests.get(
    "https://adservice.google.com/ddm/fls/i/src=2292824;type=hermes;cat=rubrique;ord=6633002248200;gtm=2wg4s0;auiddc=324567000.1620508634;u13=undefined;~oref=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F",
    headers={
        **base_headers,
        "Host": "adservice.google.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://2292824.fls.doubleclick.net/",
        "Upgrade-Insecure-Requests": "1",
    },
)


r = requests.post(
    "https://ariane.abtasty.com/",
    headers={
        **base_headers,
        "Host": "ariane.abtasty.com",
        "Accept": "*/*",
        "Referer": Referer_1,
        "Content-type": "text/plain",
        "Origin": Origin_1,
        "TE": "Trailers",
    },
    json='{"c":{},"cid":"2ba80386b56e4a2e33307bf9a949fb88","vid":"en75kr5epn6qpbxw","dr":"https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F","vp":"1440x340","sr":"1440x900","pt":"Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France","de":"UTF-8","sd":"24-bits","ul":"zh-CN","je":false,"dl":"https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne","cst":1620508634906,"sn":1,"sen":1,"lv":"YOvLC04p","h":[{"qt":502,"sen":1,"t":"PAGEVIEW"}],"t":"BATCH"}',
)


r = requests.get(
    "https://www.google-analytics.com/analytics.js",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "*/*",
        "Referer": Referer_1,
    },
)


r = requests.get(
    "https://connect.facebook.net/en_US/fbevents.js",
    headers={
        **base_headers,
        "Host": "connect.facebook.net",
        "Accept": "*/*",
        "Referer": Referer_1,
    },
)


# These variables probably come from the result of the request above
Host_4 = "connect.facebook.net"
Host_5 = "www.facebook.com"


r = requests.post(
    "https://www.google-analytics.com/j/collect?v=1&_v=j90&aip=1&a=371548637&t=event&ni=1&cu=EUR&_s=1&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&dp=%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&ul=zh-cn&de=UTF-8&dt=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&sd=24-bit&sr=1440x900&vp=1440x340&je=0&ec=Cookie%20banner&ea=Accept%20all&el=Accept%20all&_u=YADAAEALAAAAAC~&jid=43071667&gjid=1876623485&cid=365684559.1620508634&tid=UA-64545050-1&_gid=622572613.1620508636&_r=1&gtm=2wg4s0W39B2P&cd12=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&cd13=product%20grid&cd14=WOMEN&cd15=WOMENBAGSSMALLLEATHERGOODS&cd16=WOMENBAGSBAGSCLUTCHES&cd25=desktop&cd26=fr&cd27=fr&cd30=non-connected&cd34=category%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&cd42=1620508634145.yjfp3z6h&cd43=2021-05-08T23%3A17%3A14.145&cd55=0.9499799337663387_1620508634146&z=89100704",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.post(
    "https://www.google-analytics.com/j/collect?v=1&_v=j90&aip=1&a=371548637&t=event&ni=1&cu=EUR&_s=1&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&dp=%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&ul=zh-cn&de=UTF-8&dt=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&sd=24-bit&sr=1440x900&vp=1440x340&je=0&ec=Cookie%20banner&ea=Accept%20all&el=Accept%20all&_u=YADAAEALAAAAAC~&jid=43071667&gjid=1876623485&cid=365684559.1620508634&tid=UA-72839523-2&_gid=622572613.1620508636&_r=1&gtm=2wg4s0W39B2P&cd12=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&cd13=product%20grid&cd14=WOMEN&cd15=WOMENBAGSSMALLLEATHERGOODS&cd16=WOMENBAGSBAGSCLUTCHES&cd25=desktop&cd26=fr&cd27=fr&cd30=non-connected&cd34=category%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&cd42=1620508634145.yjfp3z6h&cd43=2021-05-08T23%3A17%3A14.145&cd55=0.9499799337663387_1620508634146&z=89100704",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.post(
    "https://stats.g.doubleclick.net/j/collect?t=dc&aip=1&_r=3&v=1&_v=j90&tid=UA-64545050-1&cid=365684559.1620508634&jid=43071667&gjid=1876623485&_gid=622572613.1620508636&_u=YADAAEAKAAAAAC~&z=1390388526",
    headers={
        **base_headers,
        "Host": "stats.g.doubleclick.net",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
)


r = requests.post(
    "https://stats.g.doubleclick.net/j/collect?t=dc&aip=1&_r=3&v=1&_v=j90&tid=UA-64545050-1&cid=365684559.1620508634&jid=43071667&gjid=1876623485&_gid=622572613.1620508636&_u=YADAAEAKAAAAAC~&z=1390388526",
    headers={
        **base_headers,
        "Host": "stats.g.doubleclick.net",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
)


r = requests.get(
    "https://connect.facebook.net/signals/config/985290695141332?v=2.9.39&r=stable",
    headers={**base_headers, "Host": Host_4, "Accept": "*/*", "Referer": Referer_1},
)


r = requests.get(
    "https://www.google-analytics.com/plugins/ua/ec.js",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "*/*",
        "Referer": Referer_1,
        "If-Modified-Since": "Tue, 22 Oct 2019 18:15:00 GMT",
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.facebook.com/tr/?id=985290695141332&ev=PageView&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&rl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&if=false&ts=1620508636290&sw=1440&sh=900&v=2.9.39&r=stable&ec=0&o=30&fbp=fb.1.1620508611460.107273778&it=1620508635648&coo=false&exp=l0&rqm=GET",
    headers={
        **base_headers,
        "Host": Host_5,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://connect.facebook.net/signals/config/160189624660531?v=2.9.39&r=stable",
    headers={
        **base_headers,
        "Host": Host_4,
        "Accept": "*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.google.com/ads/ga-audiences?t=sr&aip=1&_r=4&slf_rd=1&v=1&_v=j90&tid=UA-64545050-1&cid=365684559.1620508634&jid=43071667&_u=YADAAEAKAAAAAC~&z=568188895",
    cookies={
        "CONSENT": "YES+srp.gws-20210503-0-RC2.zh-CN+FX+097",
        "NID": "215=G0okXND3gAjrynwVo8gkcqNdlFyjpBXrxEQHI8aA44YmRMUJRo_fgFvHaBMP4l21xpAreZNKu8EJcUOID40uCprrb3YZOsP0rr_3HW_Jy-d28hxONMCjOdCyAAJlny2lptlYu9EkKll9FdSgslAp6SHXKMk-Ty7HM2KrWDBOQIA",
        "1P_JAR": "2021-05-08-21",
        "ANID": "AHWqTUlsw9tkiN3fIHO3G06zseUv_Z1rHtr9VisBs33-Av5tOe8mMOxUXOUo0XvK",
        "DV": "s9RY9Px3GT5HcNiZldgA7vwIxWbdlFc4dyRxmh2z6AAAANBqpq0xxbXG2CdzA1goguTbC5XtOcrcAA",
    },
    headers={
        **base_headers,
        "Host": "www.google.com",
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "CONSENT=YES+srp.gws-20210503-0-RC2.zh-CN+FX+097; NID=215=G0okXND3gAjrynwVo8gkcqNdlFyjpBXrxEQHI8aA44YmRMUJRo_fgFvHaBMP4l21xpAreZNKu8EJcUOID40uCprrb3YZOsP0rr_3HW_Jy-d28hxONMCjOdCyAAJlny2lptlYu9EkKll9FdSgslAp6SHXKMk-Ty7HM2KrWDBOQIA; 1P_JAR=2021-05-08-21; ANID=AHWqTUlsw9tkiN3fIHO3G06zseUv_Z1rHtr9VisBs33-Av5tOe8mMOxUXOUo0XvK; DV=s9RY9Px3GT5HcNiZldgA7vwIxWbdlFc4dyRxmh2z6AAAANBqpq0xxbXG2CdzA1goguTbC5XtOcrcAA",
    },
)


r = requests.get(
    "https://www.google.co.in/ads/ga-audiences?t=sr&aip=1&_r=4&slf_rd=1&v=1&_v=j90&tid=UA-64545050-1&cid=365684559.1620508634&jid=43071667&_u=YADAAEAKAAAAAC~&z=568188895",
    headers={
        **base_headers,
        "Host": "www.google.co.in",
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
    },
)


r = requests.get(
    "https://www.google-analytics.com/collect?v=1&_v=j90&aip=1&a=371548637&t=event&ni=1&cu=EUR&_s=1&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&dp=%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&ul=zh-cn&de=UTF-8&dt=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&sd=24-bit&sr=1440x900&vp=1440x340&je=0&ec=Ecommerce&ea=Impressions&_u=aCDAAEALAAAAAC~&jid=&gjid=&cid=365684559.1620508634&tid=UA-64545050-1&_gid=622572613.1620508636&gtm=2wg4s0W39B2P&cd12=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&cd13=product%20grid&cd14=WOMEN&cd15=WOMENBAGSSMALLLEATHERGOODS&cd16=WOMENBAGSBAGSCLUTCHES&cd25=desktop&cd26=fr&cd27=fr&cd30=non-connected&cd34=category%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&cd42=1620508634176.kc1n5as8&cd43=2021-05-08T23%3A17%3A14.176&cd55=0.9499799337663387_1620508634146&z=165862669",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.google-analytics.com/collect?v=1&_v=j90&aip=1&a=371548637&t=pageview&cu=EUR&_s=1&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&dp=%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&ul=zh-cn&de=UTF-8&dt=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&sd=24-bit&sr=1440x900&vp=1440x340&je=0&_u=aCDAAEALAAAAAC~&jid=&gjid=&cid=365684559.1620508634&tid=UA-64545050-1&_gid=622572613.1620508636&gtm=2wg4s0W39B2P&cd12=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&cd13=product%20grid&cd14=WOMEN&cd15=WOMENBAGSSMALLLEATHERGOODS&cd16=WOMENBAGSBAGSCLUTCHES&cd25=desktop&cd26=fr&cd27=fr&cd30=non-connected&cd34=category%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&cd42=1620508634234.796u5pjn&cd43=2021-05-08T23%3A17%3A14.234&cd55=0.9499799337663387_1620508634146&z=815677044",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.google-analytics.com/collect?v=1&_v=j90&aip=1&a=371548637&t=pageview&cu=EUR&_s=1&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&dp=%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&ul=zh-cn&de=UTF-8&dt=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&sd=24-bit&sr=1440x900&vp=1440x340&je=0&_u=aCDAAEALAAAAAC~&jid=&gjid=&cid=365684559.1620508634&tid=UA-72839523-2&_gid=622572613.1620508636&gtm=2wg4s0W39B2P&cd12=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&cd13=product%20grid&cd14=WOMEN&cd15=WOMENBAGSSMALLLEATHERGOODS&cd16=WOMENBAGSBAGSCLUTCHES&cd25=desktop&cd26=fr&cd27=fr&cd30=non-connected&cd34=category%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&cd42=1620508634234.796u5pjn&cd43=2021-05-08T23%3A17%3A14.234&cd55=0.9499799337663387_1620508634146&z=815677044",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.facebook.com/tr/?id=160189624660531&ev=PageView&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&rl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&if=false&ts=1620508636588&sw=1440&sh=900&v=2.9.39&r=stable&ec=0&o=30&fbp=fb.1.1620508611460.107273778&it=1620508635648&coo=false&exp=l0&rqm=GET",
    headers={
        **base_headers,
        "Host": Host_5,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.google-analytics.com/collect?v=1&_v=j90&aip=1&a=371548637&t=event&ni=1&cu=EUR&_s=1&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&dp=%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&ul=zh-cn&de=UTF-8&dt=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&sd=24-bit&sr=1440x900&vp=1440x340&je=0&ec=Ecommerce&ea=Impressions&_u=aCDAAEALAAAAAC~&jid=&gjid=&cid=365684559.1620508634&tid=UA-64545050-1&_gid=622572613.1620508636&gtm=2wg4s0W39B2P&cd12=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&cd13=product%20grid&cd14=WOMEN&cd15=WOMENBAGSSMALLLEATHERGOODS&cd16=WOMENBAGSBAGSCLUTCHES&cd20=Production%20version&cd25=desktop&cd26=fr&cd27=fr&cd30=non-connected&cd33=C&cd34=category%2Fwomen%2Fbags-and-small-leather-goods%2Fbags-and-clutches%2F&cd42=1620508634844.tlr2t0ko&cd43=2021-05-08T23%3A17%3A14.844&cd55=0.9499799337663387_1620508634146&il1nm=product%20grid&il1pi1nm=Sac%20Herm%C3%A8s%20Cinhetic%20verso&il1pi1id=H073540CTAA&il1pi1pr=7250.00&il1pi1br=hermes&il1pi1ca=C%2FC03&il1pi1va=bleu&il1pi1cd5=SANS_TAILLE&il1pi1cd6=C&il1pi1cd7=C03&il1pi1cd8=C031&il1pi1cd9=01&il1pi1cd10=N%2FA&il1pi1cd52=no&il1pi1ps=1&il1pi2nm=Sac%20Bolide%2031&il1pi2id=H073419CKM3&il1pi2pr=6200.00&il1pi2br=hermes&il1pi2ca=C%2FC03&il1pi2va=bleu&il1pi2cd5=SANS_TAILLE&il1pi2cd6=C&il1pi2cd7=C03&il1pi2cd8=C031&il1pi2cd9=01&il1pi2cd10=N%2FA&il1pi2cd52=no&il1pi2ps=2&il1pi3nm=Sac%20Herm%C3%A8s%20Cinhetic&il1pi3id=H076143CKM3&il1pi3pr=6750.00&il1pi3br=hermes&il1pi3ca=C%2FC03&il1pi3va=bleu&il1pi3cd5=SANS_TAILLE&il1pi3cd6=C&il1pi3cd7=C03&il1pi3cd8=C031&il1pi3cd9=01&il1pi3cd10=N%2FA&il1pi3cd52=no&il1pi3ps=4&z=175006351",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.facebook.com/tr/?id=985290695141332&ev=Microdata&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&rl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&if=false&ts=1620508636797&cd[DataLayer]=%5B%5D&cd[Meta]=%7B%22title%22%3A%22Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France%22%2C%22meta%3Adescription%22%3A%22Sacs%20%C3%A0%20dos%2C%20sacs%20bandouli%C3%A8re%2C%20sacs%20besace%20et%20pochettes%20pour%20femme%2C%20de%20magnifiques%20cr%C3%A9ations%20%C3%A0%20d%C3%A9couvrir%20en%20exclusivit%C3%A9%20sur%20le%20site%20officiel%20Herm%C3%A8s.%22%7D&cd[OpenGraph]=%7B%22og%3Atype%22%3A%22website%22%2C%22og%3Atitle%22%3A%22Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%22%2C%22og%3Adescription%22%3A%22Sacs%20%C3%A0%20dos%2C%20sacs%20bandouli%C3%A8re%2C%20sacs%20besace%20et%20pochettes%20pour%20femme%2C%20de%20magnifiques%20cr%C3%A9ations%20%C3%A0%20d%C3%A9couvrir%20en%20exclusivit%C3%A9%20sur%20le%20site%20officiel%20Herm%C3%A8s.%22%2C%22og%3Aurl%22%3A%22https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%22%7D&cd[Schema.org]=%5B%7B%22dimensions%22%3A%7B%22h%22%3A53%2C%22w%22%3A84%7D%2C%22properties%22%3A%7B%22url%22%3A%22%2Ffr%2Ffr%2F%22%7D%2C%22subscopes%22%3A%5B%5D%2C%22type%22%3A%22http%3A%2F%2Fschema.org%2FOrganization%22%7D%5D&cd[JSON-LD]=%5B%5D&sw=1440&sh=900&v=2.9.39&r=stable&ec=1&o=30&fbp=fb.1.1620508611460.107273778&it=1620508635648&coo=false&es=automatic&tm=3&exp=l0&rqm=GET",
    headers={
        **base_headers,
        "Host": Host_5,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.get(
    "https://www.facebook.com/tr/?id=160189624660531&ev=Microdata&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&rl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&if=false&ts=1620508637090&cd[DataLayer]=%5B%5D&cd[Meta]=%7B%22title%22%3A%22Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France%22%2C%22meta%3Adescription%22%3A%22Sacs%20%C3%A0%20dos%2C%20sacs%20bandouli%C3%A8re%2C%20sacs%20besace%20et%20pochettes%20pour%20femme%2C%20de%20magnifiques%20cr%C3%A9ations%20%C3%A0%20d%C3%A9couvrir%20en%20exclusivit%C3%A9%20sur%20le%20site%20officiel%20Herm%C3%A8s.%22%7D&cd[OpenGraph]=%7B%22og%3Atype%22%3A%22website%22%2C%22og%3Atitle%22%3A%22Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%22%2C%22og%3Adescription%22%3A%22Sacs%20%C3%A0%20dos%2C%20sacs%20bandouli%C3%A8re%2C%20sacs%20besace%20et%20pochettes%20pour%20femme%2C%20de%20magnifiques%20cr%C3%A9ations%20%C3%A0%20d%C3%A9couvrir%20en%20exclusivit%C3%A9%20sur%20le%20site%20officiel%20Herm%C3%A8s.%22%2C%22og%3Aurl%22%3A%22https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%22%7D&cd[Schema.org]=%5B%7B%22dimensions%22%3A%7B%22h%22%3A53%2C%22w%22%3A84%7D%2C%22properties%22%3A%7B%22url%22%3A%22%2Ffr%2Ffr%2F%22%7D%2C%22subscopes%22%3A%5B%5D%2C%22type%22%3A%22http%3A%2F%2Fschema.org%2FOrganization%22%7D%5D&cd[JSON-LD]=%5B%5D&sw=1440&sh=900&v=2.9.39&r=stable&ec=1&o=30&fbp=fb.1.1620508611460.107273778&it=1620508635648&coo=false&es=automatic&tm=3&exp=l0&rqm=GET",
    headers={
        **base_headers,
        "Host": Host_5,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.post(
    "https://c.contentsquare.net/events?v=10.8.6&str=153&di=226&dc=1207&fl=1208&sr=5&mdh=6887&pn=1&uu=0a06f4ea-99ab-a170-d6c9-0d77378fb788&sn=1&lv=1620508634&lhd=1620508634&hd=1620508634&pid=4384&eu=%5B%5B0%2C21%2C1440%2C340%5D%5D",
    headers={
        **base_headers,
        "Host": "c.contentsquare.net",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
)


r = requests.post(
    "https://www.google-analytics.com/g/collect?v=2&tid=G-Y862HCHCQ7&gtm=2oe4s0&_p=371548637&sr=1440x900&ul=zh-cn&cid=365684559.1620508634&dl=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F&dr=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2F&dt=Nouveaux%20sacs%20et%20pochettes%20pour%20femme%20%C3%A0%20d%C3%A9couvrir%20%7C%20Herm%C3%A8s%20France&sid=1620506827&sct=1&seg=1&_s=1",
    headers={
        **base_headers,
        "Host": "www.google-analytics.com",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "TE": "Trailers",
    },
    json="en=Page%20view&_et=3&ep.page_type=product%20grid\r\nen=view_item_list&_et=482&pr1=idH073540CTAA~nmSac%20Herm%C3%A8s%20Cinhetic%20verso~pr7250.00~brhermes~caC%2FC03~lp1~lnproduct%20grid&pr2=idH073419CKM3~nmSac%20Bolide%2031~pr6200.00~brhermes~caC%2FC03~lp2~lnproduct%20grid&pr3=idH076143CKM3~nmSac%20Herm%C3%A8s%20Cinhetic~pr6750.00~brhermes~caC%2FC03~lp4~lnproduct%20grid&ep.page_type=product%20grid",
)


r = requests.post(
    "https://api-js.datadome.co/js/",
    headers={
        **base_headers,
        "Host": "api-js.datadome.co",
        "Accept": "*/*",
        "Content-type": "application/x-www-form-urlencoded",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json="jsData=%7B%22ttst%22%3A49%2C%22ifov%22%3Afalse%2C%22wdifts%22%3Afalse%2C%22wdifrm%22%3Afalse%2C%22wdif%22%3Afalse%2C%22br_h%22%3A340%2C%22br_w%22%3A1440%2C%22br_oh%22%3A900%2C%22br_ow%22%3A1440%2C%22nddc%22%3A1%2C%22rs_h%22%3A900%2C%22rs_w%22%3A1440%2C%22rs_cd%22%3A24%2C%22phe%22%3Afalse%2C%22nm%22%3Afalse%2C%22jsf%22%3Afalse%2C%22ua%22%3A%22Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010.15%3B%20rv%3A88.0)%20Gecko%2F20100101%20Firefox%2F88.0%22%2C%22lg%22%3A%22zh-CN%22%2C%22pr%22%3A2%2C%22hc%22%3A4%2C%22ars_h%22%3A900%2C%22ars_w%22%3A1440%2C%22tz%22%3A-120%2C%22str_ss%22%3Atrue%2C%22str_ls%22%3Atrue%2C%22str_idb%22%3Atrue%2C%22str_odb%22%3Afalse%2C%22plgod%22%3Afalse%2C%22plg%22%3A0%2C%22plgne%22%3A%22NA%22%2C%22plgre%22%3A%22NA%22%2C%22plgof%22%3A%22NA%22%2C%22plggt%22%3A%22NA%22%2C%22pltod%22%3Afalse%2C%22lb%22%3Afalse%2C%22eva%22%3A37%2C%22lo%22%3Afalse%2C%22ts_mtp%22%3A0%2C%22ts_tec%22%3Afalse%2C%22ts_tsa%22%3Afalse%2C%22vnd%22%3A%22%22%2C%22bid%22%3A%2220181001000000%22%2C%22mmt%22%3A%22empty%22%2C%22plu%22%3A%22empty%22%2C%22hdn%22%3Afalse%2C%22awe%22%3Afalse%2C%22geb%22%3Afalse%2C%22dat%22%3Afalse%2C%22med%22%3A%22defined%22%2C%22aco%22%3A%22probably%22%2C%22acots%22%3Afalse%2C%22acmp%22%3A%22maybe%22%2C%22acmpts%22%3Afalse%2C%22acw%22%3A%22probably%22%2C%22acwts%22%3Afalse%2C%22acma%22%3A%22maybe%22%2C%22acmats%22%3Afalse%2C%22acaa%22%3A%22maybe%22%2C%22acaats%22%3Afalse%2C%22ac3%22%3A%22%22%2C%22ac3ts%22%3Afalse%2C%22acf%22%3A%22maybe%22%2C%22acfts%22%3Afalse%2C%22acmp4%22%3A%22maybe%22%2C%22acmp4ts%22%3Atrue%2C%22acmp3%22%3A%22maybe%22%2C%22acmp3ts%22%3Afalse%2C%22acwm%22%3A%22maybe%22%2C%22acwmts%22%3Atrue%2C%22ocpt%22%3Afalse%2C%22vco%22%3A%22probably%22%2C%22vcots%22%3Afalse%2C%22vch%22%3A%22probably%22%2C%22vchts%22%3Atrue%2C%22vcw%22%3A%22probably%22%2C%22vcwts%22%3Atrue%2C%22vc3%22%3A%22%22%2C%22vc3ts%22%3Afalse%2C%22vcmp%22%3A%22%22%2C%22vcmpts%22%3Afalse%2C%22vcq%22%3A%22maybe%22%2C%22vcqts%22%3Afalse%2C%22vc1%22%3A%22probably%22%2C%22vc1ts%22%3Afalse%2C%22dvm%22%3A%22NA%22%2C%22sqt%22%3Afalse%2C%22so%22%3A%22landscape-primary%22%2C%22wbd%22%3Afalse%2C%22wbdm%22%3Atrue%2C%22wdw%22%3Atrue%2C%22ecpc%22%3Afalse%2C%22lgs%22%3Atrue%2C%22lgsod%22%3Afalse%2C%22bcda%22%3Afalse%2C%22idn%22%3Atrue%2C%22capi%22%3Afalse%2C%22svde%22%3Afalse%2C%22vpbq%22%3Atrue%2C%22xr%22%3Afalse%2C%22bgav%22%3Afalse%2C%22rri%22%3Atrue%2C%22idfr%22%3Afalse%2C%22ancs%22%3Atrue%2C%22inlc%22%3Atrue%2C%22cgca%22%3Afalse%2C%22inlf%22%3Atrue%2C%22tecd%22%3Afalse%2C%22sbct%22%3Atrue%2C%22aflt%22%3Atrue%2C%22rgp%22%3Atrue%2C%22bint%22%3Atrue%2C%22spwn%22%3Afalse%2C%22emt%22%3Afalse%2C%22bfr%22%3Afalse%2C%22dbov%22%3Afalse%2C%22glvd%22%3A%22ATI%20Technologies%20Inc.%22%2C%22glrd%22%3A%22AMD%20Radeon%20R9%20M370X%20OpenGL%20Engine%22%2C%22tagpu%22%3A6%2C%22prm%22%3Atrue%2C%22tzp%22%3A%22Europe%2FParis%22%2C%22cvs%22%3Atrue%2C%22usb%22%3A%22NA%22%2C%22dcok%22%3A%22.hermes.com%22%2C%22mp_cx%22%3A876%2C%22mp_cy%22%3A262%2C%22mp_tr%22%3Atrue%2C%22mp_mx%22%3A2%2C%22mp_my%22%3A0%2C%22mp_sx%22%3A876%2C%22mp_sy%22%3A364%2C%22ewsi%22%3Afalse%2C%22tbce%22%3A80%7D&events=%5B%7B%22source%22%3A%7B%22x%22%3A743%2C%22y%22%3A321%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508632219%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A805%2C%22y%22%3A267%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508632320%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A809%2C%22y%22%3A271%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508632435%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A832%2C%22y%22%3A270%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508632537%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A874%2C%22y%22%3A262%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508633067%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A882%2C%22y%22%3A247%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508633188%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A880%2C%22y%22%3A247%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508633319%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A868%2C%22y%22%3A247%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508633436%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A868%2C%22y%22%3A247%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508633713%2C%22id%22%3A0%7D%2C%7B%22source%22%3A%7B%22x%22%3A868%2C%22y%22%3A247%7D%2C%22message%22%3A%22mouse%20click%22%2C%22date%22%3A1620508633989%2C%22id%22%3A1%7D%2C%7B%22source%22%3A%7B%22x%22%3A773%2C%22y%22%3A328%7D%2C%22message%22%3A%22mouse%20move%22%2C%22date%22%3A1620508634310%2C%22id%22%3A0%7D%5D&eventCounters=%7B%22mouse%20move%22%3A10%2C%22mouse%20click%22%3A1%2C%22scroll%22%3A0%2C%22touch%20start%22%3A0%2C%22touch%20end%22%3A0%2C%22touch%20move%22%3A0%2C%22key%20press%22%3A0%2C%22key%20down%22%3A0%2C%22key%20up%22%3A0%7D&jsType=le&cid=Ddhvy8KQU6tD-6cBnApTciV7KlXldNXAuF_AW2z7CoXSF4So~nxhQC9s3D9SY7eNqxpKvzqppN1mqqX8sI-86R7cg8Z~SAm7K4AYLZa4J0&ddk=2211F522B61E269B869FA6EAFFB5E1&Referer=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&request=%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&responsePage=origin&ddv=4.1.48",
)


r = requests.post(
    "https://bam.nr-data.net/jserrors/1/5ca1a0d07f?a=274419876&sa=1&v=1198.fe6ec20&t=Unnamed%20Transaction&rst=63868&ck=1&ref=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
    headers={
        **base_headers,
        "Host": "bam.nr-data.net",
        "Accept": "*/*",
        "content-type": "text/plain",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json='{"ierr":[{"params":{"stackHash":389037123,"exceptionClass":"TypeError","request_uri":"/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/","message":"can\'t convert null to object","stack_trace":"r@<inline>:35:24231\\n__nr_require<[6]</<@<inline>:35:5719\\nn@<inline>:35:23396\\nu@<inline>:35:22628\\nZ/<@https://www.hermes.com/fr/fr/polyfills-es2015.2b516c6d2858f0db3ab0.js:1:108381\\nf/<@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:2557646\\nf@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:2557752\\nu47x@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:2962663\\nd@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:552\\niTwO@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:2248349\\nd@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:552\\n0@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:66207\\nd@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:552\\na@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:421\\nc@https://www.hermes.com/fr/fr/runtime-es2015.19c2cb4d54792f9200e4.js:1:293\\n@https://www.hermes.com/fr/fr/main-es2015.9a18e18c1f704ae1bc14.js:3:47","releaseIds":"{}","pageview":1,"browserInteractionId":"b9d0f419-8580-4211-8027-0783c3b77039"},"custom":{"title":"Nouveaux sacs et pochettes pour femme à découvrir | Hermès France","referer":"https://www.hermes.com/fr/fr/","page_type":"product grid","perfect_partner":"null","perfect_partner_nb":"0","stock_ecommerce":false,"stock_retail":false,"stock":"No Stock at all"},"metrics":{"count":1,"time":{"t":858}}}],"xhr":[{"params":{"method":"POST","host":"api-js.datadome.co:443","pathname":"/js/","status":200},"metrics":{"count":2,"txSize":{"t":8708,"min":3355,"max":5353,"sos":39910634,"c":2},"rxSize":{"t":417,"min":208,"max":209,"sos":86945,"c":2},"duration":{"t":459,"min":211,"max":248,"sos":106025,"c":2},"cbTime":{"t":0,"min":0,"max":0,"sos":0,"c":2},"time":{"t":13602,"min":1050,"max":12552,"sos":158655204,"c":2}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/categories","status":200},"metrics":{"count":1,"rxSize":{"t":29805},"duration":{"t":420},"cbTime":{"t":41},"time":{"t":1194}}},{"params":{"method":"GET","host":"cdn-ukwest.onetrust.com:443","pathname":"/consent/870afb0c-7f7a-4f57-a8d9-a461bd01c779/870afb0c-7f7a-4f57-a8d9-a461bd01c779.json","status":200},"metrics":{"count":1,"rxSize":{"t":2646},"duration":{"t":403},"cbTime":{"t":6},"time":{"t":1275}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/feature-flag","status":200},"metrics":{"count":1,"rxSize":{"t":990},"duration":{"t":1170},"cbTime":{"t":2},"time":{"t":939}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/customer-session","status":200},"metrics":{"count":1,"rxSize":{"t":766},"duration":{"t":986},"cbTime":{"t":8},"time":{"t":1610}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/products","status":200},"metrics":{"count":1,"rxSize":{"t":68419},"duration":{"t":795},"cbTime":{"t":413},"time":{"t":2594}}},{"params":{"method":"GET","host":"www.hermes.com:443","pathname":"/fr/fr/assets/i18n/fr-FR.json","status":200},"metrics":{"count":1,"rxSize":{"t":10026},"duration":{"t":461},"cbTime":{"t":18},"time":{"t":3092}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/editorial","status":200},"metrics":{"count":1,"rxSize":{"t":2200},"duration":{"t":910},"cbTime":{"t":187},"time":{"t":3079}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/editorial/banners","status":200},"metrics":{"count":1,"rxSize":{"t":67},"duration":{"t":881},"cbTime":{"t":20},"time":{"t":3162}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/footer-items","status":200},"metrics":{"count":1,"rxSize":{"t":4098},"duration":{"t":932},"cbTime":{"t":59},"time":{"t":3188}}},{"params":{"method":"GET","host":"bck.hermes.com:443","pathname":"/category/WOMENBAGSBAGSCLUTCHES","status":200},"metrics":{"count":3,"rxSize":{"t":9498,"min":3166,"max":3166,"sos":30070668,"c":3},"duration":{"t":3043,"min":922,"max":1091,"sos":3101265,"c":3},"cbTime":{"t":68,"min":21,"max":24,"sos":1546,"c":3},"time":{"t":10500,"min":3338,"max":3809,"sos":36893334,"c":3}}},{"params":{"method":"post","host":"privacyportal-uk.onetrust.com:443","pathname":"/request/v1/consentreceipts","status":200},"metrics":{"count":1,"txSize":{"t":5681},"rxSize":{"t":2080},"duration":{"t":794},"cbTime":{"t":0},"time":{"t":4318}}},{"params":{"method":"POST","host":"bam.nr-data.net:443","pathname":"/events/1/5ca1a0d07f","status":200},"metrics":{"count":1,"txSize":{"t":1501},"rxSize":{"t":24},"duration":{"t":201},"cbTime":{"t":0},"time":{"t":4913}}},{"params":{"method":"POST","host":"www.google-analytics.com:443","pathname":"/j/collect","status":200},"metrics":{"count":2,"rxSize":{"t":4,"min":2,"max":2,"sos":8,"c":2},"duration":{"t":453,"min":224,"max":229,"sos":102617,"c":2},"cbTime":{"t":0,"min":0,"max":0,"sos":0,"c":2},"time":{"t":11984,"min":5991,"max":5993,"sos":71808130,"c":2}}},{"params":{"method":"POST","host":"stats.g.doubleclick.net:443","pathname":"/j/collect","status":200},"metrics":{"count":2,"rxSize":{"t":14,"min":7,"max":7,"sos":98,"c":2},"duration":{"t":1346,"min":671,"max":675,"sos":905866,"c":2},"cbTime":{"t":0,"min":0,"max":0,"sos":0,"c":2},"time":{"t":12435,"min":6216,"max":6219,"sos":77314617,"c":2}}}]}',
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073419CKM3_worn_6?a=a&size=3000,3000&extend=0,0,0,0&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508634.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
        "_ga": "GA1.2.365684559.1620508634",
        "ABTastySession": "mrasn=&lp=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&sen=1",
        "ABTasty": "uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=",
        "_cs_c": "1",
        "_cs_id": "0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0",
        "_cs_s": "1.0",
        "_gid": "GA1.2.622572613.1620508636",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508634.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146; _ga=GA1.2.365684559.1620508634; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&sen=1; ABTasty=uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=; _cs_c=1; _cs_id=0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0; _cs_s=1.0; _gid=GA1.2.622572613.1620508636",
        "If-Modified-Since": "Tue, 29 Oct 2019 22:00:57 GMT",
        "If-None-Match": '"616b1b22b49f11650f09ed50fa497184"',
        "Cache-Control": "max-age=0",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073419CKM3_front_1?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508634.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
        "_ga": "GA1.2.365684559.1620508634",
        "ABTastySession": "mrasn=&lp=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&sen=1",
        "ABTasty": "uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=",
        "_cs_c": "1",
        "_cs_id": "0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0",
        "_cs_s": "1.0",
        "_gid": "GA1.2.622572613.1620508636",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508634.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146; _ga=GA1.2.365684559.1620508634; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&sen=1; ABTasty=uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=; _cs_c=1; _cs_id=0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0; _cs_s=1.0; _gid=GA1.2.622572613.1620508636",
        "If-Modified-Since": "Tue, 29 Oct 2019 22:00:57 GMT",
        "If-None-Match": '"8b188f87cb00ff722820a06fbdc27d25"',
        "Cache-Control": "max-age=0",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073419CKM3_side_2?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508634.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
        "_ga": "GA1.2.365684559.1620508634",
        "ABTastySession": "mrasn=&lp=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&sen=1",
        "ABTasty": "uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=",
        "_cs_c": "1",
        "_cs_id": "0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0",
        "_cs_s": "1.0",
        "_gid": "GA1.2.622572613.1620508636",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508634.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146; _ga=GA1.2.365684559.1620508634; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&sen=1; ABTasty=uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=; _cs_c=1; _cs_id=0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0; _cs_s=1.0; _gid=GA1.2.622572613.1620508636",
        "If-Modified-Since": "Tue, 29 Oct 2019 22:00:57 GMT",
        "If-None-Match": '"926e987f48123874f284c8ea473cdfec"',
        "Cache-Control": "max-age=0",
    },
)


r = requests.post(
    "https://c.contentsquare.net/events?v=10.8.6&str=153&di=226&dc=1207&fl=1208&sr=5&mdh=6887&pn=1&uu=0a06f4ea-99ab-a170-d6c9-0d77378fb788&sn=1&lv=1620508634&lhd=1620508634&hd=1620508634&pid=4384&eu=%5B%5B6%2C132738%2C791%2C289%2C%22ul%23grid-results-ul%3Eli%3Aeq(1)%3Eh-grid-result-item%3Aeq(0)%3Ediv%3Aeq(0)%3Ea%3Aeq(0)%3Ediv%3Aeq(0)%3Eh-image-resizer%3Aeq(0)%3Epicture%3Aeq(0)%3Eimg%3Aeq(0)%22%2C%22%22%5D%2C%5B7%2C132785%2C791%2C289%2C%22ul%23grid-results-ul%3Eli%3Aeq(1)%3Eh-grid-result-item%3Aeq(0)%3Ediv%3Aeq(0)%3Ea%3Aeq(0)%3Ediv%3Aeq(0)%3Eh-image-resizer%3Aeq(0)%3Epicture%3Aeq(0)%3Eimg%3Aeq(0)%22%5D%2C%5B6%2C132786%2C791%2C289%2C%22div%23carousel-item2%3Ea%3Aeq(0)%22%2C%22%22%5D%2C%5B7%2C132892%2C791%2C289%2C%22div%23carousel-item2%3Ea%3Aeq(0)%22%5D%5D",
    headers={
        **base_headers,
        "Host": "c.contentsquare.net",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
)


r = requests.post(
    "https://c.contentsquare.net/events?v=10.8.6&str=153&di=226&dc=1207&fl=1208&sr=5&mdh=6887&pn=1&uu=0a06f4ea-99ab-a170-d6c9-0d77378fb788&sn=1&lv=1620508634&lhd=1620508634&hd=1620508634&pid=4384&eu=%5B%5B2%2C163497%2C29%2C8%5D%2C%5B6%2C163780%2C644%2C234%2C%22ul%23grid-results-ul%3Eli%3Aeq(0)%3Eh-grid-result-item%3Aeq(0)%3Ediv%3Aeq(0)%3Ea%3Aeq(0)%22%2C%22%22%5D%2C%5B2%2C163901%2C644%2C234%5D%2C%5B7%2C163989%2C644%2C234%2C%22ul%23grid-results-ul%3Eli%3Aeq(0)%3Eh-grid-result-item%3Aeq(0)%3Ediv%3Aeq(0)%3Ea%3Aeq(0)%22%5D%5D",
    headers={
        **base_headers,
        "Host": "c.contentsquare.net",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)


r = requests.post(
    "https://bam.nr-data.net/jserrors/1/5ca1a0d07f?a=274419876&sa=1&v=1198.fe6ec20&t=Unnamed%20Transaction&rst=185658&ck=1&ref=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
    headers={
        **base_headers,
        "Host": "bam.nr-data.net",
        "Accept": "*/*",
        "content-type": "text/plain",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json='{"xhr":[{"params":{"method":"POST","host":"bam.nr-data.net:443","pathname":"/jserrors/1/5ca1a0d07f","status":0},"metrics":{"count":1,"txSize":{"t":5455},"duration":{"t":73751},"cbTime":{"t":0},"time":{"t":63871}}}]}',
)


r = requests.post(
    "https://bam.nr-data.net/jserrors/1/5ca1a0d07f?a=274419876&sa=1&v=1198.fe6ec20&t=Unnamed%20Transaction&rst=247027&ck=1&ref=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
    headers={
        **base_headers,
        "Host": "bam.nr-data.net",
        "Accept": "*/*",
        "content-type": "text/plain",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json='{"xhr":[{"params":{"method":"POST","host":"bam.nr-data.net:443","pathname":"/jserrors/1/5ca1a0d07f","status":200},"metrics":{"count":1,"txSize":{"t":215},"rxSize":{"t":24},"duration":{"t":780},"cbTime":{"t":1},"time":{"t":185660}}}]}',
)


r = requests.post(
    "https://bam.nr-data.net/jserrors/1/5ca1a0d07f?a=274419876&sa=1&v=1198.fe6ec20&t=Unnamed%20Transaction&rst=308513&ck=1&ref=https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/",
    headers={
        **base_headers,
        "Host": "bam.nr-data.net",
        "Accept": "*/*",
        "content-type": "text/plain",
        "Origin": Origin_1,
        "Referer": Referer_1,
    },
    json='{"xhr":[{"params":{"method":"POST","host":"bam.nr-data.net:443","pathname":"/jserrors/1/5ca1a0d07f","status":200},"metrics":{"count":1,"txSize":{"t":233},"rxSize":{"t":24},"duration":{"t":203},"cbTime":{"t":0},"time":{"t":247028}}}]}',
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073540CTAA_back_3?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508634.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
        "_ga": "GA1.2.365684559.1620508634",
        "ABTastySession": "mrasn=&lp=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&sen=1",
        "ABTasty": "uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=",
        "_cs_c": "1",
        "_cs_id": "0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0",
        "_cs_s": "1.0",
        "_gid": "GA1.2.622572613.1620508636",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508634.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146; _ga=GA1.2.365684559.1620508634; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&sen=1; ABTasty=uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=; _cs_c=1; _cs_id=0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0; _cs_s=1.0; _gid=GA1.2.622572613.1620508636",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073540CTAA_front_1?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508634.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
        "_ga": "GA1.2.365684559.1620508634",
        "ABTastySession": "mrasn=&lp=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&sen=1",
        "ABTasty": "uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=",
        "_cs_c": "1",
        "_cs_id": "0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0",
        "_cs_s": "1.0",
        "_gid": "GA1.2.622572613.1620508636",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508634.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146; _ga=GA1.2.365684559.1620508634; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&sen=1; ABTasty=uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=; _cs_c=1; _cs_id=0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0; _cs_s=1.0; _gid=GA1.2.622572613.1620508636",
    },
)


r = requests.get(
    "https://assets.hermes.com/is/image/hermesproduct/073540CTAA_side_2?a=a&size=3000,3000&extend=300,300,300,300&align=0,1&$product_item_grid_b$=&resMode=&wid=400&hei=400",
    cookies={
        "datadome": "2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09",
        "_fbp": "fb.1.1620508611460.107273778",
        "_ga_Y862HCHCQ7": "GS1.1.1620506827.1.1.1620508634.0",
        "ECOM_SESS": "ua780gssp88sbmhnmvsfsmdlg3",
        "_gcl_au": "1.1.324567000.1620508634",
        "_cs_mk": "0.9499799337663387_1620508634146",
        "_ga": "GA1.2.365684559.1620508634",
        "ABTastySession": "mrasn=&lp=https%3A%2F%2Fwww.hermes.com%2Ffr%2Ffr%2Fcategory%2Ffemme%2Fsacs-et-petite-maroquinerie%2Fsacs-et-pochettes%2F%23%7C%7CLigne&sen=1",
        "ABTasty": "uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=",
        "_cs_c": "1",
        "_cs_id": "0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0",
        "_cs_s": "1.0",
        "_gid": "GA1.2.622572613.1620508636",
    },
    headers={
        **base_headers,
        "Host": Host_3,
        "Accept": "image/webp,*/*",
        "Referer": Referer_1,
        "Cookie": "datadome=2MYEBFQ1MQw0YtPX5j7B5urA-HUmSck1izBkru-LLhSNURxf9H3A5Uu5yubF6YYso58OaDQE-ZCbA7A7VXQAagRdRo~JlAEfI8zoKDz.09; _fbp=fb.1.1620508611460.107273778; _ga_Y862HCHCQ7=GS1.1.1620506827.1.1.1620508634.0; ECOM_SESS=ua780gssp88sbmhnmvsfsmdlg3; _gcl_au=1.1.324567000.1620508634; _cs_mk=0.9499799337663387_1620508634146; _ga=GA1.2.365684559.1620508634; ABTastySession=mrasn=&lp=https%253A%252F%252Fwww.hermes.com%252Ffr%252Ffr%252Fcategory%252Ffemme%252Fsacs-et-petite-maroquinerie%252Fsacs-et-pochettes%252F%2523%257C%257CLigne&sen=1; ABTasty=uid=en75kr5epn6qpbxw&fst=1620508634906&pst=-1&cst=1620508634906&ns=1&pvt=1&pvis=1&th=; _cs_c=1; _cs_id=0a06f4ea-99ab-a170-d6c9-0d77378fb788.1620508634.1.1620508634.1620508634.1.1654672634959.Lax.0; _cs_s=1.0; _gid=GA1.2.622572613.1620508636",
    },
)


r = requests.post(
    "https://c.contentsquare.net/events?v=10.8.6&str=153&di=226&dc=1207&fl=1208&sr=5&mdh=6887&pn=1&uu=0a06f4ea-99ab-a170-d6c9-0d77378fb788&sn=1&lv=1620508634&lhd=1620508634&hd=1620508634&pid=4384&eu=%5B%5B2%2C308129%2C320%2C48%5D%2C%5B6%2C308163%2C560%2C242%2C%22ul%23grid-results-ul%3Eli%3Aeq(0)%3Eh-grid-result-item%3Aeq(0)%3Ediv%3Aeq(0)%3Ea%3Aeq(0)%22%2C%22%22%5D%2C%5B7%2C308179%2C624%2C300%2C%22ul%23grid-results-ul%3Eli%3Aeq(0)%3Eh-grid-result-item%3Aeq(0)%3Ediv%3Aeq(0)%3Ea%3Aeq(0)%22%5D%2C%5B6%2C308180%2C624%2C300%2C%22ul%23grid-results-ul%3Eli%3Aeq(0)%3Eh-grid-result-item%3Aeq(0)%3Ediv%3Aeq(0)%3Ea%3Aeq(0)%3Ediv%3Aeq(0)%3Eh-image-resizer%3Aeq(0)%3Epicture%3Aeq(0)%3Eimg%3Aeq(0)%22%2C%22%22%5D%2C%5B7%2C308209%2C624%2C300%2C%22ul%23grid-results-ul%3Eli%3Aeq(0)%3Eh-grid-result-item%3Aeq(0)%3Ediv%3Aeq(0)%3Ea%3Aeq(0)%3Ediv%3Aeq(0)%3Eh-image-resizer%3Aeq(0)%3Epicture%3Aeq(0)%3Eimg%3Aeq(0)%22%5D%2C%5B6%2C308210%2C624%2C300%2C%22div%23carousel-item2%3Ea%3Aeq(0)%22%2C%22%22%5D%2C%5B7%2C308223%2C663%2C344%2C%22div%23carousel-item2%3Ea%3Aeq(0)%22%5D%2C%5B2%2C308532%2C655%2C334%5D%5D",
    headers={
        **base_headers,
        "Host": "c.contentsquare.net",
        "Accept": "*/*",
        "Origin": Origin_1,
        "Referer": Referer_1,
        "TE": "Trailers",
    },
)
