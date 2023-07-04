# Code for replacing domain in an email address

def replaceDomain(email, oldDomain, newDomain):
    print("Old Email: " + email)  # Print the original email address
    if "@" + oldDomain in email:  # Check if the old domain is present in the email address
        index = email.index("@" + oldDomain)  # Find the index of the old domain in the email address
        newEmail = email[:index] + "@" + newDomain  # Replace the old domain with the new domain to create a new email address
        print("New Email: " + newEmail)  # Print the new email address

replaceDomain("notjawad404@yahoo.com", "yahoo.com", "gmail.com")  # Calling the replaceDomain function

'''Explanation: 
This code defines a function called "replaceDomain" that takes in three parameters: an email address, 
an old domain, and a new domain. The function first prints the original email address, then checks if the old domain 
is present in the email address. If it is, the function finds the index of the old domain in the email address and 
replaces it with the new domain, creating a new email address. The new email address is then printed. 

When the function is called with the arguments "notjawad404@yahoo.com", "yahoo.com", and "gmail.com", the function 
will print "Old Email: notjawad404@yahoo.com" and "New Email: notjawad404@gmail.com" '''
