#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი ლუწი ან 3-ის ჯერადი.

num = int(input(" enter a number: "))

if num % 2 == 0:
    print(" this number is iven ")
elif num % 3 == 0:
    print(" this number can be divided on 3")
else:
    print(" your number cannot be divided on 5")