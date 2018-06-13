// https://leetcode.com/problems/next-greater-element-i/description/
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    var output = [], index;

    for(var i in nums1) {
        index = nums2.indexOf(nums1[i]) + 1;
        output[i] = -1;
        while(index < nums2.length) {
            if(nums2[index] > nums1[i]) {
                output[i] = nums2[index];
                break;
            }
            index++;
        }
    }
    return output;
};

//console.log(nextGreaterElement([4,1,2], [1,3,4,2]));
console.log(nextGreaterElement([2, 4], [1,2,3,4]));