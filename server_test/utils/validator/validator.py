import re


def validate_phone_number(phone_number):
    try:
        parsed_number = phone_number.parse(phone_number, None)
        return phone_number.is_valid_number(parsed_number)
    except phone_number.NumberParseException:
        return False


def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))
