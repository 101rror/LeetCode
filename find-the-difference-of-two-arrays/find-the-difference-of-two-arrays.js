/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
const findDifference = function(nums1, nums2)
{
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);

    const ans = [[], []];

    for (const i of set1)
    {
        if (!set2.has(i))
        {
            ans[0].push(i);
        }
    }

    for (const i of set2)
    {
        if (!set1.has(i))
        {
            ans[1].push(i);
        }
    }

    return ans;

};