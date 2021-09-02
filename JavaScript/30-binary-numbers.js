/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var main = function(n) {
    // var n = parseInt(readLine());
    n = (n >>> 0).toString(2);

    var count = 0, max = 0;

    for(var i = 0; i < n.length; i++) {
        if(n[i] === '1') {
            count++;

            if(count > max) {
                max = count;
            }
        } else {
            count = 0;
        }
    }

    return max;
};

console.log(main(13)); // 1