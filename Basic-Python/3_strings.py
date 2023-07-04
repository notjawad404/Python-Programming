name = "Jawad Ali"
print(name)

'''
String Indexing
'''
print(name[0])  # character at index 0
print(name[-1])  # character at last index (for reverse indexing, use -ve numbers

print(name[0:6])  # for accessing a slice of characters

print(name[:6])  # first characters up to (range-1)

print(name[6:])  # (range) till last all characters

'''
String Modifications
'''
str0 = "Welcome to Cython"

print(str0.index("C"))  # printing index of any character in string

str1 = str0[0:11] + "P" + str0[12:]  # Correction of typo mistakes
print(str1)


ans = "Python" in str1  # Checking if a character or slice of characters are present in string
print(ans)

ans = "Cython" in str1
print(ans)
