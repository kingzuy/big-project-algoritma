from flask import Flask, render_template, redirect, session, url_for, request
import json
import calculate.data as modul
from calc import ipk as sum_ipk

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET'])
def index():
    title = "WXP | Hoop Full"
    return render_template('index.html', title=title)

@app.route('/calculate', methods=['GET'])
def calculate():
    title  = "WXP | Hoop Full"
    return render_template('calculating.html', title=title)

@app.route('/calculate', methods=['POST'])
def calculate_post():
    # data = request.form
    # json_data = json.dumps(data, indent=4)
    # return json_data

    data = request.form

    data_mata_kuliah = {}
    for key, value in data.items():
        if key != "nama" and key != "nim" and key != "semester":
            data_mata_kuliah[key] = value

    data_mahasiswa = {
        "nama": data.get("nama", ""),
        "nim": data.get("nim", ""),
        "semester": data.get("semester", ""),
    }

    session['data'] = ([data_mahasiswa, data_mata_kuliah])
    return redirect(url_for('result'))

@app.route('/result', methods=['GET'])
def result():
    data = session.get('data', None)
    # Menyusun data yang diubah
    personal_info = data[0]
    academic_info = data[1]

    # Memindahkan 'Konsentrasi' ke dalam dictionary personal_info
    personal_info['Konsentrasi'] = academic_info.pop('Konsentrasi', '')

    # Hasil akhir
    ipk = sum_ipk(personal_info,academic_info)
    processed_data = [personal_info, academic_info, ipk]
    
    return render_template('result.html', data=processed_data)

@app.route('/data', methods=['GET'])
def data():
    data = modul.semester()
    json_data = json.dumps(data, indent=4)
    return json_data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True, use_reloader=False)
