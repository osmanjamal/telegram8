import re

def format_price(price):
    return f"{price:.2f} ريال"

def validate_phone_number(phone):
    # نمط بسيط لأرقام الهواتف السعودية
    pattern = r'^(05|5)(5|0|3|6|4|9|1|8|7)([0-9]{7})$'
    return re.match(pattern, phone) is not None