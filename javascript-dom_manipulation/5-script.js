// Select the header element
const header = document.querySelector('header');
const update_header = document.querySelector('#update_header');
const text = 'New Header!!!'


function change_text(){
    // Inserto el texto al nodo
    header.textContent = text;
}

update_header.addEventListener('click', change_text);
