from database import Database

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
        registered student should login. Upon login, students’ data should be read from
        “students.data”. After login, a student goes to Student Course Menu that offers the choices:
    '''

    def __init__(self, name, email, password, subjects):
        self.student_id = self.generate_id()
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects

    def login(self):
        pass

    def register(self):
        pass

    def generate_id(self):
        pass

def main():
    test = Student("Harry", "email", "password", ["123"])
    print(test.__doc__)

if __name__ == "__main__":
    main()