from database import Database
from student_course import StudentCourse
import cli
import random

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

    def __init__(self, database):
        self.database = database
        cli.menu(self)

    def login(self):
        '''
        Should check a database object to see if their given email and password exist in
        the system
        '''
        # Sub-menu title:
        cli.message("Student Sign In", "green")

        email = input("Email: ")
        password = input("Password: ")

        # Line index to reference every other credential in the database object
        idx = None

        if self._in_data(email, password):
            idx = self.database.data["email"].index(email)

            # Instantiate new student course
            student_id = self.database.data["student_id"][idx]
            name = self.database.data["name"][idx]
            email = self.database.data["email"][idx]
            password = self.database.data["password"][idx]
            subjects = self.database.data["subjects"][idx]
            marks = self.database.data["marks"][idx]

            student_session = StudentCourse(
                student_id, 
                name, 
                email, 
                password, 
                subjects, 
                marks,
                )
            
            # Menu to perform operations on specific student
            session_state = cli.menu(student_session)

            # Updates data from specific student into the data in memory
            for key in session_state.keys():
                self.database.data[key][idx] = session_state[key]

            # Writes data in memory to file
            self.database.update_file()
        else:
            cli.error("Incorrect email or password.")

    def register(self):
        '''
        Should check a database object to see if their given email and password exists in the system
        If it does, notify the user that they can already log in
        If it doesn't, check if the inputed email and password are valid
        If all input is valid, create a new student with no subjects in the database object
        '''
        # Sub-menu title
        cli.message("Student Sign Up", "green")
        pass

    def _generate_id(self):
        '''
        Check the database object for all IDs
        Create a random 6 digit ID that is NOT already listed in the existing IDs
        IDs that are less than 6 digits should be padded with 0's from the left
        '''
        id_arr = {int(id) for id in self.database.data["student_id"]}
        id_range = set(range(1,999999))
        valid_range = id_range-id_arr
        new_id = random.choice(valid_range)
        
        return str(new_id).ljust(6, "0")

    def _in_data(self, email, password):
        return email in self.database.data["email"] and password in self.database.data["password"]

def main():
    DATAFILE = "student.data"
    database = Database(filepath=DATAFILE)

    Student(database)

if __name__ == "__main__":
    main()