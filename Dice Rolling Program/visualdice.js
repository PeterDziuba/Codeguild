"use strict";

function getDiceNumber() {
    return $('#how-many-dice').val();
}

function getADieFace() {
    var aDieFace = Math.floor((Math.random() * 6) + 1);
    return aDieFace;
}

function getADiePicture(number) {
    if (number === 1) {
        return "die_01.gif"
    }
    else if (number === 2) {
        return "die_02.gif"
    }
    else if (number === 3) {
        return "die_03.gif"
    }
    else if (number === 4) {
        return "die_04.gif"
    }
    else if (number === 5) {
        return "die_05.gif"
    }
    else if (number === 6) {
        return "die_06.gif"
    }
}

function makeADie(imageSource) {
    var myDie = $("<img>").attr("src", imageSource).attr("width", 200);
    myDie.on("click", function (event) {
        event.preventDefault();
        replaceADie(myDie);
    })
    return myDie;
}

function replaceADie(aDie) {
    var newDieFace = getADieFace();
    var newDiePic = getADiePicture(newDieFace);
    var newDie = $("<img>").attr("src", newDiePic).attr("width", 200);
    newDie.on("click", function (event) {
        event.preventDefault();
        replaceADie(newDie);
    })
    aDie.replaceWith(newDie);
    displayDiceTotal(countDice);
}

function addDieToPage(aDie) {
    $("div").append(aDie);
}

function everyStepToMakeADie() {
    var dieFace = getADieFace();
    var diePicture = getADiePicture(dieFace);
    var wholeDie = makeADie(diePicture);
    addDieToPage(wholeDie);
}

function removeAllImages() {
    var images = document.getElementsByTagName('img');
    while(images.length > 0) {
        images[0].parentNode.removeChild(images[0]);
    }
}

function countDice() {
    var dieCount = 0;
    $("img").each(function() {  
        var imgsrc = this.src;
        if (imgsrc === "file://localhost/Users/htdzi/Documents/codeguild/die_01.gif") {
            dieCount += 1;
        }
        else if (imgsrc === "file://localhost/Users/htdzi/Documents/codeguild/die_02.gif") {
            dieCount += 2;
        }
        else if (imgsrc === "file://localhost/Users/htdzi/Documents/codeguild/die_03.gif") {
            dieCount += 3;
        }
        else if (imgsrc === "file://localhost/Users/htdzi/Documents/codeguild/die_04.gif") {
            dieCount += 4;
        }
        else if (imgsrc === "file://localhost/Users/htdzi/Documents/codeguild/die_05.gif") {
            dieCount += 5;
        }
        else if (imgsrc === "file://localhost/Users/htdzi/Documents/codeguild/die_06.gif") {
            dieCount += 6;
        }
    });  
    return dieCount;
}

function displayDiceTotal(dieTotal) {
    $("h1").text(dieTotal);
}

function registerHandlers() {
    $("form").on("submit", function(event) {
    event.preventDefault();
    removeAllImages();
    var howManyTimes = getDiceNumber();
    for(var i = 0; i < howManyTimes; i += 1) {
        everyStepToMakeADie();
    }
    displayDiceTotal(countDice);
  })
}

$(document).ready( function() {
  registerHandlers();
});