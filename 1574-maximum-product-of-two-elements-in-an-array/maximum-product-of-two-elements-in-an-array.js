/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums)
{
    nums.sort((a, b) => b - a)

    let x = nums[0] - 1
    let y = nums[1] - 1

    let ans = (x * y)

    return ans
};