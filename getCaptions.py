import requests


baseurl = "https://www.googleapis.com/youtube/v3/captions/"

videoID = 'S-yhk6Y3g4Q'

r = requests.get(baseurl+videoID,auth="")

print(r.text)

