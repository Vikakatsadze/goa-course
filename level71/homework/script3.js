//შექმენით სია სადაც იქნება user-ების სახელი და გვარი და ახალ სიაში დაამატეთ ამ იუსერების  ინიციალები სახელის და გვარის პირველი ასოები, მაგალითად: გიორგი ბიბილაშვილი -> გ.ბ

var list = ["გიორგი ბიბილაშვილი", "გიორგი ზირაქაშვილი", "goa academy", "bmw m4"]
var initials = []

for(let fullName of list){
    var parts = fullName.split(" ")

    initials.push(parts[0][0] + "." + parts[1][0])
}
console.log(initials)