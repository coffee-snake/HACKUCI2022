from flask import Flask
from flask import request
from flask_cors import CORS
import URLKey
import getCaptions
import getSummary
import getZoomText
from random import randint
from tryyuja import getYujaText


app = Flask(__name__)
CORS(app)

fullString = ""

@app.route("/")
def landing_page():
    index_html = ""
    with open("test.html") as file:
        index_html ="\n".join(file.readlines())
    return index_html


@app.route("/getFullStrings")
def hello_world():
    return f"<html><body><p>{fullString}</p></body></html>"

@app.route("/sendURL",methods=["POST"])
def sendURL():
    global fullString
    apiKey2 = ""
    with open("api.txt","r") as f:
        apiKey2=f.readlines()[1]
    if("you" in request.form['videoTitle']):
        VID = URLKey.getURLkey(request.form['videoTitle'])
        print(VID)
        if VID==-1:
            return "6969"
        
        fullTranscript = getCaptions.transcripter(VID)
        if(fullTranscript==-1):
            return "6969"
        fullString = fullTranscript



        shortSummary = getSummary.get_summary(apiKey2,f"https://21fa-169-234-19-252.ngrok.io/getFullStrings?v={randint(1,9999)}")
       
        if(shortSummary==-1):
            return "69420"
        
        return shortSummary



    if("zoom" in request.form['videoTitle']):
        fullString = getZoomText.getZoomText(request.form['videoTitle'])
        if(type(fullString)==int and fullString<0):
            return fullString
        shortSummary = getSummary.get_summary(apiKey2,"https://21fa-169-234-19-252.ngrok.io/getFullStrings?v={randint(1,9999)}")

        if(shortSummary==-1):
            return "69420"
        return shortSummary

    if("yuja" in request.form['videoTitle']):
        fullString = getYujaText(request.form['videoTitle'])
        shortSummary = getSummary.get_summary(apiKey2,"https://21fa-169-234-19-252.ngrok.io/getFullStrings?v={randint(1,9999)}")

        return shortSummary
    return "6969"


