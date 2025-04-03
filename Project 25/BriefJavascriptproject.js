let count = 1
while(count <= 100){
    if(count == 4){
        console.log("Oh no! The program has reached the number 4! stop operation Now!")
        return;
    }
    else{
        console.log("ok")
    }
     count = Math.floor(Math.random() * 10 + 1)
     console.log(count);
}