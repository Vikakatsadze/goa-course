#შექმენით კალკულატორი, მომხმარებელს შეეკითხეთ ორი რიცხვი, შემდეგ შეეკითხეთ რა მოქმედების შესრულება სურს ამ ორ რიცხვზე და მისი პასუხიდან გამომდინარე შეასრულეთ მოქმედება და დაბეჭდეთ მაგალითად თუ მომხმარებელი შემოიტანს რიცხვებს 5 და 7 ,და შემოიტანს მოქმედებას მაგალითად დამატებას თქვენ უნდა დაუბეჭდოთ 5 + 7 = 12
num1 = int(input(" please enter a number"))
math_operation = input("please enter a mathematical operation: ")
num2 = int(input(" please enter a number: "))

if math_operation == "+":
    print(num1+num2)
elif math_operation == "_":
    print(num1-num2)
elif math_operation == "*":
    print(num1*num2)
elif math_operation == "/":
    print(num1 / num2)
elif math_operation == "//":
    print(num1 // num2)
elif math_operation == "%":
    print(num1 % num2) 
else:
    print(" sorry i cant solve that")
                           