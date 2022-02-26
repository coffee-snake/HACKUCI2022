from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

@app.route("/submittedURL",methods=["POST"])
def update_difficulty():
    global difficulty
    difficulty = string_Difficult_to_int(request.form['difficulty'])
    print(request.form['difficulty'])
    return "200"

print("testing")