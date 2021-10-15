from libs.utils import base_headers
import requests
# from libs.sms_receive import receive_msg

def send_sms_code(url,code):
    # code = receive_msg(number).strip()
    print(f"code is {code}, sending code info")
    print(url)
    send_sms_response = requests.post(
            url,
            headers={
                **base_headers,
                "Host": "rendezvousparis.hermes.com",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                
            },
            data={"sms_code": code}
        )
    print(send_sms_response)
    # print(send_sms_response.text)
    if send_sms_response.status_code == 200 and "Your request for a Leather Goods appointment has been registered" in send_sms_response.text:
        return True
    