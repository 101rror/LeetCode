/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t)
{
    n = [...s].sort().join('');
    m = [...t].sort().join('');

    if(n == m)
    {
        return true
    }
    return false
};