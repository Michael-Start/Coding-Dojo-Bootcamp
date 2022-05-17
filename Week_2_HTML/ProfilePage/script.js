console.log("page loaded...")
var username = document.querySelector("#username");
var remove1 = document.querySelector("#waiting1");
var remove2 = document.querySelector("#waiting2");

function edit(){
username.innerText = "Definitely Not Jane Doe";
}

function rem(){
    remove1.remove();
}

function rem2(){
    remove2.remove();
}
