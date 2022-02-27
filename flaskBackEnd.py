from flask import Flask
from flask import request
from flask_cors import CORS
import URLKey
import getCaptions


app = Flask(__name__)
CORS(app)

fullString = ""

@app.route("/getFullString")
def hello_world():
    return f"<p>{fullString}</p>"

@app.route("/sendURL",methods=["POST"])
def sendURL():
    VID = URLKey.getURLkey(request.form['videoTitle'])
    if VID==-1:
        return "6969"
    
    fullTranscript = getCaptions.transcripter(VID)
    if(fullTranscript==-1):
        return "6969"
    

    global fullString
    fullString = fullTranscript
    return fullTranscript


