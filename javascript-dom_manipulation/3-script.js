// Select the header element
const header = document.querySelector('.green');
const toggle_header = document.querySelector('#toggle_header');

function changeColor(){
    if (header.className == 'green'){
        header.classList.replace('green', 'red');
    } else{
        header.classList.replace('red', 'green');
    }
}

toggle_header.addEventListener('click', changeColor);
