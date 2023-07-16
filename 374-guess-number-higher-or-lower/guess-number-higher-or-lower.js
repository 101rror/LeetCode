let guessNumber = function(n)
{
    let first = 1;
    let last = n;
    while (first <= last)
    {
        let mid = Math.ceil(first + (last - first) / 2);
        let pick = guess(mid)

        if (pick == 0)
        {
            return mid;
        }
        else if (pick < 0)
        {
            last = mid - 1;
        } 
        else
        {
            first = mid + 1;
        }
    }
    
    return -1;
};