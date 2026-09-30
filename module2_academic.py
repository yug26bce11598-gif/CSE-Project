# module2_academic.py

def process_data(marks):
    if marks < 33:
        return "F"
    elif marks >= 33 and marks <= 40:
        return "E"
    elif marks >= 41 and marks <= 60:
        return "D"
    elif marks >= 61 and marks <= 80:
        return "C"
    elif marks >= 81 and marks <= 90:
        return "B"
    elif marks > 90 and marks <= 100:
        return "A"
    else:
        return "Invalid"

def input_marks(db, reg_no, marks):
    if reg_no in db:
        if marks >= 0 and marks <= 100:
            db[reg_no]["marks"] = marks
            db[reg_no]["grade"] = process_data(marks)
            print("Success: Marks and Grade updated.")
        else:
            print("Error: Marks must be between 0 and 100.")
    else:
        print("Error: Student not found.")

def generate_report(db):
    print("\n=== ACADEMIC GRADE REPORT ===")
    count = 0
    for reg_no, data in db.items():
        if data["marks"] != -1:
            print(f"Reg No: {reg_no} | Name: {data['name']} | Marks: {data['marks']} | Grade: {data['grade']}")
            count += 1
    if count == 0:
        print("No academic data available yet.")
    print("=============================\n")
