#Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

#The output should be two capital letters with a dot separating them.

def abbrev_name(name):
    s = []
    n = ""
     
    s.append(name[0].upper() + "." + str(name[name.index(" ") + 1].upper()))
    for i in s:
        n += i
    return n