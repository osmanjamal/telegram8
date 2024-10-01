import re

def validate_phone(phone):
    pattern = r'^(05|5)(5|0|3|6|4|9|1|8|7)([0-9]{7})$'
    return re.match(pattern, phone) is not None

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None