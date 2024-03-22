import calculate.data as data

def semester():
    # Your semester data goes here as defined earlier

# Function to map grades to grade points
    def map_grade_to_points(grade):
        grade_points_map = {'a': 4.00, 'b': 3.00, 'c': 2.00, 'd': 1.00, 'e': 0.00}
        return grade_points_map.get(grade.lower(), 0.00)

# Function to calculate GPA
    def calculate_ipk(user_grades):
        data = semester()
        total_weighted_points = 0
        total_sks = 0

        for semester_data in data["data"]:
            for course_data in semester_data["data"]:
                sks = course_data["sks"]
                total_sks += sks
                course_name = course_data["name"]
                user_input = user_grades.get(course_name)
                if user_input is not None:
                    total_weighted_points += (map_grade_to_points(user_input) * sks)

        if total_sks == 0:
            return "No courses found."
        else:
            ipkEnd = total_weighted_points / total_sks
            return ipkEnd

def test():
    return data.semester()
