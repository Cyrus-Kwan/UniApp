from admin import Admin
from student import Student
from database import Database
import cli

class University:

    def __init__(self, name, database):
        self.name = name
        Database.initialize()
        self.student = Database.read()
        
    def student(self):
        return Student()

    def admin(self):
        return Admin() 

    def main():
        uni = University("CBA")
        cli.menu(uni)
    '''
    The university menu system should enable users to choose to go the Admin menu or Student Menu

    (A) Admin
    (S) Student
    (X) Exit
    '''
    
    if __name__ == '__main__':
        main() 
    