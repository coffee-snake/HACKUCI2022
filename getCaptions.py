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


from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi


'''
Test Scenarios:
if the video has subtitles disabled, transcript.txt wont change.
if the video is by default English - (not auto-translated), then ofc it works.
if the video 
'''


# # attempt to force auto-translating every video to english
# transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
# transcript = transcript_list.find_transcript(['en'])
# translated_transcript = transcript.translate('en')
# print(translated_transcript.fetch())


def getKey():
    '''
    Accesses api.txt to open the file with the api key
    '''
    with open('api.txt', 'r') as f:
        API_key = f.readline()
    return API_key


def transcripter(video_id):
    '''
    Transcripts the video into transcript.txt given the video_id
    '''
    youtube = build('youtube', 'v3', developerKey=getKey())
    try:
        responses = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['en'])
        '''
        Note:- If captions are disabled or language is not EN(English) for a video you will get an Exception Message.
        "No transcripts were found for any of the requested language codes: ['en']"
        meaning, if auto-translation is by default English, then it will
        still work, but if the video's auto-translation is by default Russian, 
        say because its a video related to Russia, then
        it will return an error, even if there IS an auto-translation to English.
        '''
        print('\n'+"Video: "+"https://www.youtube.com/watch?v="+str(video_id)+'\n'+'\n'+"Captions:")
        
        with open('transcript.txt', 'w') as f:
            for response in responses:
                text = response['text']
                # print(text)
                
                if len(text) < 30:
                    # print(text)
                    if '.' not in text:  # conditions for adding punctuation, ignoring manual transcripts
                        if '?' not in text:
                            if ',' not in text:
                                f.write(text + '.\n')
                
                # after every time you add . capitalize the next letter. 
                # and capitalize the beginning letter. 
                
                else:
                    f.write(text + '\n')
    except Exception as e:
        print(e)


def display_transcript():
    '''
    Displays the transcript as it is written in transcript.txt
    '''
    with open('transcript.txt') as open_file:
        for line in open_file:
            print(line.rstrip('\n'))


if __name__ == '__main__':
    video_id = 'yYWvUoN4yt8'
    transcripter(video_id)

