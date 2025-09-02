/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
let addTwoPromises = async function (promise1, promise2) {
    let sum = 0;

    sum += await promise1;
    sum += await promise2;

    return Promise.resolve(sum);
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */