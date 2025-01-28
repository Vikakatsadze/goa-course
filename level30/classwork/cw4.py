#შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვებით სავსე სია ამ ფუნქციამ კი უნდა დააბრუნოს ამ სიის რიცხვების ჯამი

def sum():
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8] #ეს არის რიცხვებით სავსე სია

    numbers_sum = 0 #ცვლადი რომელიც არის თავდაპირველად ნულის ტოლი
    for i in range(len(numbers_list)): #დავატრიალეთ ციკლი 
        numbers_sum += numbers_list[i]


    return numbers_sum

print(sum())    