from flask import Flask, render_template, redirect, session, url_for, request
import json
import calculate.calculate as calc
import calculate.data as modul

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET'])
def index():
    title = "WXP | Hoop Full"
    return render_template('calculating.html', title=title)

@app.route('/calculate', methods=['POST'])
def calculate_post():
    data = request.form

    data_mata_kuliah = {}
    for key, value in data.items():
        if key != "nama" and key != "nim" and key != "semester":
            data_mata_kuliah[key] = value

    data_mahasiswa = {
        "nama": data.get("nama", ""),
        "nim": data.get("nim", ""),
        "semester": data.get("semester", "")
    }

    return ([data_mahasiswa, data_mata_kuliah])



@app.route('/data', methods=['GET'])
def data():
    data = modul.semester()
    json_data = json.dumps(data, indent=4)
    return json_data

@app.route('/test', methods=['GET'])
def test():
    data = calc.test()
    json_data = json.dumps(data, indent=4)
    return json_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
