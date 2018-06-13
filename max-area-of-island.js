// https://leetcode.com/problems/max-area-of-island/description/

// DFS

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
    var val = null,
        count = 0,
        row = grid.length,
        column = grid[0].length;

    for (var x = 0; x < row; x++) {
        for (var y = 0; y < column; y++) {
            val = grid[x][y];
            if (val !== 0) {
                if (val === 1) {
                    count++;
                    // Self
                    grid[x][y] = 2;
                }

                // Right
                if (y + 1 < column && grid[x][y + 1] === 1) {
                    grid[x][y + 1] = 2;
                }

                // Bottom
                if (x + 1 < row && grid[x + 1][y] === 1) {
                    grid[x + 1][y] = 2;
                }
                console.log(count);
                console.log(grid);
                console.log('\n');
            }
        }
    }

    return count;
};

console.log(maxAreaOfIsland(
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ])
);