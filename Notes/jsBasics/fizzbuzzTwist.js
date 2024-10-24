let range = prompt("What do you want the range to be? 1 to what?")
let fizzCount = 0
let buzzCount = 0
let fizzbuzzCount = 0
for(var i = 1; i <= range; i++){
    switch(true){
        case(i%3 == 0 && i%5 == 0):
            console.log("FizzBuzz")
            fizzbuzzCount++
            break
        case(i%3 == 0):
            console.log("Fizz")
            fizzCount++
            break
        case(i%5 ==0):
            console.log("Buzz")
            buzzCount++
            break
        default:
            console.log(i)
    }
}
console.log(`FizzBuzz showed up ${fizzbuzzCount} times.`)
console.log(`Fizz showed up ${fizzCount} times.`)
console.log(`Buzz showed up ${buzzCount} times.`)