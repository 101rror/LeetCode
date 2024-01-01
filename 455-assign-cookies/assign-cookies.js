/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s)
{
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    n = g.length
    m = s.length

    let i = 0, j = 0

    while(i < n && j < m)
    {
        if(g[i] <= s[j])
        {
            i += 1
        }
        j += 1
    }

    return i
};