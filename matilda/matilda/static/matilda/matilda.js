"use strict";

$("#user-word-form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
        url: "/count",
        data: { w : $("#user-word").val()},
        type: 'GET',
        success: function(result) {
            $("#div1").append(result);
            $("#div1").append("<br>")
        }
    })
})