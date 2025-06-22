//Given an array of integers your solution should find the smallest integer.

function findSmallestInt(arr) {
    var first = arr[0]
    
    for(let i of arr){
      if(i < first){
        first = i
      }
    }
    return first
    
  }