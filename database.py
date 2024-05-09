import os
import regex as re
import cli

class Database():
    def __init__(self, filepath="student.data"):
        # Default directory and file name
        self.default_name = "student.data"
        self.current_dir = os.path.dirname(__file__)

        # Database path, this will be used to create a Database object to perform CRUD operations on
        self.path = self.get_path(filepath)

        # Reads the filepath into a data field and then closes the file
        # if the filepath does not exist, then it is first created and that is read into data
        self.make_file()
        self.data = self.read_data()
    
    def make_file(self):
        '''
        Creates the data file if it doesn't exist
        If it does exist, read the data file
        '''
        file_handle = None
        # 'r' opens the existing file handle for reading
        if self.file_in_dir():
            cli.notify("File exists!")
            file_handle = open(self.path, mode="r")
        else:
            cli.error("File does not exist!")
            file_handle = self.create_file()

        file_handle.close()

    def file_in_dir(self):
        '''
        Checks if the given file path exists in the directory and returns a corresponding boolean.
        To check the current directory, file paths should be preceeded with ./
        '''
        return os.path.exists(self.path)

    def create_file(self):
        # Guard clause for None paths
        if not self.path:
            cli.error(f"'{self.path}' is an invalid path, default 'student.data' was created instead.")
            self.path = "\\".join((self.current_dir, self.default_name))
        
        # 'w' creates a new file for writing
        return open(self.path, mode="w")

    def write_data(self, line, line_index=None):
        '''
        Modifies the values in the self.data field
        If a line index is given, it will insert the line into the provided index
        '''
        for idx, key in enumerate(self.data):
            if type(line_index) == int:
                self.data[key].insert(line_index, line.split(',')[idx])
            else:
                self.data[key].append(line.split(',')[idx])

    def update_file(self):
        '''
        Writes the self.data field to the file (imagine this to be a save function)
        Changes made to the file cannot be undone
        This function should NOT be called regularly, only when necessary
        '''
        with open(self.path, mode="r+") as file_handle:
            # Deletes the contents in the data file
            file_handle.seek(len(file_handle.readline()))
            file_handle.truncate()

            # Transposes keys into lines
            lines = [','.join(line) for line in zip(*(self.data[key] for key in self.data))]

            # Writes the input string to the data file
            save_content = "\n".join(lines)
            file_handle.writelines(save_content)

    def read_data(self):
        '''
        By default, reads all the lines in the file
        '''
        data = {}
        with open(self.path, mode="r") as file_handle:
            # Splits the data file by new line characters such that they can be indexed
            lines = file_handle.read().split('\n')
            
            # Takes the header line as keys for dictionary
            for key in lines[0].split(','):
                data[key] = []

            # Populates data keys with values after the header line
            for idx, key in enumerate(data.keys()):
                for line in lines[1:]:
                    data[key].append(line.split(',')[idx])

            return data

    def clear_data(self, line_index=None):
        '''
        Deletes the contents of the data field
        If an index is provided, only the given index for each key will be removed
        '''
        for key in self.data:
            if type(line_index) == int:
                self.data[key] = self.data[key][:line_index] + self.data[key][line_index+1:]
            else:
                self.data[key] = []

    def get_path(self, filepath):
        '''
        If file path is received, create that path
        If only filename is received, create filename in current directory
        If only directory name is received, create "student.data" in given directory
        Function returns a full path
        '''
        re_dir, = re.findall(r"^.*[/\\]$", filepath) or [None]
        re_file, = re.findall(r"^[^/\\]+$", filepath) or [None]
        re_path, = re.findall(r"^.*$", filepath) or [None]

        if re_dir: return "\\".join((re_dir, self.default_name))
        elif re_file: return "\\".join((self.current_dir, re_file))
        else: return re_path

def main():
    DATAFILE = "students.data"
    new_db = Database(DATAFILE)
    # new_db.write_data(f"")
    #new_db.update_file()

if __name__ == "__main__":
    main()