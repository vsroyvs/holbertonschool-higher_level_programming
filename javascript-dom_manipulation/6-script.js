// Select the header element
const tag = document.querySelector('#character');

async function llamarApi(){
    const response = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    const json = await response.json();
    const name = json.name;
    tag.textContent = name;
}
llamarApi();