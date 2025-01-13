name = "vika"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "vika" არის ცვლადისთვის მნიშვნელობა

surname = "katsadze"

#print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "vika"   #ეს არის str (string) ტიპის ცვლადი
age = 22 # ეს არის int (integer) მთელი რიცხვი 
height = 184.5 #ეს არის float ტიპის ცვლადი (ათწილადი)
#boolean (bool) ტიპის ცვლადი

knows_programming = True  #True ან False
is_ugly = False   #snakecase(უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False #ჯავასკრიპტული camelcase 


print (name + " " + surname)

#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები 
#print(name + age)

print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programming))

print(name + " " + str(age))