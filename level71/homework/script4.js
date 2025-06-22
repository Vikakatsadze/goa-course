//Splice მეთოდის გამოყენებით ჩაანაცვლეთ სიაში ყველა უარყოფითი რიცხვი 0 - ით

let arr = [323, -456, 256, 456, -678, 234]
for(let i = 0; i<arr.length; i++){
    if(arr[i]<0){
        arr.splice(i, 1, 0)
    }
}
console.log(arr)