//Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

function moveZeros(arr) {
    let myArr = []
    for(let i of arr){
      if(i!==0){
        myArr.push(i)
      }
    }
    for(let num of arr){
      if(num === 0){
        myArr.push(num)
      }
    }
    return myArr
  }