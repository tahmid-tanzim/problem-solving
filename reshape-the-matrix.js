// https://leetcode.com/problems/reshape-the-matrix/description/

/**
 * @param {number[][]} nums
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(nums, r, c) {
    var rx = nums.length, cx = nums[0].length;
    if(rx * cx !== r * c) {
        return nums;
    }

    var flattened_nums = nums.reduce((acc, cur) => acc.concat(cur), []);
    var output = [];

    for(rx = 0; rx < r; rx++) {
        output[rx] = [];
        for(cx = 0; cx < c; cx++) {
            output[rx][cx] = flattened_nums.shift();
        }
    }

    return output;
};

//console.log(matrixReshape([[1,2], [3,4]], 4, 1));
console.log(matrixReshape([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 8, 2));