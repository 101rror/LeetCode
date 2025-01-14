/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function (A, B) {
    const n = A.length;
    let seenA = new Set();
    let seenB = new Set();
    let common = new Set();
    let C = new Array();

    for (let i = 0; i < n; i++) {
        seenA.add(A[i]);
        seenB.add(B[i]);

        if (seenA.has(B[i])) {
            common.add(B[i]);
        }
        if (seenB.has(A[i])) {
            common.add(A[i]);
        }
        C.push(common.size);
    }
    
    return C;
};