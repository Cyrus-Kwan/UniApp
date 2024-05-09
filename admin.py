import cli

from subject import Subject
from database import Database

class Admin():
    '''
    Admin menu offers the following actions:

    (c) clear database file: enables admin to clear the data file "students.data"
    (g) group students: shows the students organized with respect to the subject grade
    (p) partition students: shows the pass/fail distribution
    (r) remove student: enables admin to remove a student by ID
    (s) show: show the students from the data file
    (x) exit
    '''

    def __init__(self, database):
        self.database:Database = database
        # Admins do not require access to some specific keys
        self.exclude = (
            "password",
        )
        self.split = (
            "subjects",
            "marks",
        )
        self.students = self._get_students(self.exclude, self.split)
        cli.menu(self)
        self.database.update_file()

    def clear_database_file(self) -> None:
        '''
        Clears the data in memory and deletes all lines in the file excluding the headers
        '''
        cli.message("Clearing students database", "yellow")
        warning_text:str = "Are you sure you want to clear the database (Y)ES/(N)O: "
        warning:str = cli.colour["red"]+f"{warning_text}"+cli.colour["white"]
        selection:str = input(warning).lower()

        match selection:
            case "y":
                self.database.clear_data()
                self.database.update_file()
                self.students = self._get_students(self.exclude, self.split)
            case "n":
                pass

    def group_students(self) -> None:
        '''
        Shows a list of all the students organised by grade F -> HD
        '''
        cli.message("Student List", "yellow")

        grades_list = ("F", "P", "C", "D", "HD")
        for grade in grades_list:
            # Filter by grade
            students = filter(lambda student: Admin._average_grade(student) == grade, self.students)
            for student in students:
                name:str = student["name"]
                student_id:str = student["student_id"]
                pad_grade:str = grade.rjust(3, " ")
                pad_mark:str = str(Admin._average_mark(student["marks"])).rjust(5, " ")

                # Output formatting
                pattern:str = f"{pad_grade} --> [{name} :: {student_id} --> GRADE: {pad_grade} - MARK: {pad_mark}]"
                cli.message(pattern, "white")

    def partition_students(self):
        cli.message("PASS/FAIL Partition", "yellow")
        pass_arr = []
        fail_arr = []

        for student in self.students:
            name = student["name"]
            student_id = student["student_id"]
            grade = Admin._average_grade(student).rjust(2, " ")
            mark = str(Admin._average_mark(student["marks"])).rjust(5, " ")
            pattern = f"\n{' '*8}"+f"{name} :: {student_id} --> GRADE: {grade} - MARK: {mark}"
            if Admin._average_grade(student) == "F":
                fail_arr.append(pattern)
            else:
                pass_arr.append(pattern)
        
        fail_pattern = f"FAIL :: {", ".join(fail_arr)}"
        pass_pattern = f"PASS :: {", ".join(pass_arr)}"
        cli.message(fail_pattern, "white")
        cli.message(pass_pattern, "white")

    def remove_student(self) -> None:
        '''
        Removes the first instance of user selected student by ID in database data.
        self.students is then reinstantiated to match database.data
        '''
        data:dict = self.database.data
        student_id:str = input("Removing by ID: ")
        if student_id in data["student_id"]:
            idx:int = data["student_id"].index(student_id)
            self.database.clear_data(idx)
            self.students = self._get_students(self.exclude, self.split)
            cli.message(f"Removing Student {student_id} Account", "yellow")
        else:
            cli.message(f"Student {student_id} does not exist", "red")

    def show(self) -> None:
        '''
        Shows basic student information
        '''
        cli.message("Student List", "yellow")
        for student in self.students:
            name:str = student["name"]
            student_id:str = student["student_id"]
            email:str = student["email"]
            pattern = f"{name} :: {student_id} --> Email: {email}"
            cli.message(pattern, "white")

    def _get_students(self, private:tuple[str], splits:tuple[str]) -> list[dict]:
        '''
        Transposes database data for easier manipulation.
        '''
        transposed:list[dict] = []
        data:dict = {}

        # Creates a deep copy of database data but removes the specified private key
        for key in self.database.data.keys():
            if key in private:
                pass
            else:
                data[key] = self.database.data[key]

        student_list:zip = zip(*data.values())
        for value in student_list:
            student:dict = dict(zip(data.keys(), value))
            transposed.append(self._split_keys(student, splits))

        return transposed
    
    def _split_keys(self, map:dict, keys:tuple[str]) -> dict:
        '''
        Splits the specified keys in a dictionary by string whitespace.
        '''
        new_map = {}
        for key in map.keys():
            if key in keys:
                new_map[key] = map[key].split()
            else:
                new_map[key] = map[key]

        return new_map
    
    @staticmethod
    def _average_grade(student:dict):
        mark = Admin._average_mark(student["marks"])
        return Subject.get_grade(mark)
    
    @staticmethod
    def _average_mark(marks:list[int]):
        try:
            temp = [int(mark) for mark in marks]
            return round(sum(temp)/len(temp), 2)
        except TypeError:
            cli.message("Marks must be integers", "red")

def main():
    Admin(Database())
    pass

if __name__ == "__main__":
    main()