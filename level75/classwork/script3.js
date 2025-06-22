const carInfo = {
    brand: "Toyota",
    model: "Camry",
    year: 2021,
    color: "DarkBlue",
    carFullInfo(){
        return this.brand + ' ' + String(this.year)+ ' ' + this.model + ' ' + this.color
    }
}
console.log(carInfo.carFullInfo())