#Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed. The geese are any strings in the following array, which is pre-populated in your solution:

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for i in geese:
        for elements in birds:
            if i == elements:
                birds.remove(i)
    return birds