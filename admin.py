from database import Database  # Assuming you have a database module with Database class

class Admin:
    '''
    Admin menu offers the following actions:

    (c) clear database file: enables admin to clear the data file "students.data"
    (g) group students: shows the students organized with respect to the subject grade
    (p) partition students: shows the pass/fail distribution
    (r) remove student: enables admin to remove a student by ID
    (s) show: show the students from the data file
    (x) exit
    '''

    def __init__(self, database):
        self.database = database
#For Clearing the entire database .
    def clear_database_file(self):
        # Open the file in write mode to clear its contents
        with open("students.data", "w") as file:
            file.write("")
        print("Database file cleared.")
#For grounping the students based on their grades
    def group_students(self):
        # Get students from the database and group them by grade
        students_by_grade = self.database.group_by_grade()
        for grade, students in students_by_grade.items():
            print(f"Grade {grade}:")
            for student in students:
                print(student)
            print()  # Add a newline for better readability
            
# For dividning the students based on they are pass/fail
    def partition_students(self):
        # Get pass/fail distribution from the database
        pass_fail_distribution = self.database.pass_fail_distribution()
        print("Pass/Fail Distribution:")
        for status, count in pass_fail_distribution.items():
            print(f"{status.capitalize()}: {count}")
            
# For removing the particular student from the database
    def remove_student(self, student_id):
        # Remove student by ID from the database
        success = self.database.remove_student(student_id)
        if success:
            print(f"Student with ID {student_id} removed successfully.")
        else:
            print(f"Student with ID {student_id} not found in the database.")

# For showing the list of all the students.
    def show(self):
        # Show all students from the database
        students = self.database.get_all_students()
        print("All Students:")
        for student in students:
            print(student)

def main():
    # Initialize the database
    database = Database()  # You need to define the Database class and its methods
    admin = Admin(database)

    while True:
        print("\nAdmin Menu:")
        print("(c) Clear Database File")
        print("(g) Group Students")
        print("(p) Partition Students")
        print("(r) Remove Student")
        print("(s) Show Students")
        print("(x) Exit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "c":
            admin.clear_database_file()
        elif choice == "g":
            admin.group_students()
        elif choice == "p":
            admin.partition_students()
        elif choice == "r":
            student_id = input("Enter student ID to remove: ").strip()
            admin.remove_student(student_id)
        elif choice == "s":
            admin.show()
        elif choice == "x":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
