//შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ კი დაბეჭდეთ ამ სიის ჯამი

function sumArr(arr){
    let sum = 0
    for (let element of arr){
        sum += element}
    return sum    
    
}
console.log(sumArr([10,20,53,27]))