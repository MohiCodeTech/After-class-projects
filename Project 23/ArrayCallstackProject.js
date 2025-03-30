Foods = ["Pasta", "Pizza", "Dosa", "Rice and curry"];

Foods[0] = "Noodles";

console.log("These are my Favourite meals " + Foods);

Numbers = [22, 79, 10, 7, 99];

console.log("\n" + Numbers[1])

Numbers[1] = 84

console.log("These are my favourite Numbers! " + Numbers )

Numbers.pop()
console.log("This is numbers after pop function: " + Numbers)

Numbers.push(54)
console.log("This is numbers after pushing the number 54: " + Numbers)

//This is Call stack
function first(){
    console.log("Hello This is me the first")
}

function second(){
    first()
    console.log("Hello This is me the second")
}

function third(){
    second()
    console.log("Hello i am the third!")
}

third()
