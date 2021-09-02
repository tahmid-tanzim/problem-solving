/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var stack = [], ascii, last;
    for(var i in s) {
        ascii = s.charAt(i).charCodeAt(0);
        if([40, 91, 123].indexOf(ascii) !== -1) {
            stack.push(ascii);
        } else {
            last = stack.pop();
            if(ascii === 41 && last !== 40 || ascii === 93 && last !== 91 || ascii === 125 && last !== 123) {
                return false;
            }
        }
    }
    return !stack.length;
};

console.log(isValid("["));

//"([)]"

/*
*
( - 40
[ - 91
{ - 123
} - 125
] - 93
) - 41
* */