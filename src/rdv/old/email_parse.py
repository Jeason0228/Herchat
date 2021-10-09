from imapclient import IMAPClient
import email
from bs4 import BeautifulSoup

# context manager ensures the session is cleaned up
imap_query_start = u"("
imap_query_end = ")"
imap_query=""
from_person = "no-reply@hermes.com"
to_person = "penghanyuan@gmail.com"
from_date = None
to_date = None
failed_text = "In view of the high number of requests for appointments, we are extremely sorry that we were not able to fulfill your request this time. We invite you to repeat your request at another date."


with IMAPClient(host="imap.gmail.com") as client:
    client.login('herchat.server@gmail.com', 'ParisHerchat123!')
    client.select_folder('INBOX')
    
    # search criteria are passed in a straightforward way
    # (nesting is supported)
    if from_person:
        imap_query += 'FROM {}'.format(from_person)
    if to_person:
        imap_query += ' TO {}'.format(to_person)
    if from_date:
        imap_query += ' SINCE {}'.format(from_date)
    if to_date:
        imap_query += ' BEFORE {}'.format(to_date)

    imap_query = "{}{}{}".format(imap_query_start, imap_query, imap_query_end)

    messages = client.search(imap_query)

    # fetch selectors are passed as a simple list of strings.
    response = client.fetch(messages, ['FLAGS', 'RFC822', 'BODY[TEXT]'])

    # `response` is keyed by message id and contains parsed,
    # converted response items.
    for message_id, data in response.items():
        # print('{id}: {size} bytes, flags={flags}'.format(
        #     id=message_id,
        #     size=data[b'RFC822'],
        #     flags=data[b'FLAGS']))
        email_message = email.message_from_bytes(data[b"RFC822"])
        # print(message_id, email_message.get("From"), email_message.get("Subject"))
        payload = email_message.get_payload(decode=True)
        strtext = payload.decode()
        soup = BeautifulSoup(strtext)
        numbers = soup.find_all("h4", attrs={"class": "number-boxes-itemm-number"})
        print((failed_text in strtext))