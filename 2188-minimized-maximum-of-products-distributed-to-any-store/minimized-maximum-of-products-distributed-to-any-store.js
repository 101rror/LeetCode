/**
 * @param {number} n
 * @param {number[]} quantities
 * @return {number}
 */
var minimizedMaximum = function (n, quantities) {
    var low = 1;
    var high = Math.max(...quantities);
    var count = 0;

    const storesNeeded = (x) => {
        return quantities.reduce((sum, quantity) => sum + Math.ceil(quantity / x), 0);
    };

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const need = storesNeeded(mid);

        if (need <= n){
            count = mid;
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }

    return count;
};