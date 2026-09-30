# module3_storage.py

def save_data(db, filename="student_db.txt"):
    file = open(filename, "w")
    for reg_no, data in db.items():
        line = str(reg_no) + "," + str(data["name"]) + "," + str(data["branch"]) + "," + str(data["marks"]) + "," + str(data["grade"]) + "\n"
        file.write(line)
    file.close()
    print("Success: Data saved to file.")

def load_data(filename="student_db.txt"):
    db = {}
    try:
        file = open(filename, "r")
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 5:
                reg_no = parts[0]
                db[reg_no] = {
                    "name": parts[1],
                    "branch": parts[2],
                    "marks": float(parts[3]),
                    "grade": parts[4]
                }
        file.close()
        print("Success: Data loaded from file.")
    except FileNotFoundError:
        print("Notice: No previous data found. Starting fresh database.")
    return db