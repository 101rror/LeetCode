/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    let sum = 0;

    for(let i = 1; i < s.length; i++){
        let x = s.charCodeAt(i);
        let y = s.charCodeAt(i - 1);
        let ab = Math.abs(x - y);

        sum += ab;
    }

    return sum;
};