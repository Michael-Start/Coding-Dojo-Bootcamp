var likes = 3;
likesElement = document.querySelector("#likes");

console.log(likes);

function add1(){
    likes++;
    likesElement.innerText = likes + " likes"
    console.log(likes);
}
