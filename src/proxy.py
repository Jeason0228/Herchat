import requests    
proxy="http:35.181.50.135:3128"
html = requests.get("https://api.ipify.org/", proxies={"http":proxy}, timeout=5)  
print(html.content.decode('latin-1'))