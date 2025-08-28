/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
    return function (x) {
        if (functions.length === 0) {
            return x;
        }

        var ans = functions[functions.length - 1](x);

        for (var i = functions.length - 2; i >= 0; i--) {
            ans = functions[i](ans);
        }
        return ans;
    };
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */