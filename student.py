from database import Database
from student_course import StudentCourse

import cli

class Student():
    '''
    The student menu system should enable students to Login and Register as follows:

    (l) login
    (r) register
    (x) exit

    Register:
        Students should be able to register. Email and password should be verified against pattern 
        rules. Then the student should be checked if they exist. Only register students that do not 
        exist in the Database file. On registration, student data should be stored in “students.data”.

    Login:
        Students should be able to login. Then the student should be checked if they exist. Only a 
        registered student should login. Upon login, students data should be read from
        “students.data”. After login, a student goes to Student Course Menu that offers the choices:
    '''

    def __init__(self, database:Database):
        self.database = database
        cli.menu(self)

    def login(self) -> None:
        '''
        Should check a database object to see if their given email and password exist in
        the system
        '''
        email = input("Email: ")
        password = input("Password: ")

        # Line index to reference every other credential in the database object
        student_index = None
        students = self.database.data

        for i, student in enumerate(students):
            if (email == student["email"]) and (password == student["password"]):
                student_index = i
                break

        try:
            student_session = StudentCourse(
                    students[student_index]["student_id"],
                    students[student_index]["name"],
                    students[student_index]["email"],
                    students[student_index]["password"],
                    students[student_index]["subjects"],
                    students[student_index]["marks"],
            )
        except IndexError:
            cli.error("Incorrect email or password.")
            return None
                
        # Menu to perform operations on specific student
        session_state = cli.menu(student_session)

        updated_student = {
            "student_id":session_state["student_id"],
            "name":session_state["name"],
            "email": session_state["email"],
            "password": session_state["password"],
            "subjects": " ".join((str(subject.subject_id) for subject in session_state["subjects"])),
            "marks": " ".join((str(subject.mark) for subject in session_state["subjects"])),
            }

        # Replaces student at index with a student map
        self.database.write_data(updated_student, student_index)
            
        # Writes data in memory to file
        self.database.update_file()

    def register(self):
        '''
        Should check a database object to see if their given email and password exists in the system
        If it does, notify the user that they can already log in
        If it doesn't, check if the inputed email and password are valid
        If all input is valid, create a new student with no subjects in the database object
        '''
        pass

    def _generate_id(self):
        '''
        Check the database object for all IDs
        Create a random 6 digit ID that is NOT already listed in the existing IDs
        IDs that are less than 6 digits should be padded with 0's from the left
        '''
        pass

def main():
    DATAFILE = "student.data"
    database = Database(filepath=DATAFILE)

    Student(database)

if __name__ == "__main__":
    main()