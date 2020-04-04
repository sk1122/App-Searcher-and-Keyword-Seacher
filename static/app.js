$(document).ready(function(){
    $("select#appstore").change(function(){
        var selectedOption = $(this).children("option:selected").val();
        if (selectedOption == "0") {
            $(".form").show();
        } else if (selectedOption == "1"){
            $(".formApp").show();
        } else {
            $('form').hide();
            $(".formApp").hide();
        }
    });
});


