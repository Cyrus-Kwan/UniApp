from admin import Admin
from student import Student
from database import Database as db
import cli
#import datetime

class University:
        
    def __init__(self, database) -> None:
        self.db = database
        db.initialize()
        cli.menu(self)
            
    def student(self):
        return Student()

    def admin(self):
        return Admin() 

'''
    The university menu system should enable users to choose to go the Admin menu or Student Menu

    (A) Admin
    (S) Student
    (X) Exit
'''
def main():
    database = db()
    University(database)
        #university.UniversityMenu()
            
if __name__ == "__main__":
    main()
    
