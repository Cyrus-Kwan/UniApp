from admin import Admin
from student import Student
from database import Database as db
import cli
#import datetime

class University:
        
    def __init__(self, database) -> None:
        self.db = database
        db.initialize()
        self.student = db.read_data() 
        self.admin = Admin() #Build the object of the admin
        cli.menu(self)
            
    def student(self):
        return Student()

    def admin(self):
        return Admin() 

   # def UniversityMenu(self):
   #     x = datetime.datetime.now()
    #    print(f'University menu {x.strftime("%c")}')
     #   choice = input("University menu (L/A/X): ")
      #  while choice != 'x':
       #     match choice:
        #        case 'S':
         #           self.student()
          #      case 'A':
           #         self.admin()
            #    case _:
             #       self.exit_menu()
                    
      #  choice = input("University menu (S/A/X): ")        

       # print("Done")
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
    
