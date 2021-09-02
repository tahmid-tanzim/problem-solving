/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    for (var i = 0, x = 0, y = 0; i < moves.length; i++) {
        switch (moves.charAt(i)) {
            case 'U':
                y++;
                break;
            case 'D':
                y--;
                break;
            case 'L':
                x--;
                break;
            case 'R':
                x++;
                break;
        }
    }
    return x === 0 && y === 0;
};

console.log(judgeCircle('LL'));