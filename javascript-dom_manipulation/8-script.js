
async function llamarApi(){
    const tag = document.querySelector('#hello');
    const response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    const json = await response.json();
    tag.textContent = json.hello;
    
}
document.addEventListener("DOMContentLoaded", llamarApi);