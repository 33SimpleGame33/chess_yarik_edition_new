$('.element__button').click(function(){
    let t = $(this)
    $(this).attr('winner', 'true')
    $(this).parent().children().attr('disabled', '')
    let data = {
        'game':$(this).attr('game'),
        'winner':$(this).val(),
    }
    $.ajax({
        method: 'GET',
        data: data,
        dataType: 'json',
        url: 'set_winner_ajax',
        success: function (response) {
            let next = t.parent().parent().parent().find('.element__button[game=' + response.next_game + ']')
            if(next.first().val() == ''){
                next.first().text(t.text()).val(t.val()).attr('winner', 'false')
            } else {
                next.last().text(t.text()).val(t.val()).attr('winner', 'false')
                next.removeAttr('disabled')
            }
        },
    });
})