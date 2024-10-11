#შეამოწმე მომხმარებლის შემოტანილი რიცხვი თუ არის 5-ის ან 10-ის ჯერადი.

num = int(input(" enter a num: "))
if num % 10 == 0:
    print(" your number can be divided 10 ")
elif num % 5 == 0:
    print(" your number can be divided 5 ")
else:
    print(" your number cannot be divided on 5")