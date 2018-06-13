// https://leetcode.com/problems/toeplitz-matrix/description/

/**
 * @param {number[][]} matrix
 * @return {boolean}
 */


var isToeplitzMatrix = function(matrix) {
    var M = matrix.length;
    var N = matrix[0].length;
    var diagonals = M + N - 1;
    var flag = 'True';

    for(var i = 0, start, container; i < diagonals; i++) {
        start = {
            row: i < M ? M - i - 1 : 0,
            column: i >= M ? i - M + 1 : 0
        };

        container = matrix[start.row++][start.column++];
        //console.log(i + '. Diagonal {x: ' + start.row + ', y: ' + start.column + '}');

        while(start.row < M && start.column < N) {
            if(container !== matrix[start.row][start.column]) {
                flag = 'False';
                break;
            }

            start.row++;
            start.column++;
            //console.log('\t'+ container +' | {x: ' + start.row + ', y: ' + start.column + '}');
        }

        if(flag === 'False') {
            break;
        }
    }

    return flag;
};

console.log(isToeplitzMatrix(/*[[1,2,3,4],[5,1,2,3],[9,5,1,2]]*/ [[1,2],[2,2]]));