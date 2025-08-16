/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {
    return {
        toBe: (newVal) => {
            if (newVal === val) {
                return true;
            }
            else {
                throw new Error("Not Equal");
            }
        },
        notToBe: (newVal) => {
            if (val === newVal) {
                throw new Error("Equal");
            }
            else {
                return true;
            }
        }
    }

};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */