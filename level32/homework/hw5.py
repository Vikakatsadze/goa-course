#Kids drink toddy.
#Teens drink coke.
#Young adults drink beer.
#Adults drink whisky.
#Make a function that receive age, and return what they drink.

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age >= 14 and age < 18:
        return "drink coke"
    elif age < 21 and age >= 18:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"
    else:
        return "error"

