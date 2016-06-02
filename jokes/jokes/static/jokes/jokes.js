"use strict";
function postJokes() {
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

function showJokes() {
   $("a.visible").on("click", function(event) {
        event.preventDefault();
        $(event.target).children().removeClass("invisible");
    }) 
}


$(document).ready(function(){
    showJokes();
    postJokes();
});

