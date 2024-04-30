import regex as re

colour = {
    "black":"\033[0;30m",
    "red":"\033[0;31m",
    "green":"\033[0;32m",
    "yellow":"\033[0;33m",
    "blue":"\033[0;34m",
    "purple":"\033[0;35m",
    "cyan":"\033[0;36m",
    "white":"\033[0;37m",
}

def error(text):
    '''
    Prints error message in red text to the terminal
    '''
    print(colour["red"]+f"ERROR: {text}"+colour["white"])

def notify(text):
    '''
    Prints green text to the terminal
    '''
    print(colour["green"]+f"SUCCESS: {text}"+colour["white"])

def menu(class_obj):
    '''
    Calls a function based on the user's selection from available methods in the class object
    '''
    selection = input(getMethods(class_obj))
    func = {}
    for method in getMethods(class_obj):
        func[method] = getattr(class_obj, method)

    func[selection]()

def getTitle(class_obj):
    raw_name = re.search(r"(?<=\.)\w+(?=\s)", class_obj.__str__())[0] or None
    class_name = re.sub(r'((?<=\S)[A-Z](?=[a-z]))', r" \1", raw_name)
    method_keys = (key[0] for key in getMethods(class_obj))
    options = "("+"/".join(method_keys)+")"

    return " ".join((class_name, "System:", options))

def getMethods(class_obj):
    methods = []

    # Lambda function that check whether or not a method is callable
    is_method = lambda obj, func: callable(getattr(obj, func))
    # Lambda function that checks if a method is not double underscored
    is_pure = lambda func: re.fullmatch(r"^[^_].+[^_]$", func)

    for func in dir(class_obj):
        if is_method(class_obj, func) and is_pure(func):
            methods.append(func)

    # Methods are returned as strings
    return methods

def main():
    test = SomeElaborateClass()
    print(getTitle(test))

class SomeElaborateClass():
    def apple(self):
        print("apple")

    def banana(self):
        print("banana")

    def coconut(self):
        print("coconut")

if __name__ == "__main__":
    main()