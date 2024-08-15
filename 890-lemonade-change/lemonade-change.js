/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function (bills) {
    let n = bills.length;
    let c5 = 0, c10 = 0, c15 = 0;

    for (let i = 0; i < n; i++) {
        if (bills[i] === 5) {
            c5 += 1;
        }
        else if (bills[i] === 10) {
            c10 += 1;
            if (c5 === 0) {
                return false;
                break;
            }
            else {
                c5 -= 1;
            }
        }
        else {
            if (c5 >= 1 && c10 >= 1) {
                c5 -= 1;
                c10 -= 1;
            }
            else if (c5 >= 3) {
                c5 -= 3;
            }
            else {
                return false;
            }
        }
    }

    return true;
};