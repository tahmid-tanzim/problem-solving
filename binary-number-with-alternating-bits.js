// https://leetcode.com/problems/binary-number-with-alternating-bits/description/

/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    var binary = n.toString(2),
        output = true,
        first_bit = binary.charAt(0);
    for(var i = 1; i < binary.length; i++) {
        if(i % 2 === 0 && binary.charAt(i) !== first_bit || i % 2 !== 0 && binary.charAt(i) === first_bit) {
            output = false;
            break;
        }
    }
    return output;
};

[5, 7, 11, 10].forEach(function (x) {
    console.log(hasAlternatingBits(x));
});