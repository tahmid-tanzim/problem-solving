var dec2bin = function(dec) {
    return (dec >>> 0).toString(2);
};

var hammingWeight = function(n) {
    n = dec2bin(n);
    var count = 0;

    for(var i = 0; i < n.length; i++) {
        parseInt(n[i]) && count++;
    }
    return count;
};

console.log(hammingWeight(11)); // 3