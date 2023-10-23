$(function() {
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
        success: (data) => {
            console.log('success', data);
            $('#character').text(data.name);
        }
    });
});