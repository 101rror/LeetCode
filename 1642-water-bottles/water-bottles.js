/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    let div = Math.floor((numBottles - 1) / (numExchange - 1));
    let ans = numBottles + div;

    return ans;
};