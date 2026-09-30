# module1_crud.py

def create_student(db, reg_no, name, branch):
    if reg_no in db:
        print("Error: Student with this Registration Number already exists!")
        return
    db[reg_no] = {"name": name, "branch": branch, "marks": -1, "grade": "N/A"}
    print("Success: Student created.")

def read_student(db, reg_no):
    if reg_no in db:
        student = db[reg_no]
        print(f"\n--- Student Details ---")
        print(f"Reg No: {reg_no}\nName: {student['name']}\nBranch: {student['branch']}")
        if student['marks'] != -1:
            print(f"Marks: {student['marks']}\nGrade: {student['grade']}")
        print("-----------------------")
    else:
        print("Error: Student not found.")

def update_student(db, reg_no, new_name, new_branch):
    if reg_no in db:
        if new_name != "":
            db[reg_no]["name"] = new_name
        if new_branch != "":
            db[reg_no]["branch"] = new_branch
        print("Success: Student updated.")
    else:
        print("Error: Student not found.")

def delete_student(db, reg_no):
    if reg_no in db:
        del db[reg_no]
        print("Success: Student deleted.")
    else:
        print("Error: Student not found.")