/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var dec2bin = function(dec) {
    return (dec >>> 0).toString(2);
};

var reverseBits = function(n) {
    n = dec2bin(n);

    while(n.length < 32) {
        n = "0" + n;
    }

    var x = "";
    for(var i = n.length - 1 ; i >=0 ; i--) {
        x += n[i];
    }

    return parseInt(x, 2);
};

console.log(reverseBits(43261596)); // 3