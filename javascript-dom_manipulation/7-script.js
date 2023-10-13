// Select the header element
const ul = document.querySelector('#list_movies');

async function llamarApi(){
    const response = await fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    const films = await response.json();
    const titles = films.results;
    for (let i = 0; i < titles.length; i++){
        const title = titles[i].title;
        const li = document.createElement('li');
        li.textContent = title;
        ul.appendChild(li);
    }
}
llamarApi();