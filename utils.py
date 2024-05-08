import regex as re

class Utils():
    @staticmethod
    def password(password:str) -> bool:
        '''
        Valid passwords must:
            - Start with upper case
            - Minimum 6 letters
            - Followed by minimum 3-digits
        '''
        result = False
        pattern = re.compile(r"^[A-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*\d{3}$")
        result = pattern.fullmatch(password)
        return bool(result)

    @staticmethod
    def email(email:str) -> bool:
        '''
        Valid emails must:
            - contain the "@" symbol
            - contain "."
            - contain "university.com"
        '''
        result = False
        pattern = re.compile(r"^\w+[.]\w+[@]university[.]com$")
        result = pattern.fullmatch(email)
        return bool(result)