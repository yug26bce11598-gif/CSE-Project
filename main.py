# main.py
import module1_crud
import module2_academic
import module3_storage

def main():
   
    student_db = module3_storage.load_data()

    while True:
        print("\n--- Student Management System ---")
        print("1. Create Student")
        print("2. Read Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Input Marks & Generate Grade")
        print("6. Generate Academic Report")
        print("7. Save Data")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            reg = input("Enter Registration No: ")
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            module1_crud.create_student(student_db, reg, name, branch)
        
        elif choice == '2':
            reg = input("Enter Registration No to read: ")
            module1_crud.read_student(student_db, reg)
            
        elif choice == '3':
            reg = input("Enter Registration No to update: ")
            name = input("Enter new Name (leave blank to keep current): ")
            branch = input("Enter new Branch (leave blank to keep current): ")
            module1_crud.update_student(student_db, reg, name, branch)
            
        elif choice == '4':
            reg = input("Enter Registration No to delete: ")
            module1_crud.delete_student(student_db, reg)
            
        elif choice == '5':
            reg = input("Enter Registration No: ")
            try:
                marks = float(input("Enter marks obtained (0-100): "))
                module2_academic.input_marks(student_db, reg, marks)
            except ValueError:
                print("Error: Please enter a valid number for marks.")
                
        elif choice == '6':
            module2_academic.generate_report(student_db)
            
        elif choice == '7':
            module3_storage.save_data(student_db)
            
        elif choice == '8':
            module3_storage.save_data(student_db)
            print("Exiting Program. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please select between 1 and 8.")

if __name__ == "__main__":
    main()