var dec2bin = function(dec) {
    return (dec >>> 0).toString(2);
};

var hammingDistance = function(x, y) {
    x = dec2bin(x);
    y = dec2bin(y);

    var diff = Math.abs(x.length - y.length), prefix = "", count = 0, x1, y1;
    while(diff > 0) {
        prefix += "0";
        diff--;
    }

    if(x.length > y.length) {
       y = prefix + y; 
    } else {
       x = prefix + x;
    }

    for(var i = 0; i < x.length; i++) {
        x1 = parseInt(x[i]);
        y1 = parseInt(y[i]);

        if((!x1 && y1) || (x1 && !y1)) {
            count++;
        }

        console.log(x1, y1);
    }
    return count;
};

// console.log(hammingDistance(94, 73));
console.log(hammingDistance(3, 1)); // 1