#კომენტარებით ახსენით რას შვება pop append

# append is adding a list to a list, for example we have a list "a" of integers
a = [1,2,3,4,5,6,7,]
# and we have a list "b" of strings
b = ["a","b","c"]
# and we want to combine this two lists we have to use append()
a.append(b)
# then we need to print our combined list
print(a)

# append() doesnt insert lists with a specific index it justs adds it in after last index



# pop removes an element from a list, for example we have a list "c"

c = [1,2,3,4,5,6,7]
# now for example if i want to remove number four i'l write it's index in pop() and it will remove number four
c.pop(3)
# now we need to print the result
print(c)