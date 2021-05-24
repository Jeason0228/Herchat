base_headers = {
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
}

r = requests.get(
    "https://bck.hermes.com/products?locale=fr_fr&category=WOMENBAGSBAGSCLUTCHES&sort=relevance",
    cookies={
        "datadome": "AOZkyHD6zB.rPGwQLB2C.LQA7DEAXcZL8ySKY9cuo6ZzL.WHC0m2NVUw.gcUsop5Tlm7Zi5Ri~8f70XzntljYpx-CPKEjN92Pl7kw6KxbP"
    },
    headers={
        **base_headers,
        ":method": "GET",
        ":authority": "bck.hermes.com",
        ":scheme": "https",
        ":path": "/products?locale=fr_fr&category=WOMENBAGSBAGSCLUTCHES&sort=relevance",
        "cache-control": "max-age=0",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6",
        "cookie": "datadome=AOZkyHD6zB.rPGwQLB2C.LQA7DEAXcZL8ySKY9cuo6ZzL.WHC0m2NVUw.gcUsop5Tlm7Zi5Ri~8f70XzntljYpx-CPKEjN92Pl7kw6KxbP",
    },
)


r = requests.get(
    "https://bck.hermes.com/favicon.ico",
    cookies={
        "datadome": "R2h6G.gZpaUkPUMX~FJ043hXQeiYAxkubgtT8g9pWfsgYzLW.4DUtYiwrh2otz7auef7y217oy_~4oOy6c9UPzHz1ai4hF9SMua7QRt2Zp"
    },
    headers={
        **base_headers,
        ":method": "GET",
        ":authority": "bck.hermes.com",
        ":scheme": "https",
        ":path": "/favicon.ico",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-dest": "image",
        "referer": "https://bck.hermes.com/products?locale=fr_fr&category=WOMENBAGSBAGSCLUTCHES&sort=relevance",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6",
        "cookie": "datadome=R2h6G.gZpaUkPUMX~FJ043hXQeiYAxkubgtT8g9pWfsgYzLW.4DUtYiwrh2otz7auef7y217oy_~4oOy6c9UPzHz1ai4hF9SMua7QRt2Zp",
    },
)


r = requests.get(
    "https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,100i,200i,300i,400i,500i",
    headers={
        **base_headers,
        "Referer": "",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    },
)


# These variables probably come from the result of the request above
Referer_1 = "https://fonts.googleapis.com/"


r = requests.get(
    "https://fonts.gstatic.com/s/roboto/v27/KFOlCnqEu92Fr1MmSU5fBBc4AMP6lQ.woff2",
    headers={
        **base_headers,
        "Referer": Referer_1,
        "Origin": "https://bck.hermes.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    },
)


r = requests.get(
    "https://fonts.gstatic.com/s/roboto/v27/KFOmCnqEu92Fr1Mu4mxKKTU1Kg.woff2",
    headers={
        **base_headers,
        "Referer": Referer_1,
        "Origin": "https://bck.hermes.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    },
)


r = requests.get(
    "https://fonts.gstatic.com/s/roboto/v27/KFOlCnqEu92Fr1MmEU9fBBc4AMP6lQ.woff2",
    headers={
        **base_headers,
        "Referer": Referer_1,
        "Origin": "https://bck.hermes.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    },
)
