/**
 *   Return the second largest number in the array.
 *   @param {Number[]} nums - An array of numbers.
 *   @return {Number} The second largest number in the array.
 **/
function getSecondLargest(nums) {
    nums = nums
        .sort((a, b) => a - b)
        .filter((item, pos) => nums.indexOf(item) == pos);
    console.log(nums[nums.length - 2]);
}

getSecondLargest([3, 6, 2, 6, 5]);