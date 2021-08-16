from utils import base_headers
from sms_code import send_sms_code
import requests
from recaptcha import g_response
from webdriver_manager.chrome import ChromeDriverManager

def send_rdv_infos(person):

    captcha_response = g_response()
    # captcha_response = 0
    form_json = {
        "check": "",
        "_csrf": "eoLUX36a-miwJVoErMEUZO_l2r97FxxUwRvI",
        "prefer": person["prefer"],
        "surname": person["surname"],
        "name": person["name"],
        "phone_country": person["phone_country"],
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
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                
            },
            data=form_json
        )

    _redirect_url = rdv_response.url
    print(_redirect_url)
    if rdv_response.status_code == 200:
        return _redirect_url
    else:
        raise Exception("Error when sending the rdv info.")

