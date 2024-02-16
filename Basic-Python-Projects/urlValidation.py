import re

def urlValidation(url):
    if re.match(r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', url):
        print(f'{url} is a valid URL')
        return True
    else:
        print(f'{url} is not a valid URL')
        return False
    
urlValidation('http://www.google.com')
urlValidation('https://www.google.com')
urlValidation('http://www.google.co.in')
urlValidation('www.google.co.in')
urlValidation('sasasasa')