//Write a function which calculates the average of the numbers in a given array.

//Note: Empty arrays should return 0.

function findAverage(array) {
    let sum = 0
    if(array.length == 0){
      return 0
    }
    for(let i of array){
      sum+=i
    }
    let avg = sum/array.length
    return avg
  }