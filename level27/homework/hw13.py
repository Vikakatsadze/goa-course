#შექმენით სია რომელშიც გექნებათ ოცი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ მხოლოდ 10-ზე ნაკლები და მხოლოდ ლუწი რიცხვები, ისე რომ ლუწიც იყოს და 10-ზე ნაკლებიც, გამოიყენეთ for loop

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


for i in num:
    if i < 10 and i %2 == 0:
        print([i])