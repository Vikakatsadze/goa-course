//შექმენით სია შეიყვანეთ user-ების სახელი და გვარი თუ user-ების სახელი და გვრი იწყება პატარა ასოთი slice-მეთოდის გამოყენებით ამოშალეთ ასეთი სახელები და გვარები სიიდან

let myArr = ["Saba Bokuchava", "gela barkalaia", "lorwo Givia", "Maia nutsubidze", "Tornike Beruchashvili"]
let filteredArr = []
for(let fullName of myArr){
    words = fullName.split(" ")
    if(words[0][0] == words[0][0].toUpperCase()&& words[1][0] == words[1][0].toUpperCase()){
        filteredArr.push(fullName)
    }
}alert(filteredArr)