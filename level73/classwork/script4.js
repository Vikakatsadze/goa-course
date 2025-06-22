//You get an array of numbers, return the sum of all of the positives ones.

function positiveSum(arr) {
    let sum = 0
    for(let element of arr){
      if(element >= 0){
        sum+=element
      }
    }
    return sum
  }