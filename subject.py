import random
import cli

class Subject():
    # Stores all instances of Subject class, allows an instance to refrence other instances
    instances = []

    def __init__(self, subject_id=None, mark=None):
        Subject.instances.append(self)

        self.subject_id = -1
        self.mark = -1

        if subject_id and mark:
            self.subject_id = subject_id
            self.mark = mark
            self.grade = self.get_grade(self.mark)
        else:
            self.subject_id:str = self.new_id(Subject.instances)
            self.mark:int = self.new_mark()
            self.grade:str = self.get_grade(self.mark)
        Subject.instances.append(self)

    @staticmethod
    def new_id(self, subjects:list[object]) -> str:
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
        invalid_set = {int(subject.subject_id) for subject in subjects}
        full_set = set(range(1,999))
        valid_set = list(full_set-invalid_set)

        subject_id = random.choice(valid_set)
        line = str(subject_id).rjust(3, '0')
        return line
    
    @staticmethod
    def new_mark() -> int:
        '''
        mark is randomly generated where 25<= mark <= 100
        '''
        # Reference: https://docs.python.org/3/library/random.html#functions-for-integers
        # This method should return an Integer value between 25 and 100
        # Example: mark = 75
        #               return mark
        # NOTE: value types can be checked with print(type(value))
        new_mark= random.randint(25,100)
        return new_mark   

    @staticmethod    
    def get_grade(mark:int) -> str:    
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
        if mark < 50: 
            return "F"
        if mark >= 50 and mark < 65: 
            return "P"
        if mark >= 65 and mark < 75: 
            return "C"
        if mark >= 75 and mark < 85: 
            return "D"
        if mark >= 85:
            return "HD"   

    # This method belongs to the class and can be called without creating a class instance.
    @staticmethod    
    def _get_instances() -> object:
        '''
        This method is only intended to be used so that Subject instances 
        can reference other Subject instances.
        '''
        return Subject.instances

def main():
    # You can test your code here
    subject1 = Subject()
    subject2 = Subject(321, 57)
    print("Subject ID:", subject1.subject_id)
    print("Mark:", subject1.mark)
    print("Grade:", subject1.grade)
    # print(Subject._get_instances())

if __name__ == "__main__":
    main()