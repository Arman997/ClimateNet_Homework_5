from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("main.html")
@app.route("/Cli_ip", methods=['GET'])
def get_IP():
    data_url = requests.get('https://emvnh9buoh.execute-api.us-east-1.amazonaws.com/getData?device_id=14&start_time=2025-03-15&end_time=2025-03-16')
    data = json.loads(data_url.content)   
    print(data["keys"])
    return render_template("getIp.html", newdata=data)

if __name__ == '__main__':
    app.run(debug = True, host= '0.0.0.0', port=8000)
