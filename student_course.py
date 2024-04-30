class StudentCourse():
    '''
    Logged in students can access this menu to perform the following actions:

    (c) change: enables a student to change their password
    (e) enrol: Student enrols in a subject. A student can enrol in a maximum of 4 subjects
    (r) remove: Student can remove a subject from subjects' enrolment list
    (s) show: Shows the enrolled subjects and marks the grades for each subject
    (x) exit
    '''

    def __init__(self, id, name, email, password, subjects, marks):
        self.id = None
        self.name = None
        self.email = None
        self.password = None
        self.subjects = []
        self.marks = []

    def change(self):
        '''
        Changes the current student's password.
        '''
        pass

    def enrol(self):
        '''
        Adds a random subject to your current list of subjects.
        You can have a maximum of up to four subjects.
        '''
        pass

    def remove(self):
        '''
        Removes the specified subject from the current student's subject list.
        '''
        pass

    def show(self):
        '''
        Prints the student's currently enrolled subjects to the terminal.
        '''
        pass

def main():
    pass

if __name__ == "__main__":
    main()