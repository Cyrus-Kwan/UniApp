class Subject():
    def __init__(self):
        self.subject_id = self.new_id()
        self.mark = self.new_mark()
        self.grade = self.get_grade(self.mark)

    def new_id(self):
        pass

    def new_mark(self):
        pass

    def get_grade(self, mark):
        pass

def main():
    pass

if __name__ == "__main__":
    main()