"use strict";

var namesToAges = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
};

var my_ob = {};
for (var name in namesToAges) {
    var tracker = namesToAges[name];
    if (tracker in my_ob) {
        my_ob[tracker] += 1;
    }
    else {
        my_ob[tracker] = 1;
    }
};

var sortable = {};
for (var number in my_ob) {
    var flipper = my_ob[number]
    sortable[flipper] = number;
};

var sort_array = [];
for (var count in sortable) {
    sort_array.push(count)
};

sort_array.sort(function(a, b){return a-b});
var final_number = sort_array[0];
console.log("The least common number is:")
console.log(sortable[final_number]);

