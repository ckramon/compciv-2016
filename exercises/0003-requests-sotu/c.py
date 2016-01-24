import requests
resp = requests.get("www.thisdomaincannotpossiblyexist.com")
print(resp.url)