//Prompით მომხმარებელს შემოატანინეთ მისი სახელი, გვარი, ასაკი და ჰობი, შემდეგ ეს ინფორმაცია შეინახეთ ობიექტში, ასევე ამ ობიექტს დაუმატეთ ფუნქცია, რომლის გამოძახებაზეც კონსოლში გამოიტანს "Welcome {name}"

const userInfo = {
    name: prompt("please enter your name :"),
    lastName: prompt("please enter your lastname: "),
    age: Number(prompt("enter your age: ")),
    hobby: prompt("enter your hobby"),
    greet(){
        return "Welcome " + this.name
    }
}
    console.log(userInfo)
    console.log(userInfo.greet())