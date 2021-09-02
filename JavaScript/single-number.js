/**
 * @param {number[]} nums
 * @return {number}
 */
const singleNumber = nums =>  {
    nums.sort((a,b) => a - b);

    let i, num;
    for(i = 0; i < nums.length - 2; i += 2) {
        if(nums[i] !== nums[i + 1]) {
            num = nums[i];
            break;
        }
    }

    return typeof num !== 'undefined' ? num : nums.pop();
};

console.log(singleNumber([1,0,1]));