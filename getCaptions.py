# import requests
#
#
# baseurl = "https://www.googleapis.com/youtube/v3/captions/"
#
# videoID = ''
#
# r = requests.get(baseurl+videoID,auth="")
#
# print(r.text)




# import requests


# link = input('Enter link of video transcript you want to use: ')
# print(link)


with open('api.txt', 'r') as f:
    API_key = f.readline()
print(API_key)

from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

youtube = build('youtube', 'v3', developerKey=API_key)
video_id = '4uEC_xibqNY'


# difference between auto-generated vs auto-translated
# 


# if the video has subtitles disabled, transcript.txt wont change.
# if the video is by default English - (not auto-translated), then ofc it works.
# if the video 


try:
    responses = YouTubeTranscriptApi.get_transcript(
        video_id, languages=['en'])
        
        
        # Note:- If captions are disabled or language is not EN(English) for a video you will get an Exception Message.
        # "No transcripts were found for any of the requested language codes: ['en']"

    
        # meaning, if auto-translation is by default English, then it will
        # still work, but if the video's auto-translation is by default Russian, 
        # say because its a video related to Russia, then 
        # it will return an error, even if there IS an auto-translation to English.
        
    
        # sometimes use en-US instead?
    print('\n'+"Video: "+"https://www.youtube.com/watch?v="+str(video_id)+'\n'+'\n'+"Captions:")
    
    with open('transcript.txt', 'w') as f:
        for response in responses:
            text = response['text']
            # print(text)
            
            f.write(text + '\n')
except Exception as e:
    print(e)
    
    
with open('transcript.txt') as open_file:
    for line in open_file:
        print(line.rstrip('\n'))


# put all info into a txt file

