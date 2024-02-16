import re

def phoneNumValidation(phoneNum):
    if re.match(r'^\d{11}$', phoneNum):
        print(f'{phoneNum} is a valid phone number')
        return True
    else:
        print(f'{phoneNum} is not a valid phone number')
        return False
    

phoneNumValidation('12345678901')
phoneNumValidation('1234567890')
phoneNumValidation('123456789012')
phoneNumValidation('1234567890a')