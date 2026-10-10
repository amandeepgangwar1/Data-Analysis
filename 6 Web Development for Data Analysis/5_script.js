console.log("Hello World!");

let a = 34;
let b = 56;
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);


function sum(a, b) {
    return a + b;
}
console.log("The sum of 3 and 6 is: ", sum(3, 6))



document.getElementById("message").style.color = "red";



let btn = document.getElementById("btn");
btn.addEventListener("click", function() {
    alert("Button Clicked");
});



let scores = [85, 90, 78]
scores[1] = "Amandeep"
alert(scores[1])



let students = {
    name : "Rahul",
    age : 19
}
alert(students['name'])
alert(students['age'])