from calculate.data import semester

def ipk(personal_info, academic_info) :
    data = semester()
    data2 = academic_info
    input_semester = personal_info['semester']
    konsentrasi = personal_info['Konsentrasi']
    grands = grand(data2) 
    a = []
    main_data = []
    cyber_data = ""
    iot_data = ""
    
    #memisah data
    for semester_data in data["data"]:
        if semester_data["semester"] == input_semester:
            a.append(semester_data['data'])
    
    for i in a[0]:
        if i['name'] != "Konsentrasi" :
            main_data.append(i)
        else :
            second_data = [i['data']]    
            cyber_data = second_data[0][0]['data']
            iot_data = second_data[0][1]['data']
            
    #end
    ipk = sum_ipk(main_data, cyber_data, iot_data, grands, konsentrasi)
    #sumipk
            
    return ipk
    
def sum_ipk(main, cyber, iot, grands, konsentrasi):
    if konsentrasi == "Cyber Security":
        main.extend(cyber)
    elif konsentrasi == "Internet of Things":
        main.extend(iot)
    
    total_ipk = sum(int(item['sks']) * grands[item['name']] for item in main)
    
    total_sks = sum(int(item['sks']) for item in main)
    
    result = round(total_ipk / total_sks, 2)
    
    data = {"total_ipk" : total_ipk, "total_sks" : total_sks, "rata_rata" : result}

    return data
        
    
def grand(data):

    grade_map = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

    scored_grades = {key.replace("_", " "): grade_map[value.upper()] for key, value in data.items()}

    return scored_grades

if __name__ == "__main__":
    ipk()
