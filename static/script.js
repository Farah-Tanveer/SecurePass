document.querySelectorAll("button").forEach(btn=>{

btn.addEventListener("click",function(e){

let circle=document.createElement("span");

circle.classList.add("ripple");

this.appendChild(circle);

setTimeout(()=>{
circle.remove();
},600);

});

});
/* Navbar hover glow */

document.querySelectorAll(".nav-links a")
.forEach(link => {

link.addEventListener("mouseover", () => {

link.style.textShadow =
"0 0 8px rgba(210,193,182,.8)";

});

link.addEventListener("mouseout", () => {

link.style.textShadow = "none";

});

});