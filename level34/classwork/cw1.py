#Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
     strr = ""
     for char in x:
        if char != " ":
            strr += char
     return strr        