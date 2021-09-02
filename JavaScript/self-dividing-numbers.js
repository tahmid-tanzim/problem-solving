/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    var arr = [];
    for(var i = left, number, remainder, isSelfDividingNumbers; i <= right; i++) {
        console.log(i);

        number = i;
        isSelfDividingNumbers = true;
        while (number > 0) {
            remainder = number % 10;
            console.log('1, ', remainder);
            if(remainder === 0 || i % remainder !== 0) {
                isSelfDividingNumbers = false;
                break;
            }
            number = (number - remainder) / 10;
        }

        if(isSelfDividingNumbers) {
            arr.push(i);
        }
    }

    return arr;
};

console.log(selfDividingNumbers(1, 22));