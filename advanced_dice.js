"use strict";

function getDiceSides() {
    return $("#how-many-sides").val();
}
var myCounter = 0;
function makeDice(number) {
    var aDieFace = Math.floor((Math.random() * number) + 1);
    myCounter += aDieFace;
    $("h1").text(myCounter);
    aDieFace = aDieFace.toString();
    var aDieFaceParagraph = $("<p></p>").append(aDieFace);
    aDieFaceParagraph.on("click", function (event) {
        event.preventDefault();
        myCounter -= aDieFace;
        $("h1").text(myCounter);
        replaceADie(aDieFaceParagraph, number);
    })
    var aDieBox = $("<div class='die-box'></div>").append(aDieFaceParagraph);
    var xForBox = $("<p>X</p>");
    xForBox.on("click", function (event) {
        event.preventDefault();
        aDieBox.remove();
        myCounter -= aDieFace;
        $("h1").text(myCounter);
    })
    aDieBox.append(xForBox);
    return aDieBox;
}

function replaceADie(aDie, number) {
    var newDieFace = Math.floor((Math.random() * number) + 1);
    myCounter += newDieFace;
    $("h1").text(myCounter);
    var newDieFaceParagraph = $("<p></p>").append(newDieFace);
    newDieFaceParagraph.on("click", function (event) {
        event.preventDefault();
        myCounter -= newDieFace;
        $("h1").text(myCounter);
        replaceADie(newDieFaceParagraph, number);
    })
    aDie.replaceWith(newDieFaceParagraph);
}


$("form").on("submit", function (event) {
    event.preventDefault();
    var myNumber = getDiceSides();
    var myDie = makeDice(myNumber);
    $("#die-box").append(myDie);
})