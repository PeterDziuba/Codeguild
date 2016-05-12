"use strict";
function postJokes(){
    $("#funny-form").on("submit", function(event) {
        event.preventDefault();
        $.ajax({
            url: "/jokebank/",
            data: {setup: $("#setup").val(),
                   punchline: $("#punchline").val()},
            type: "POST",
        })
        $("#setup").val("");
        $("#punchline").val("");
    })
}





// $("#funny-form").on("submit", function(event) {
//     event.preventDefault();
//     $.ajax({
//         url: "/jokebank/",
//         data: {setup: $("#setup").val(),
//                punchline: $("#punchline").val()},
//         type: "POST",
//     })
//     $("#setup").val("");
//     $("#punchline").val("");
// })


$(document).ready(function(){
    $("a.visible").on("click", function(event) {
        event.preventDefault();
        $(event.target).children().removeClass("invisible");
    })
    postJokes();
});

