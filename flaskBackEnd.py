from flask import Flask
from flask import request
from flask_cors import CORS
import URLKey
import getCaptions
import getSummary
import getZoomText


app = Flask(__name__)
CORS(app)

fullString = ""

@app.route("/")
def landing_page():
    index_html = ""
    with open("test.html") as file:
        index_html ="\n".join(file.readlines())
    return index_html


@app.route("/getFullString")
def hello_world():
    return f"<html><body><p>{fullString}</p></body></html>"

@app.route("/sendURL",methods=["POST"])
def sendURL():
    if("you" in request.form['videoTitle']):
        VID = URLKey.getURLkey(request.form['videoTitle'])
        print(VID)
        if ID==-1:
            return "6969"
        
        fullTranscript = getCaptions.transcripter(VID)
        if(fullTranscript==-1):
            return "6969"
        

        global fullString
        fullString = fullTranscript

        apiKey2 = ""
        with open("api.txt","r") as f:
            apiKey2=f.readlines()[1]

        shortSummary = getSummary.get_summary(apiKey2,"https://bdee-169-234-19-252.ngrok.io/getFullString")

        if(shortSummary==-1):
            return "69420"
        
        return shortSummary
    if("zoom" in request.form['videoTitle']):
        getZoomText.getZoomText(request.form['videoTitle'])
    return "6969"


