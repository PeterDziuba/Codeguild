"use strict";

function makeAMole() {
    var newMole = $("<img src='mole.jpg' alt='mole'>");
    newMole.on("click", function (event) {
        event.preventDefault();
        var newMoleHole = $("<img src='hole.jpg' alt='mole hole'>");
        newMole.replaceWith(newMoleHole);
        molesWhacked += 1;
        molesWhackedCounter();
    })
    return newMole;
}

var molesWhacked = 0;

function molesWhackedCounter() {
    $("#moles-whacked").text(molesWhacked);
}

var moleSpots = ["#row1column1 img", "#row2column1 img", "#row3column1 img",
                 "#row4column1 img", "#row1column2 img", "#row2column2 img",
                 "#row3column2 img", "#row4column2 img", "#row1column3 img",
                 "#row2column3 img", "#row3column3 img", "#row4column3 img",
                 "#row1column4 img", "#row2column4 img", "#row3column4 img",
                 "#row4column4 img", "#row1column5 img", "#row2column5 img",
                 "#row3column5 img", "#row4column5 img"]

function dropAMole(location) { 
    var newMole = makeAMole();
    location.replaceWith(newMole);
}
function whereToDrop () {
   var myIndex = Math.floor((Math.random() * 19) + 0);
   var myLocation = moleSpots[myIndex];
   console.log(myLocation);
   myLocation = $(myLocation);
   dropAMole(myLocation);
}

function intervalDrop () {
    setInterval(whereToDrop, 1000);
}


$(document).ready(function() {
    intervalDrop();
});