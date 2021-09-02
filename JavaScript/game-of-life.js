/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 * @URL https://leetcode.com/problems/game-of-life/
 */

var countNeighbours = function (board, position, size) {
    var count = 0;
    for (var i = Math.max(0, position.x - 1); i <= Math.min(position.x + 1, size.row - 1); i++) {
        for (var j = Math.max(0, position.y - 1); j <= Math.min(position.y + 1, size.column - 1); j++) {
            if ((i !== position.x || j !== position.y) && board[i][j] === 1) {
                count++;
            }
        }
    }

    return count;
};

var computeNextState = function (originalBoard, updatedBoard, position, neighboursCount) {

    if (originalBoard[position.x][position.y] === 1 && (neighboursCount < 2 || neighboursCount > 3)) {
        updatedBoard[position.x][position.y] = 0;
    }

    if (originalBoard[position.x][position.y] === 0 && neighboursCount === 3) {
        updatedBoard[position.x][position.y] = 1;
    }

    return updatedBoard;
};

var gameOfLife = function (board) {
    var neighboursCount = 0, i, j, size = {
        row: board.length,
        column: board[0].length
    }, updatedBoard = board.map(function (a) {
        return a.slice()
    });

    for (i = 0; i < size.row; i++) {
        for (j = 0; j < size.column; j++) {
            neighboursCount = countNeighbours(board, {x: i, y: j}, size);
            updatedBoard = computeNextState(board, updatedBoard, {x: i, y: j}, neighboursCount);
        }
    }

    for (i = 0; i < size.row; i++) {
        for (j = 0; j < size.column; j++) {
            board[i][j] = updatedBoard[i][j];
        }
    }
};

gameOfLife([
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]);

// Output [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
// Expected [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]