class Sports{
    constructor(name){
        this.name = name
    }
    Throwball(){
        console.log(`This ${this.name} can throw ball`)
    } 
    Scoring(){
        console.log(` ${this.name}  can score`)
    }
}

class Basketball extends Sports{
    Throwball(){
        console.log(`${this.name} can Throw Fast and accurate throwing!`)
    }
    Scoring(){
        console.log(`${this.name} can score Points such as 3-pointer DUNK🏀 and normal shots`)
    }
}

class Football extends Sports{
    Throwball(){
        console.log(`${this.name} has kicked the ball outside of bounders the enemy team gets a free throw`)
        console.log("Free throws are slow but have some distance")
    }
    Scoring(){
        console.log(`${this.name} can GOAL!⚽ and Hatricks🎩`)
    }
}

const GOAT = new Football("Lioneal Andreas Messi")
GOAT.Scoring()
GOAT.Throwball()
console.log("\nNext GOAT in Basketball")
const LebronJames = new Basketball("Lebron James")
LebronJames.Scoring()
LebronJames.Throwball()