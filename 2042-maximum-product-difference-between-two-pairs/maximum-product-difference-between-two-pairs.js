/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums)
{
    nums.sort(function(a, b){return a - b})
    let n = nums.length

    let a = nums[0]
    let b = nums[1]
    let c = nums[n - 2]
    let d = nums[n - 1]

    let ans = (c * d) - (a * b)

    return ans
};