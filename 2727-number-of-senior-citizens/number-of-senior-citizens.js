/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function (details) {
    let count = 0;

    for (let i = 0; i < details.length; i++) {
        let x = parseInt(details[i].substring(11, 13), 10);

        if (x > 60) {
            count += 1;
        }
    }

    return count;
};