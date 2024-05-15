import cli

from database import Database
from admin import Admin
from student import Student

class University():
    '''
    The university menu system should enable users to choose to go the Admin menu or Student Menu

    (A) Admin
    (S) Student
    (X) Exit
    '''
    def __init__(self):
        cli.menu(self)

    def admin(self):
        return Admin()

    def student(self):
        return Student()

def main():
    DATAFILE = "student.data"
    database = Database(filepath=DATAFILE)
    University()

if __name__ == "__main__":
    main()