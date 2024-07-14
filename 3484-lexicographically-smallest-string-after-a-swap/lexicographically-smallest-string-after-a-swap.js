/**
 * @param {string} s
 * @return {string}
 */
var getSmallestString = function(s) {
    var arr = [];

    for(let i = 0; i < s.length; i++){
        arr.push(Number(s[i]));
    }

    let n = arr.length;

    for(let i = 0; i < n - 1; i++){
        let x = arr[i];
        let y = arr[i + 1];

        if((x & 1) === (y & 1) && x > y){
            arr[i] = y;
            arr[i + 1] = x;
            break;
        }
    }

    return arr.join("");
};