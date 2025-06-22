//Given a string, you progressively need to concatenate the first character from the left and the first character from the right and "1", then the second character from the left and the second character from the right and "2", and so on.

function charConcat(string){
    let st =""
    let bla = string.length
    let idk = Math.floor(bla/2)
    for(let i=0;i<idk;i++){
      st += string[i]+string[bla-1-i]+(i+1)
    }
    return st
  }