#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    empty = ""
    for i in range(repeat):
        empty = empty + string
    return empty    