def removeWhiteSpaces (string):
    
    newString = ''.join(string.split())
    print(newString)


removeWhiteSpaces("Hello World")
removeWhiteSpaces("Hello World 123 ")
removeWhiteSpaces(" Hello World 123 ")
removeWhiteSpaces(" Hello World 123")
