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

def message(text, code):
    print(colour[code]+f"{text}"+colour["white"])

def menu(class_obj, title=None):
    '''
    Calls a function based on the user's selection from available methods in the class object
    '''
    func = {}
    keys = getKeys(class_obj)
    defaults = {exit:"x", help:"h"}

    # Populates func map with class methods
    for method in get_methods(class_obj):
        func[keys[method]] = getattr(class_obj, method)

    # Populates func map with default methods
    for method in defaults:
        func[defaults[method]] = method

    selection = None
    while selection not in func.keys():
        if title:
            selection = input(colour["cyan"]+f"{title}"+colour["white"])
        else:
            selection = input(colour["cyan"]+f"{getTitle(class_obj)}"+f"{get_options(func)}"+": "+colour["white"])
        
        try:
            if func[selection] in defaults:
                # Calls one of the default methods
                func[selection](class_obj)
            else:
                # Calls the class method
                func[selection]()
            break
        except KeyError:
            error(f"'{selection}' is not a valid function.")

def getKeys(class_obj):
    '''
    Maps method names from a given class object to unique characters
    '''
    method_keys = {}

    # Iterates through each method String
    for method in get_methods(class_obj):
        # Iterates through each character in the method string
        for char in method:
            # Ensures only unique values are assigned to each method
            if char in method_keys.values():
                continue
            else:
                method_keys[method] = char
                break

    return method_keys

def getTitle(class_obj):
    '''
    Returns a string for a generic formatted title based on the given class parameter
    '''
    raw_name = re.search(r"(?<=\.)\w+(?=\s)", class_obj.__str__())[0] or None
    class_name = re.sub(r'((?<=\S)[A-Z](?=[a-z]))', r" \1", raw_name)

    return " ".join((class_name, "System: "))

def get_options(keys):
    '''
    Returns a string of menu options based on given dictionary keys.
    '''
    options = "("+"/".join(keys)+")"
    return options

def get_methods(class_obj):
    '''
    Returns a list of all public class methods in the given class object
    '''
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

def exit(class_obj):
    '''
    Exits the current class menu.
    Default method that is present in all menus
    '''
    del class_obj

def help(class_obj):
    print(class_obj.__doc__)

def main():
    test = SomeElaborateClass()
    menu(SomeElaborateClass())

class SomeElaborateClass():
    '''
    Sample docstring
    '''
    def apple(self):
        print("apple")

    def banana(self):
        print("banana")

    def coconut(self):
        print("coconut")

    def anchovies(self):
        print(">:]")

    def astronaut(self):
        print("i'm in space!")

    def ape(self):
        print("I like bananas")

if __name__ == "__main__":
    main()