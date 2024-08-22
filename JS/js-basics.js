let park = "disney"

//Camel Case Example
let firstName = "Kaden"
let lastName = "Smiley"

console.log(firstName)
console.log(park)
console.log(typeof (-65))
console.log(typeof(20n))
console.log(typeof "true")

let message = `I enjoy
chocolate
and 
Ice Cream`
console.log(message)

let name = "Kaden"
let age = 16
let alive = true
let favFoods = ["mexican", "italian", "chinese"]

console.log(name + " " + age + " " + alive + " " + favFoods)

let result = "Hired"
const nickName = "The Council"
console.log("The person we interviewed yesterday named " + nickName + " was " + result)
// spaces between + and ""s don't matter

let turquoise = "blue"
const strandsOfGrass = 1000000
var dead = true
console.log("The sky was "+turquoise+" and there were "+strandsOfGrass+" strands of grass that spoke "+dead)

console.log(typeof String(84))
console.log(String(84))
console.log(String(null))
console.log(String(true))
console.log(Number(true)+" "+Number(null))
console.log(Boolean(0))
let age1 = 23
let age2 = 56
if(age1>45){
    console.log("They OLD")
}
// Since this if statement is false, nothing is printed
let bf = "Jesse"
let thinksBF = "Dylan"
if(bf!=thinksBF){
    console.log("You need more friends")
}
if(15 == "15"){
    console.log("You can read yay")
}
//two equal signs will convert and then compare. 3 equal signs won't work becuase there is no conversion.
if("15" === "15"){
    console.log("This won't work unless they are the same type of data")
}
let test1, test2, test3
//These are all separate variables
let aliveOrNot = false, year = 2024, truck = "Tacoma"
if(aliveOrNot == true){
    if(year==2024){
        console.log("Yayy")
    }
    console.log("Level 1")
}else{
    console.log("oops")
}
if(aliveOrNot){
    console.log("True")
} // This will run because alive is a boolean that is set to true. If it was false, it wouldn't run
let money = 14
if(money <= 20){
    console.log("Broke Netflix")
}else if(money >= 21 && money <= 60){
    console.log("Movie Theatre")
}else if(money >= 61 && money <= 80){
    console.log("Dinner")
}else{
    console.log("Sky Diving")
}

//Browser Commands
// let num = 5546
// alert("This is proof")
// console.log("I will live until I'm " + num)
// This will stop at the alert until the user confirms they read it, then executes the rest of the code after it.

// answer = confirm("ME")
// if the user responds with okay, answer stores true and if it is a no, it will store false

// let firstName = prompt("What is your first name?")
// first name now holds the string value of the response
// console.log(firstName)

input1 = 76.8
input2 = 5

console.log(`Comparing ${input1} (${typeof(input1)}) amd ${input2} (${typeof(input2)})`)
console.log(`When compared with == is ${input1 == input2}`)
console.log(`When compared with === is ${input1 === input2}`)
console.log(`When compared with Object.is is ${Object.is(input1,input2)}`)

console.log("Honey, I shrunk the kids!")