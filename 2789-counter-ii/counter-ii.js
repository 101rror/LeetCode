/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (num) {
    let Counter = num
    return {
        increment: () => ++Counter,
        decrement: () => --Counter,
        reset: () => Counter = num
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */