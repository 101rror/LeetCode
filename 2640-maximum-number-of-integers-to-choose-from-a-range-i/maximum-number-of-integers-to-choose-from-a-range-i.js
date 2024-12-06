/**
 * @param {number[]} banned
 * @param {number} n
 * @param {number} maxSum
 * @return {number}
 */
var maxCount = function(banned, n, maxSum) {
    const st = new Set(banned);
    let arr = [];

    for(let i = 1; i <= n; i++){
        if (!st.has(i)){
            arr.push(i);
        }
    }

    let cursum = 0, count = 0;

    for (const it of arr){
        cursum += it;

        if (cursum <= maxSum){
            count += 1;
        }
        else{
            break;
        }
    }

    return count;
};