def calculate_gpa(student_data):
    total_grade_points = 0
    total_sks = 0

    # Calculate total grade points and total SKS
    for course, grade in student_data[1].items():
        if grade.upper() == 'A':
            grade_point = 4.0
        elif grade.upper() == 'B':
            grade_point = 3.0
        elif grade.upper() == 'C':
            grade_point = 2.0
        elif grade.upper() == 'D':
            grade_point = 1.0
        elif grade.upper() == 'E':
            grade_point = 0.0
        else:
            # Ignore unrecognized grades
            continue

        total_grade_points += grade_point
        total_sks += 1  # Assuming each course has 1 SKS

    # Calculate GPA
    if total_sks == 0:
        return 0.0  # To avoid division by zero error
    else:
        gpa = total_sks * total_grade_points / total_sks
        return gpa

# Example data
student_data = [{'nama': 'asd', 'nim': '21.32.1311', 'semester': '3', 'Konsentrasi': 'Internet of Things'}, {'Edge_Computing': 'b', 'Elektronika_dan_Sistem_Digital': 'a', 'Jaringan_Komputer_2': 'a', 'Pemrograman_Python': 'a', 'Pemrograman_Web': 'a', 'Pendidikan_Pancasila': 'a', 'Teknologi_Sensor': 'a'}]

# Calculate GPA
gpa = calculate_gpa(student_data)
print("GPA:", gpa)
