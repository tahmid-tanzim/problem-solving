function getMaxLessThanK(n, k) {
    let output = 0, bitwise_AND;
    for (let a = 1; a < n; a++) {
        for (let b = a + 1; b <= n; b++) {
            bitwise_AND = a & b;
            // Maximum possible value of a & b < k for any a < b in sequence S.
            if(bitwise_AND > output && bitwise_AND < k) {
                output = bitwise_AND;
            }
        }
    }
    return output;
}

(input => {
    input.forEach(x => {
        console.log(getMaxLessThanK(...x));
    });
})([
    [5, 2],
    [8, 5],
    [2, 2]
]);
