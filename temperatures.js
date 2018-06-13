// var n = 16;
// var inputs = [0, 7, -10, 13, 8, 4, 0, -7, -12, -3, 3, -9, 6, -6, 7, -1];

var n = 0;
var inputs = [];


if(n) {
    var min = {
        temp: 0,
        abs: 0
    };

    for(var i = 0, temp, abs; i < n; i++) {
        temp = inputs[i];
        // Check temp in non zero
        if(temp) {
            abs = Math.abs(temp);
            if((min.abs === 0) || (min.abs !== 0 && abs <= min.abs)) {
                min = {
                    temp: abs === min.abs ? Math.max(temp, min.temp) : temp,
                    abs: abs
                }
            }
        }
    }

    console.log(min.temp);
} else {
    console.log(0);
}

