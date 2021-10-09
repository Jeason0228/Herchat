# Code in Python
import time
import requests
import json
import re


def get_verification_code(email):
    # We want to get account validation code in email
    validation_code = None
    # We will retry the request every 6 seconds to get the email
    for i in range(2):
        # Get emails from an email box
        req = requests.get(f'https://snapmail.cc/emaillist/{email}?isPrefix=True')
        if req.status_code == 200:
            # Get email text of the first email,
            # take "This is a test email." for example,
            # email_text = "This is a test email."
            email_text = json.loads(req.text)[0]['subject']
            print(email_text)
            # Use regex to get the validation code, we'll get "test" here.
            # validation_code = "test"
            validation_code = re.search(r'This is a ([a-zA-Z0-9]{4}) email', email_text)
            break

        print("Waiting for next retry")
        time.sleep(6)
    if validation_code:
        print('validation_code:' + validation_code.group(1))
        return validation_code.group(1)


get_verification_code('kutauz@snapmail.cc')
