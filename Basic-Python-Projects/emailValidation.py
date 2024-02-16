import re


def validEmail(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print(f'{email} is a valid email')
        return True
    else:
        print(f'{email} is not a valid email')
        return False
    
validEmail('abv@gmail.com')
validEmail('abv23@gmail.com')
validEmail('ab1.v@mail.jd')
validEmail('abv@yahoo.com')