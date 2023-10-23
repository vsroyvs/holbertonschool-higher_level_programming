$(function() {
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.hbtn.io/api/films/?format=json',
        success: (data) => {
            const titles = data.results;
            console.log('success', titles);
            for (let i = 0; i < titles.length; i++) {
                const title = titles[i].title;
                $('#list_movies').append(`<li>${title}</li>`);
            }
        },
    });
});