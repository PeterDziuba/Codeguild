"using strict";

var taxFunction = function(principle_amount) {
    if (principle_amount < 3351) {
        return (0.05 * principle_amount);
    }

    else if ((principle_amount > 3350) && (principle_amount < 8401)) {
        var new_principle = principle_amount - 3350;
        return ((167.5) + (new_principle * 0.07));
    }

    else if ((principle_amount > 8400) && (principle_amount < 125001)) {
        var new_principle = principle_amount - 8400;
        return ((167.5 + 353.50) + (new_principle * 0.09));
    }
    else { 
        var new_principle = principle_amount - 125000;
        return ((167.5 + 353.50 + 10494) + (new_principle * 0.099));
    }

};

var our_principle_amount = 125001;

console.log(taxFunction(our_principle_amount));