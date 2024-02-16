
def checkPaleindromes(word):
    if word == word[::-1]:
        print(f'{word} is a palindrome')
    
    else:
        print(f'{word} is not a palindrome')
        
    
print(checkPaleindromes('madam'))
print(checkPaleindromes('hello'))
print(checkPaleindromes('racecar'))