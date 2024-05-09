import cli

from utils import Utils
from subject import Subject

class StudentCourse():
    '''
    Logged in students can access this menu to perform the following actions:

    (c) change: enables a student to change their password
    (e) enrol: Student enrols in a subject. A student can enrol in a maximum of 4 subjects
    (r) remove: Student can remove a subject from subjects' enrolment list
    (s) show: Shows the enrolled subjects and marks the grades for each subject
    (x) exit
    '''

    def __init__(self, student_id, name, email, password, subject_str, mark_str):
        self.student_id:str = student_id
        self.name:str = name
        self.email:str = email
        self.password:str = password
        self.subjects:list[Subject] = self._get_subjects(subject_str, mark_str)
        
    def _get_subjects(self, subject_str, mark_str):
        id_arr = subject_str.split()
        marks = [int(mark) for mark in mark_str.split()]
        subject_arr = []

        while len(id_arr) != len(marks):
            if len(id_arr) < len(marks):
                id_arr.append(Subject.new_id(Subject._get_instances()))
            elif len(id_arr) > len(marks):
                marks.append(Subject.new_mark())

        for subject_id, mark in zip(id_arr, marks):
            subject_arr.append(Subject(subject_id, mark))

        return subject_arr

    def change(self):
        '''
        Changes the current student's password.
        Valid passwords must:
            - Start with upper case
            - Minimum 6 letters
            - Followed by minimum 3-digits
        '''
        cli.message("Updating Password", "yellow")
        new_password = ""
        confirm_password = ""

        while Utils.password(new_password) == False:
            new_password = input("New Password: ")
            if Utils.password(new_password) == False:
                cli.message("Incorrect password format", "red")

        while new_password != confirm_password:
            confirm_password = input("Confirm Password: ")
            if  new_password != confirm_password:
                cli.message("Password does not match - try again", "red")

        self.password = new_password


    def enrol(self):
        '''
        Adds a random subject to your current list of subjects.
        You can have a maximum of up to four subjects.
        '''
        if len(self.subjects) >= 4:
            cli.message("Students are allowed to enrol in 4 subjects only", "red")
        else:
            new_subject = Subject()
            self.subjects.append(new_subject)

            cli.message(f"Enrolling in Subject-{new_subject.subject_id}", "yellow")
            cli.message(f"You are now enrolled in {len(self.subjects)} out of 4 subjects", "yellow")

    def remove(self):
        '''
        Removes the specified subject from the current student's subject list.
        '''
        selection = input("Remove Subject by ID: ")
        for subject in self.subjects:
            if selection == subject.subject_id:
                self.subjects.remove(subject)
                cli.message(f"Dropping Subject-{subject.subject_id}", "yellow")
                break
        

    def show(self):
        '''
        Prints the student's currently enrolled subjects to the terminal.
        '''
        def show(self):
    '''
    Prints the student's currently enrolled subjects to the terminal.
    '''
    # Loop through each Subject in self.subjects
    for subject in self.subjects:
        # Extract subject_id, mark, and grade from the Subject object
        subject_id = subject.subject_id
        mark = subject.mark
        grade = subject.grade

        # Format the output string with subject_id, mark, and grade
        output_line= f"[ Subject::{subject_id} -- Mark = {mark} -- Grade = {grade.rjust(3)}]"

        # Print the formatted string
        print(output_line)


def main():
    test = StudentCourse("0001", "test", "email", "123","123 456", "65 76 85")
    print(Utils.password("123"))
    cli.menu(test)
    print(test.password)

if __name__ == "__main__":
    main()
