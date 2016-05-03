"use strict";

var myName = $("#user-name");
var myBirthday = $("#birth-day");
var myPhoneNumber = $("#phone-number");

$("#user-name").on("blur", function (event) {
    event.preventDefault();
    if (isValidName(myName)) {
        $("#user-name").removeClass("error-class");
        $("#warning-div-1").empty();
    }
    else if (!isValidName(myName)) {
        $("#user-name").addClass("error-class");
        $("#warning-div-1").append("<p class='warning'> Enter Name as First Last, Without Numbers</p>");
    }
})

$("#birth-day").on("blur", function (event) {
    event.preventDefault();
    if (isValidBirthDay(myBirthday)) {
        $("#birth-day").removeClass("error-class");
        $("#warning-div-2").empty();
    }
    else if (!isValidBirthDay(myBirthday)) {
        $("#birth-day").addClass("error-class");
        $("#warning-div-2").append("<p class='warning'> Enter Birthday as YYYY-MM-DD, Without Letters </p>");
    }
})

$("#phone-number").on("blur", function (event) {
    event.preventDefault();
    if (isValidPhoneNumber(myPhoneNumber)) {
        $("#phone-number").removeClass("error-class");
        $("#warning-div-3").empty();
    }
    else if (!isValidPhoneNumber(myPhoneNumber)) {
        $("#phone-number").addClass("error-class");
        $("#warning-div-3").append("<p class='warning'> Enter Phone Number as 555-555-5555, Without Letters </p>");
    }
})
        

$("form").on("submit", function (event) {
    event.preventDefault();
    console.log(myName.val());
    console.log(myBirthday.val());
    console.log(myPhoneNumber.val());
    if((isValidName(myName)) && (isValidBirthDay(myBirthday)) && (isValidPhoneNumber(myPhoneNumber))){
        $("#form-header-success").append("<p>Successfully Submitted</p>");
        $("#form-header-failure").empty();
    }
    else {
        $("#form-header-failure").append("<p>Something Went Wrong! Try Again</p>")
        $("#form-header-success").empty();
    }
})

var Contains =  function(a, obj) {
    for (var i = 0; i < a.length; i++) {
        if (a[i] === obj) {
            return true;
        }
    }
    return false;
}

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function isValidName(name) {
    var aName=name.val();
    aName.split();
    if (aName.length === 0) {
        return false;
    }
    else if (aName.length > 0) {
        for(var i = 0; i < aName.length; i += 1) {
            if (isNumeric(aName[i])) {
                return false;
            }
        }
        if (Contains(aName, " ")) {
            return true;
        }
    }
    return false;
}

function isValidBirthDay(birthDay) {
    var aBirthDay = birthDay.val();
    aBirthDay.split();
    if (aBirthDay.length === 0){
        return false;
    }
    else if (aBirthDay.length === 10){
        for(var i = 0; i < 4; i += 1) {
            if (!isNumeric(aBirthDay[i])) {
                return false;
            }
        }
        for(var i = 5; i < 6; i += 1) {
            if (!isNumeric(aBirthDay[i])) {
                return false;
            }
        }
        for(var i = 8; i < 9; i += 1) {
            if (!isNumeric(aBirthDay[i])) {
                return false;
            }
        }
        if (aBirthDay[4] === "-") {
            if (aBirthDay[7] === "-") {
                return true;
            }
        }
    }
    return false;
}

function isValidPhoneNumber(phoneNumber) {
    var aPhoneNumber = phoneNumber.val();
    aPhoneNumber.split();
    if (aPhoneNumber.length === 0){
        return false;
    }
    else if (aPhoneNumber.length === 12){
        for(var i = 0; i < 3; i += 1) {
            if (!isNumeric(aPhoneNumber[i])) {
                return false;
            }
        }
        for(var i = 4; i < 7; i += 1) {
            if (!isNumeric(aPhoneNumber[i])) {
                return false;
            }
        }
        for(var i = 8; i < aPhoneNumber.length; i += 1) {
            if (!isNumeric(aPhoneNumber[i])) {
                return false;
            }
        }
        if (aPhoneNumber[3] === "-") {
            if (aPhoneNumber[7] === "-") {
                return true;
            }
        }
    }
    return false;
}