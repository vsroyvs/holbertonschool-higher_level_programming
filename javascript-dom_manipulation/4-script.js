// Select the header element
const ul = document.querySelector('.my_list');
const add_item = document.querySelector('#add_item');
const li = document.createElement('li');
const text = document.createTextNode('Item')


function add_node(){
    // Inserto el texto al nodo
    li.appendChild(text);
    // Inserto el nodo al padre
    ul.appendChild(li)
}

add_item.addEventListener('click', add_node);
