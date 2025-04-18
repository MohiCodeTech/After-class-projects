let minus = (a, b) => (a - b)
console.log(minus(10, -10))

let anonymfunc = function(){
    console.log("Hey this is a Secret Function You are not supposed to see this")
    console.log("Go shoo away!")
}
anonymfunc()

// try and catch!

try{
   let a = 99.1
   let b = 99.432424234324324234234324324234234234
   let sum = a - b
   console.log(sum)
}
catch(error){
    console.log("Uh oh u got an error ! Try again", error.message)
}

//Check if any specific character is there in the program
let test = "HelloIwant12ICECREAM"
let regex = /\s/
console.log(regex.test(test))