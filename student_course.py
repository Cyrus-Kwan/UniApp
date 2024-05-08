import random
import cli

class StudentCourse():
    '''
    Logged in students can access this menu to perform the following actions:

    (c) change: enables a student to change their password
    (e) enrol: Student enrols in a subject. A student can enrol in a maximum of 4 subjects
    (r) remove: Student can remove a subject from subjects' enrolment list
    (s) show: Shows the enrolled subjects and marks the grades for each subject
    (x) exit
    '''

    def __init__(self, student_id, name, email, password, subjects, marks):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects
        self.marks = marks

    def change(self):
        '''
        Changes the current student's password.
        '''
        new_password = input("Type new password:")
        self.password = new_password

    def enrol(self):
        '''
        Adds a random subject to your current list of subjects.
        You can have a maximum of up to four subjects.
        '''
        # NOTE: Subjects should be a list of subject classes
        # REFACTOR:

        # subjects variable is stored as a string in the format "<subject 1>-<subject 2>-<subject 3>"
        # Each subject should be 3 digits long between 1 and 999
        # A subject should not be duplicated in the student course list
        subject_arr = self.subjects.split()
        if len(subject_arr) >= 4:
            cli.message("Students are allowed to enrol in 4 subjects only", "red")
        else:
            new_subject = random.randint(1, 999)

            while new_subject in subject_arr:
                new_subject = random.randint(1, 999)

            subject_arr.append(str(new_subject).ljust(3, "0"))
            self.subjects = " ".join(subject_arr)
            cli.message(f"Enrolling in Subject-{new_subject}", "yellow")
            cli.message(f"You are now enrolled in {len(subject_arr)} out of 4 subjects", "yellow")

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