# 9) შექმენით ცვლადები და დააჯამეთ ლუწი და კენტი რიცხვები სიიდან 

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = 0
odd = 0

for i in range(11):
    if i % 2 == 0:
        even += num[i]
    else:
        odd += num[i]
print(odd)
print(even)
