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

    def __init__(self, data):
        self.data = data
        cli.menu(self)

    def login(self):
        '''
        Should check a database object to see if their given email and password exist in
        the system
        '''
        email = input("Email: ")
        password = input("Password: ")

        # Line index to reference every other credential in the database object
        idx = None

        if email in self.data["email"] and password in self.data["password"]:
            idx = self.data["email"].index(email)

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

    Student(database.data)

if __name__ == "__main__":
    main()