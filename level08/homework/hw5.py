#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი რიცხვი 100-ზე მეტი და ლუწი.

user_num = int(input(" enter a number: "))
if user_num > 100 and user_num % 2==0:
    print(" this number is greater than 100 and even ")
else:
    print(" this number a neither ")
    