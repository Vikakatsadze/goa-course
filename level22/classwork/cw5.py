#სიის ფუნქციები

#len - length (სიგრძე)
#append()
#insert()
#pop()

numbers = [15,12,3,15,61]
print(len(numbers))    #ამ შემთხვევაში დამიწერს რამდენი რიცხვია ოღონდ აქ ნულიდან არ იწყება, აქ ჩვეულებრივად ადამიანური თვლა მიდის

#ასევე შეგვიძლია გავაკეთოთ სტრინგებზე

surname = "motiashvili"
print(len(surname)) #აქ გამოგვიტანს თუ რამდენი ასო არის გვარში

surname = "motiashvili "
print(len(surname)) #ეს გამოიტანს 12 ს რადგან სფეისი ჩვეულებრივ სიმბოლოდ ითვლება 

#სიმბოლოების დათვლა თუ გვინდა უნდა იყოს აუცილებლად სტრინგი ინტეჯერს ვერ ვიზამთ
# 50 ესე არა "50"