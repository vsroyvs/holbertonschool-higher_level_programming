$('#add_item').click(function() {
    const li = $('<li>', {
        text: 'Item'
    });
    $('.my_list').append(li);
});
