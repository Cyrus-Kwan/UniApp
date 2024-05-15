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
    def __init__(self, database:Database):
        '''
        Initializes the University object with a database.

        Args:
        - database (Database): The database object to be used by the University.
        '''
        self.database:Database = database
        cli.menu(self)  # Call the menu function from the cli module to display the menu options

    def admin(self):
        '''
        Creates an instance of the Admin class and returns it.
        '''
        return Admin(self.database)

    def student(self):
        '''
        Creates an instance of the Student class and returns it.
        '''
        return Student(self.database)

def main():
    DATAFILE = "student.data" # Filepath for the student data file.
    database = Database(filepath=DATAFILE)  # Create a Database instance with the specified filepath.
    University(database=database)  # Create an instance of University with the database object

if __name__ == "__main__":
    main() # Call the main function when the script is executed
