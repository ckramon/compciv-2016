import requests
resp = requests.get("http://www.thisdomaincannotpossiblyexist.com")
print(resp.url)
