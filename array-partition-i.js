/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    var sum = 0;
    nums = nums.sort(function(a, b) {
        return a - b;
    });

    for(var i = 0; i < nums.length; i+=2) {
        sum += Math.min(nums[i], nums[i + 1]);
    }

    return sum;
};

console.log(arrayPairSum([1,4,3,2]));