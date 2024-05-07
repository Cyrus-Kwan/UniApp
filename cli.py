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
    defaults = {exit_menu:"x", help:"h"}

    # Populates func map with class methods
    for method in get_methods(class_obj):
        func[keys[method]] = getattr(class_obj, method)

    # Populates func map with default methods
    for method in defaults:
        func[defaults[method]] = method

    # Sets a default user selection
    selection = None

    # Menu runs until the user exits the program
    while selection != "x":
        if title:
            selection = input(colour["cyan"]+f"{title}"+colour["white"])
        else:
            selection = input(colour["cyan"]+f"{get_title(class_obj)}"+f"{get_options(func)}"+": "+colour["white"])

        try:
            args = selection.split(" ")
            if func[args[-1]] in defaults:
                # Calls one of the default methods
                func[args[-1]](class_obj, func, selection)
            else:
                # Calls the class method
                func[selection]()
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
                method_keys[method] = char.lower()
                break

    return method_keys

def get_title(class_obj):
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

def exit_menu(*args):
    '''
    Exits the current class menu.
    Default method that is present in all menus.
    '''
    pass

def help(class_obj, func=None, selection=None):
    '''
    Prints the docstring of the parsed-in selection to the terminal.
    If the user selection was "h", prints the docstring of the class object.
    If the user selection is a class method followed by "h", EXAMPLE: "a h" prints the docstring of class method "a".
    '''
    args = selection.split(" ")
    if len(args) > 2:
        raise KeyError
    elif len(args) == 2:
        message(func[args[0]].__doc__, "yellow")
    else:
        message(class_obj.__doc__, "yellow")

def main():
    test = SomeElaborateClass()
    menu(test)

class SomeElaborateClass(object):
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