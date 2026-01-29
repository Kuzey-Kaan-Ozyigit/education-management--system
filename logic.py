import json

class StudentsLogic():
    def __init__(self):
        try:
            with open("students.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.number_of_students = len(data)
        except:
            self.number_of_students = 0

    def update_number_of_students(self):
        try:
            with open("students.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.number_of_students = len(data)
        except:
            self.number_of_students = 0
        return self.number_of_students

    def save_to_json(self, student_id, student_info):
        student_dict = {student_id: student_info}
        try:
            with open("students.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = {}

        data.update(student_dict)
        with open("students.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        return self.update_number_of_students()
    
    def load_json(self):
        try:
            with open("students.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = {}
        return data