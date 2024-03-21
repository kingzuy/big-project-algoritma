from flask import Flask, render_template, redirect, url_for, request
import json
import calculate.data as modul

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    title = "WXP | Hoop Full"
    return render_template('index.html', title=title)

@app.route('/calculate', methods=['GET'])
def calculate():
    title  = "WXP | Hoop Full"
    return render_template('calculating.html', title=title)

@app.route('/data', methods=['GET'])
def data():
    data = modul.semester()
    json_data = json.dumps(data, indent=4)
    return json_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
