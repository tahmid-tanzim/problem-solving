/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    for (var i = 0, count = 0; i < S.length; i++) {
        if(J.indexOf(S.charAt(i)) !== -1) {
            count++;
        }
    }
    return count
};

console.log(numJewelsInStones("aA", "aAAbbbb"));