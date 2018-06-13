/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var dec2bin = function(dec) {
    return (dec >>> 0).toString(2);
};

var findComplement = function(n) {
    n = dec2bin(n);

    // while(n.length < 32) {
    //     n = "0" + n;
    // }

    var i = 0, x = "";
    while(i < n.length) {
        x += 1 - parseInt(n[i]);
        i++;
    }

    return parseInt(x, 2);
};

console.log(findComplement(5)); // 2