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


def getKey():
    '''
    Accesses api.txt to open the file with the api key
    '''
    with open('api.txt', 'r') as f:
        API_key = f.readline()
    return API_key


def transcripter(video_id):
    '''
    Transcripts the video, return a string or maybe transcript.txt given the video_id
    '''
    youtube = build('youtube', 'v3', developerKey=getKey())
    try:
        responses = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['en', 'en-CA'])
        print(responses)
        
        '''
        Note: If captions are disabled or language is not EN(English) for a video you may get an Exception Message.
        "No transcripts were found for any of the requested language codes: ['en']"
        meaning, if auto-translation is by default English, then it will
        still work, but if the video's auto-translation is by default Russian, 
        it will return an error, even if there is an auto-translation to English.
        
        Sometimes with videos with manual subtitles, it will still return the auto-translated version, and sometimes not. 
        '''
        
        print('\n'+"Video: "+"https://www.youtube.com/watch?v="+str(video_id)+'\n'+'\n'+"Captions:")
        
        # with open('transcript.txt', 'w') as f:
        long_string = ''
        flag = False
        responses[0]['text'] = responses[0]['text'].capitalize()  # first sentence
        
        for response in responses:
            text = response['text']
            # print(text)
            
            if flag:
                text = text.capitalize()
                flag = False
            
            if len(text) < 30:
                if '.' not in text:  # conditions for adding punctuation, ignoring manual transcripts
                    if '?' not in text:
                        if ',' not in text:
                            long_string += text + '.\n'
                            flag = True  # need to capitalize after every period.
                            # f.write(text + '.\n')
            
            else:
                long_string += text + '\n'
                # f.write(text + '\n')
        return long_string
                    
    except Exception as e:
        print(e)
        return -1


# def display_transcript():
#     '''
#     Displays the transcript as it is written in transcript.txt
#     '''
#     with open('transcript.txt') as open_file:
#         for line in open_file:
#             print(line.rstrip('\n'))


if __name__ == '__main__':
    video_id = 'xICkLB3vAeU'
    subtitle = transcripter(video_id)
    # print('type: ', type(subtitle))
    # print()
    print(subtitle)
    

