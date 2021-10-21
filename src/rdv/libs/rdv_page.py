from libs.utils import base_headers
from libs.sms_code import send_sms_code
import requests
from libs.recaptcha import g_response
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_csrf():
    rdv_response = requests.get(
            "https://rendezvousparis.hermes.com/client/register",
            headers={
                **base_headers,
                "Host": "rendezvousparis.hermes.com",
                
            }
            # cookies={"_csrf":"eoLUX36a-miwJVoErMEUZO_l2r97FxxUwRvI"}
        )
    soup = BeautifulSoup(rdv_response.content, "html.parser")
    csrf = soup.find("input", {"name":"_csrf"}).get("value")
    print(csrf)
    return csrf
    # print(type(soup.))

def send_rdv_infos(person):

    captcha_response = g_response()
    # captcha_response = 0
    print(captcha_response)
    if captcha_response == 0:
        print("Captcha error.")
        return False
    else:
        form_json = {
            "check": "",
            "_csrf": get_csrf(),
            "prefer": person["prefer"],
            "surname": person["surname"],
            "name": person["name"],
            "phone_country": "FR",
            "phone_number": person["phone_number"],
            "email": person["email"],
            "passport_id": person["passport_id"],
            "cgu": "on",
            "processing": "on",
            "g-recaptcha-response": captcha_response,
        }

        rdv_response = requests.post(
                "https://rendezvousparis.hermes.com/client/register",
                headers={
                    **base_headers,
                    "Host": "rendezvousparis.hermes.com",
                    "Origin": "https://rendezvousparis.hermes.com",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Refer":"https://rendezvousparis.hermes.com/client/register",
                    "Cookie": "i18next=en; _csrf=fvD60KKcducZ1P1HRXemiv-D; policy=accepted; app=eyJmbGFzaCI6e30sImNhY2hlZmxhc2giOltdLCJhcHBvaW50bWVudF9jb2RlIjoiWjdIRkY5IiwiYmxvY2tfcmVnaXN0cmF0aW9uIjpmYWxzZX0=; app.sig=ru86sjE37_711oHA3v0-W6KI9hg"
                },
                data=form_json,
                # cookies={"_csrf":"eoLUX36a-miwJVoErMEUZO_l2r97FxxUwRvI"}
            )

        _redirect_url = rdv_response.url
        print(rdv_response.status_code)
        # print(rdv_response.text)
        # print(_redirect_url)

        if rdv_response.status_code == 200:
            return _redirect_url
        else:
            raise Exception("Error when sending the rdv info.")
