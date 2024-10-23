// let park = "disney"

// //Camel Case Example
// let firstName = "Kaden"
// let lastName = "Smiley"

// console.log(firstName)
// console.log(park)
// console.log(typeof (-65))
// console.log(typeof(20n))
// console.log(typeof "true")

// let message = `I enjoy
// chocolate
// and 
// Ice Cream`
// console.log(message)

// let name = "Kaden"
// let age = 16
// let alive = true
// let favFoods = ["mexican", "italian", "chinese"]

// console.log(name + " " + age + " " + alive + " " + favFoods)

// let result = "Hired"
// const nickName = "The Council"
// console.log("The person we interviewed yesterday named " + nickName + " was " + result)
// // spaces between + and ""s don't matter

// let turquoise = "blue"
// const strandsOfGrass = 1000000
// var dead = true
// console.log("The sky was "+turquoise+" and there were "+strandsOfGrass+" strands of grass that spoke "+dead)

// console.log(typeof String(84))
// console.log(String(84))
// console.log(String(null))
// console.log(String(true))
// console.log(Number(true)+" "+Number(null))
// console.log(Boolean(0))
// let age1 = 23
// let age2 = 56
// if(age1>45){
//     console.log("They OLD")
// }
// // Since this if statement is false, nothing is printed
// let bf = "Jesse"
// let thinksBF = "Dylan"
// if(bf!=thinksBF){
//     console.log("You need more friends")
// }
// if(15 == "15"){
//     console.log("You can read yay")
// }
// //two equal signs will convert and then compare. 3 equal signs won't work becuase there is no conversion.
// if("15" === "15"){
//     console.log("This won't work unless they are the same type of data")
// }
// let test1, test2, test3
// //These are all separate variables
// let aliveOrNot = false, year = 2024, truck = "Tacoma"
// if(aliveOrNot == true){
//     if(year==2024){
//         console.log("Yayy")
//     }
//     console.log("Level 1")
// }else{
//     console.log("oops")
// }
// if(aliveOrNot){
//     console.log("True")
// } // This will run because alive is a boolean that is set to true. If it was false, it wouldn't run
// let money = 14
// if(money <= 20){
//     console.log("Broke Netflix")
// }else if(money >= 21 && money <= 60){
//     console.log("Movie Theatre")
// }else if(money >= 61 && money <= 80){
//     console.log("Dinner")
// }else{
//     console.log("Sky Diving")
// }

// //Browser Commands
// // let num = 5546
// // alert("This is proof")
// // console.log("I will live until I'm " + num)
// // This will stop at the alert until the user confirms they read it, then executes the rest of the code after it.

// // answer = confirm("ME")
// // if the user responds with okay, answer stores true and if it is a no, it will store false

// // let firstName = prompt("What is your first name?")
// // first name now holds the string value of the response
// // console.log(firstName)

// input1 = 76.8
// input2 = 5

// console.log(`Comparing ${input1} (${typeof(input1)}) amd ${input2} (${typeof(input2)})`)
// console.log(`When compared with == is ${input1 == input2}`)
// console.log(`When compared with === is ${input1 === input2}`)
// console.log(`When compared with Object.is is ${Object.is(input1,input2)}`)

// console.log("Honey, I shrunk the kids!")

// let x = 14
// let y = 25

// function addFunction(x,y,z){
//     console.log(String(x+y+z))
// }

// addFunction(x,y,45)

// myNameIs = "Kaden"
// function childTruth(hisName){
//     console.log(String(hisName) + " is the favorite child.")
// }
// childTruth(myNameIs)

// let tests = "Bored"
// let tests5 = "bored"

// // console.log(Object.is(tests,tests5))

// // console.log(5>4)
// // console.log("apple" > "appear")
// // console.log("west" < "Went")
// // console.log(2 > "12")
// // console.log(undefined == null)
// // console.log(undefined === null)
// // console.log(null == 0)

// let answer = false
// if(answer){
//     console.log("This is true")
// }
// if(!answer){
//     console.log("This is false")
// }

// let years = 231
// if(years == 231) console.log("uh oh");

// if(true)console.log('works');

// if(0)console.log("doesn't work");

// let check = "false"
// if(check)console.log("this works too")

// let age7 = 21
// let canDrink = (age7 >= 21) ? 643 : 24
// console.log(canDrink)


// let a = 2
// let b = 5
// let results12 = (a+b < 4) ? "Below" : "Over"
// console.log(results12)

// let letterGrade = 40
// if(letterGrade > 90){
//     return "A"
// }else if(letterGrade > 80){
//     return "B"
// }else if(letterGrade > 70){
//     return "C"
// }else if(letterGrade > 60){
//     return "D"
// }else{
//     return "F"
// }
// let myVal = 2
// switch (true){
//     case(myVal >=10):
//         multiplier = 2;
//         console.log("Jeff");
//         break;
//     case (myVal >= 0):
//         multiplier = 1;
//         console.log("Men");
//         break;
//     default:
//         multiplier = -1;
//         console.log("Mommy");
// }
// let login = "Director"
// let message2;

// switch (login){
//     case ("Employee"):
//         message2 = "Hello";
//         break
//     case ("Director"):
//         message2 = "Greetings"
//         break
//     case (""):
//         message2 = "No login"
//         break
//     default:
//         message = ""
// }
// console.log(message2)

let pen = true
let paper = false
let keyboard = true
let mouse = true

if(pen && paper||keyboard && mouse){
    console.log("You can take notes")
}
let stayedUpLate = false
let playedTooMuch = false
let studied = true
let skippedBreakfast = false

if(!stayedUpLate && !playedTooMuch && studied && !skippedBreakfast){
    console.log("YAAYYYY!!!!")
}

let location = null
let geoLocation = "Tuscon"
console.log(geoLocation ?? "Not a valid location")
let newLocation = location ?? "Arizona"
console.log(newLocation)


let a = null
let b = undefined
let c = ""
let d = "This is the last thing"
console.log(a ?? b ?? c ?? d)

let empty = []
for(var i = 1;  i < 6; i++){
    
    let newNumber = Math.floor((Math.random()*99+1))
    empty.push(newNumber)
}
console.log(empty)

for(let i = 10; i > -30; i--){
    console.log(i)

}

for(let i = 1; i < 20; i++){
    if((i==5)||(i==7)||(i==9)||(i==11)||(i==13)){
        console.log(i)
    }
}

for(let i = 5; i < 12; i++){
    console.log(i)
}
for(let i = 0; i < 9; i++){
    console.log("this is nice")
}
for(let i = 11; i > 0; i -= 2){
    console.log(i)
}

let i = 3
while(i){
    console.log(i)
    i--
}