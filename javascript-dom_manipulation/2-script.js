// Select the header element
const header = document.querySelector('header');
const tag = document.querySelector('#red_header');

function changeColor(){
    header.classList.add('red');
}

tag.addEventListener('click', changeColor);
