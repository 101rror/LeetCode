/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxK = function(nums)
{
    nums.sort((a, b) => a - b);
    n = nums.length;

    for(let i = 0; i < n; i++)
    {
        if(nums[i] < 0)
        {
            for(let j = 0; j < n; j++)
            {
                if(nums[i] * -1 == nums[j])
                {
                    return nums[i] * -1;
                }
            }
        }
    }

    return -1
};