//შექმენით სია, ამ სიაში შეინახეთ String-ტიპის მონაცემები და for-ციკლის გამოყენებით ახალ სიაში დაამატეთ ძველი სიიდან ყოველი სიტყვის პირველი ასო

let arr = ["vika", "geno", "jemo"]

let newArr = []

for (let i of arr){
    newArr.push(i[0])
}

console.log(newArr)