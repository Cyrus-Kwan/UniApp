from admin import Admin
from student import Student
from database import Database as db
import cli

class University:

    def __init__(self, name):
        self.name = name
        cli.menu(self)
        
    def student(self):
        return Student()

    def admin(self):
        return Admin() 

def main():
    pass
'''
    The university menu system should enable users to choose to go the Admin menu or Student Menu

    (A) Admin
    (S) Student
    (X) Exit
'''
    
if __name__ == '__main__':
    main() 
    