import os
import regex as re
import cli

class Database():
    separator = os.path.sep
    
    def __init__(self, filepath="student.data", headers):
        # Default directory and file name
        self.headers = headers
        self.default_name:str = "student.data"
        self.current_dir:str = os.path.dirname(__file__)

        # Database path, this will be used to create a Database object to perform CRUD operations on
        self.path:str = self.get_path(filepath)
        os.makedirs(os.path.dirname(self.path) + Database.separator, exist_ok=True)

        # Reads the filepath into a data field and then closes the file
        # if the filepath does not exist, then it is first created and that is read into data
        self.make_file()
        self.data:list[dict] = self.read_data()
    
    def make_file(self):
        '''
        Creates the data file if it doesn't exist
        If it does exist, read the data file
        '''
        file_handle = None
        # 'r' opens the existing file handle for reading
        if self.file_in_dir():
            file_handle = open(self.path, mode="r")
        else:
            cli.message("File does not exist!", "red")
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
            self.path = Database.separator.join((self.current_dir, self.default_name))
        
        # 'w' creates a new file for writing
        headers = ",".join(self.headers)
        return open(self.path, mode="w").write(headers)

    def write_data(self, data_map, line_index=None):
        '''
        Modifies the values in the self.data field
        If a line index is given, it will insert the line into the provided index
        '''
        if type(line_index) == int:
            self.data[line_index] = data_map
        else:
            self.data.append(data_map)

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

            # Converts values for each dictionary in data to a string representation
            lines = [",".join(line.values()) for line in self.data]

            # Writes the input string to the data file
            save_content = "\n".join(lines)
            file_handle.writelines(save_content)

    def read_data(self):
        '''
        By default, reads all the lines in the file
        '''
        data:list[dict] = []
        with open(self.path, mode="r") as file_handle:
            # Splits the data file by new line characters such that they can be indexed
            lines:list[str] = file_handle.read().split('\n')

            keys:list[str] = lines[0].split(",")
            entries:tuple[str] = (row.split(",") for row in lines[1:])

            for entry in entries:
                # Validates the length of lines so that that they match the length of keys
                if len(entry) != len(keys):
                    pass
                else:
                    data_map:dict = dict(zip(keys, entry))
                    data.append(data_map)

        return data

    def clear_data(self, line_index=None):
        '''
        Deletes the contents of the data field
        If an index is provided, only the given index for each key will be removed
        '''
        if type(line_index) == int:
            del self.data[line_index]
        else:
            self.data = []

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

        if re_dir: return Database.separator.join((re_dir, self.default_name))
        elif re_file: return Database.separator.join((self.current_dir, re_file))
        else: return re_path

def main():
    DATAFILE = "student.data"
    new_db = Database(DATAFILE)
    print(new_db.read_data())
    # new_db.write_data(f"")
    #new_db.update_file()

if __name__ == "__main__":
    main()
