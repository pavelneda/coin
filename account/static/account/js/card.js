$(document).ready(function () {
    $("#ajax-create-card").click(function () {
        $.ajax({
            type: 'GET',
            async: true,
            url: '/account/ajax-card',
            success: function (data) {
                $("#ajax-create-card").remove();
                $("#card-number").text(data['num_of_card']);
                $("#card-cvv").text(data['cvv']);
                $("#card-date").text(data['date']);
            },
            dataType: 'json',
        });
    });
});

termInput = document.querySelector('#form_id_term');
percentInput = document.querySelector('#formid_percent');

termInput.addEventListener('change', () => {
    if (termInput.value == 3){
        percentInput.value = 15;
    }else if(termInput.value == 6){
        percentInput.value = 18;
    }else if(termInput.value == 12){
        percentInput.value = 20;
    }else if(termInput.value == 24){
        percentInput.value = 25;
    }
});