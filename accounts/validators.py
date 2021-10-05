import re

class ValidationError(BaseException):
    def __init__(self, code: str, info=''):
        self.code = code
        self.info = info
    
    code = ''
    info = ''

class WrongCharset(BaseException):
    def __init__(self, details: str):
        self.details = details

    details = ''

PASSWORD_ALLOWED_SPECIAL_SYMBOLS = '!$^&_*-+=;:,.?'

############################################################
#       Password validator for the CreateUser form.        #
############################################################
#
# This class's methods raise ValidationError if validating
# field does not meet specified requirements.
#
class PasswordValidator(object):

    # validate password contents: contains only digits, English letters, and special symbols  
    def dig_eng_and_spec_symbols(password: str):
        if not re.search(re.compile(f'^[0-9A-Za-z{PASSWORD_ALLOWED_SPECIAL_SYMBOLS}]+$'), password):
            raise ValidationError(
                'pwd_dig_eng_and_spec_symbols',
                info="password must contain English letters and special symbols only"
            )

    # validate basic password complexity: at least one digit
    def one_digit(password: str):
        if not re.findall('\d', password):
            raise ValidationError(
                'pwd_at_least_one_digit',
                info="password must contain at least one digit in it"
            )
    
    # validate basic password complexity: at least one special symbol
    def one_special_symbol(password: str):
        if not re.findall(f'[{PASSWORD_ALLOWED_SPECIAL_SYMBOLS}]', password):
            raise ValidationError(
                'pwd_at_least_one_special_symbol',
                info=f"password must contain at least one of the symbols {PASSWORD_ALLOWED_SPECIAL_SYMBOLS} in it"
            )

    # validate basic password complexity: at least 8 characters long
    def eight_characters(password: str):
        if len(password) < 8:
            raise ValidationError(
                'pwd_at_least_8_characters',
                info="password must be at least 8 characters long"
            )

    # validate basic password complexity: at least one uppercase letter
    # 
    # Warning!
    # This works only when password made of digits, english letters, and
    # special symbols. Otherwise, this function raises WrongCharset.
    def one_uppercase_letter(password: str):
        try:
            PasswordValidator.dig_eng_and_spec_symbols(password)
        except ValidationError:
            raise WrongCharset(
                "for this function to work, a given password must only contain digits, english letters, and pre-defined special symbols"
            )

        if not re.findall('[A-Z]', password):
            raise ValidationError(
                'pwd_at_least_one_uppercase_letter',
                info="password must contain at least one uppercase letter"
            )