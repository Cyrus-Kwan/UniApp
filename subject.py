import random

class Subject():
    def __init__(self, subject_id=None, mark=None):
        if subject_id and mark:
            self.subject_id = subject_id
            self.mark = mark
        else:
            self.subject_id = self.new_id()
            self.mark = self.new_mark()
        self.grade = self.get_grade(self.mark)

    def new_id(self):
        '''
        ID randomly generated 1 <= ID <= 999, unique and formatted as 3-digits width
        IDs less than 3-digits width should be completed with zeroes from the left.
        '''
        # Reference: https://docs.python.org/3/library/random.html#functions-for-integers
        # This method should return a String value between 1 and 999.
        # Reference: https://docs.python.org/3/library/stdtypes.html#str.ljust
        # If the value is smaller fewer than 3 digits long, the String should be padded with '0'
        # Example: subject_id = "023"
        #               return subject_id
        # NOTE: value types can be checked with print(type(value))
        return 0

    def new_mark(self):
        '''
        mark is randomly generated where 25<= mark <= 100
        '''
        # Reference: https://docs.python.org/3/library/random.html#functions-for-integers
        # This method should return an Integer value between 25 and 100
        # Example: mark = 75
        #               return mark
        # NOTE: value types can be checked with print(type(value))
        return 0

    def get_grade(self, mark):
        '''
        grade is determined based on the mark
        '''
        # Reference: https://docs.python.org/3/tutorial/controlflow.html#if-statements
        # This method should return a String value based on self.mark
        # If mark < 50, grade = "F"
        # If mark >= 50 and mark < 65, grade = "P"
        # If mark >= 65 and mark < 75, grade = "C"
        # If mark >= 75 and mark < 85, grade = "D"
        # If mark >= 85, grade = "HD"
        return 0

def main():
    # You can test your code here
    test_subject = Subject()
    print("Subject ID:", test_subject.subject_id)
    print("Mark:", test_subject.mark)
    print("Grade:", test_subject.grade)

if __name__ == "__main__":
    main()