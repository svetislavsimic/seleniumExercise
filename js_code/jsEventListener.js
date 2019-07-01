function alertFunction() {
    alert("Yo");
}
var btn1 = document.createElement("BUTTON");
btn1.addEventListener("click", alertFunction);
btn1.innerHTML = 'Klik';
btn1.style.width = '200px'; 
btn1.style.height = '200px'; 
btn1.style.background = 'yellow';
btn1.style.color = 'red';
btn1.style.fontSize = '20px';
var d = document.getElementById("ntp-contents");
d.appendChild(btn1);
