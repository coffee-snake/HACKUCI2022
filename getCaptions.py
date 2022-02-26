import requests

baseurl = "https://www.googleapis.com/youtube/v3/captions/"

videoID = ''

r = requests.get(baseurl+videoID,auth="")
print(r.text)

