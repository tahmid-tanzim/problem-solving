// https://leetcode.com/problems/distribute-candies
/**
 * @param {number[]} candies
 * @return {number}
 */
var distributeCandies = function(candies) {
    var kind = {};

    for(var i in candies) {
        kind[candies[i]] += (kind[candies[i]] || 0);
    }

    return kind;
};

console.log(distributeCandies([2,1,2,3,1,3]));

/**
 * Input: [1,1,2,2,3,3]
 * Output: 3
 * ----------------------
 * Input: [1,1,2,3]
 * Output: 2
 * */