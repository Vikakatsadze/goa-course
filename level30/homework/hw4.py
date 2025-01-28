#შექმენით ფუნქცია რომელსაც არგგუმენტად გადაეცემა რიცხვი შემდეგ კი ფუნქციამ უნდა დაგვიბრუნოს მისი საპირისპირო რიცხვი

user_number = int(input("enter number: "))

def opposite(number):
    return number * -1
print(opposite(user_number))