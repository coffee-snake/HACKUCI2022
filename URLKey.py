import re

def getURLkey(URL):
    youtube_url = str(URL)

    regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
    match = regex.match(youtube_url)

    if match:
        start = youtube_url.find("v=") + len("v=")
        end = youtube_url.find("&")
        key = youtube_url[start:end]

        return key

    if not match:
        not_match = -1
        return not_match
