from admin import Admin
from student import Student
import cli
import datetime

class University:
    def __init__(self, name) -> None:
        self.name = name
        self.admin = Admin()
        self.student = Student()
        cli.menu(self)

    def helpMenu(self):
        print(f"Menu Options: \n( S ) Login and use a Student menu\n( A ) Admin Login \n(X) Exit the system")

        '''
    The university menu system should enable users to choose to go the Admin menu or Student Menu

    (A) Admin
    (S) Student
    (X) Exit
    '''
    def universityMenu(self):
        x = datetime.datetime.now()
        print(f'University menu {x.strftime("%c")}')
        choice = input("University menu (S/A/X): ")
        while choice != 'x':
            match choice:
                case 'S':
                    self.student()
                case 'A':
                    self.admin()
                case _:
                    self.helpMenu()
                    
            choice = input("Customer menu (S/A/X): ")        

        print("Done")
    
    def admin(self):
        return Admin()

    def student(self):
        return Student()

def main():
    pass

if __name__ == '__main__':
    UniversityA = University("CBA")
    UniversityA.universityMenu()
    



