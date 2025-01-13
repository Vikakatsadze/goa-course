# )დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს მომხმარებლის შემოტანილი რიცხვის მიხედვით (1 არის ორშაბათი, 2 სამშაბათი და ა.შ) გამოიყენეთ if elif else 


print(" ")
print("1  -  monday")
print("2  - tuesday")
print("3  - wednesday")
print("4  - thursday")
print("5  - friday")
print("6  - saturday")
print("7  - sunday")
print(" ")

num = int(input("enter a num: "))

if num == 1:
    print("monday")
elif num == 2:
    print("tuesday")
elif num == 3:
    print("wednesday")
elif num == 4:
    print("thursday")
elif num == 5:
    print("friday")
elif num == 6:
    print("saturday")
elif num == 7:
    print("sunday")
else:
    print("your num is incorrect")