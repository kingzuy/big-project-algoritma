from data import semester

def hitung_ipk(nilai_sks):
    total_sks = 0
    total_nilai = 0
    for nilai, sks in nilai_sks:
        total_sks += sks
        total_nilai += nilai * sks
    if total_sks == 0:
        return 0
    return total_nilai / total_sks

def ambil_data_sks(data_semester):
    nilai_sks = []
    for sem in data_semester:
        if "data" in sem:
            for mata_kuliah in sem["data"]:
                if "data" in mata_kuliah:
                    for spesialisasi in mata_kuliah["data"]:
                        for kurs in spesialisasi["data"]:
                            if "sks" in kurs:
                                nilai_sks.append((int(kurs["sks"]), 0))  # Konversi sks ke integer
                            else:
                                print(f"Error: 'sks' tidak ditemukan di {kurs}")
                else:
                    if "sks" in mata_kuliah:
                        nilai_sks.append((int(mata_kuliah["sks"]), 0))  # Konversi sks ke integer
                    else:
                        print(f"Error: 'sks' tidak ditemukan di {mata_kuliah}")
        else:
            print(f"Error: 'data' tidak ditemukan di semester {sem}")
    return nilai_sks

def main():
    data = semester()
    data_semester = data["data"]
    print(data_semester[3]['data'][0])
    # print(data_semester[3]['data'][0]['data'][0]) //Konsentrasi Cyber Security
    # print(data_semester[3]['data'][0]['data'][1]) //Konsentrasi IOT
    print(data_semester[3]['data'][1]['name'])
    print('========================')
    nilai_sks = ambil_data_sks(data_semester)
    ipk = hitung_ipk(nilai_sks)
    print(f"IPK: {ipk:.2f}")

if __name__ == "__main__":
    main()
