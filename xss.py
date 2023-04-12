import requests
import re

url = input("Enter URL: ")
response = requests.get(url)
paths = re.findall(r'href="([^"]+)"', response.text)
for path in paths:
    response = requests.get(url + "/" + path)
    if "<script>" in response.text:
        print(f"XSS vulnerability detected: {url}/{path}")
