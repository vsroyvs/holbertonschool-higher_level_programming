// Select the header element
const header = document.querySelector('#red_header');
function changeColor(){
    header.style.color = '#FF0000';
}
// Update the text color to red
header.addEventListener('click', changeColor);
