/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function(nums, k)
{
    let n = nums.length;
    let mx = Math.max(...nums);

    let i = 0, j = 0, count = 0, ans = 0;

    while(j < n)
    {
        if(nums[j] == mx)
        {
            count++;
        }

        if(count >= k)
        {
            while(count >= k)
            {
                ans += (n - j);

                if(nums[i] == mx)
                {
                    count--;
                }
                i++;
            }
        }
        j++;
    }

    return ans;
};