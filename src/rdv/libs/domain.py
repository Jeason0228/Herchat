import requests



rdv_response = requests.get(
                "https://api.freenom.com/v2/domain/search?domainname=idqs.ml&domaintype=FREE",

            )

print(rdv_response.json)