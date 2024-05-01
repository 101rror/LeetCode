/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch)
{
    let n = word.length
    let idx = 0

    for(let i = 0; i < n; i++)
    {
        if(word[i] == ch)
        {
            idx = i;
            break;
        }
    }

    if(idx == 0)
    {
        return word;
    }
    else
    {
        return word.substring(0, idx + 1).split('').reverse().join('') + word.substring(idx + 1);
    }
};