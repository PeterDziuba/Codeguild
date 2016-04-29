"use strict";

var pair_list = [5, 7, 1, -1, 12, 3, 4, 6, 22, 11, 2, 0];

var notContains =  function(a, obj) {
    for (var i = 0; i < a.length; i++) {
        if (a[i] === obj) {
            return false;
        }
    }
    return true;
}

var findSumPairs = function(list, sum) {
    var func_pair_list = [];
    var my_item_list = [];
    for (var i=0; i<list.length; i++) {
        for (var j=0; j<list.length; j++) {
            if (sum - list[i] === list[j]) {
                var my_list = [list[i], list[j]];
                if((notContains(my_item_list, list[i])) && (notContains(my_item_list, list[j]))) {
                    func_pair_list.push(my_list);
                    my_item_list.push(list[i]);
                    my_item_list.push(list[j]);
                };
            };
        }
    }
    return func_pair_list
};

var my_sum = findSumPairs(pair_list, 10);
for(var i = 0; i < my_sum.length; i++){
    console.log(my_sum[i]);
}