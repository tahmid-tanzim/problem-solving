// https://leetcode.com/problems/island-perimeter/description/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function (grid) {
    var perimeter = 0,
        r = grid.length,
        c = grid[0].length;

    for(var x = 0; x < r; x++) {
        for(var y = 0; y < c; y++) {
            if(grid[x][y]) {
                // Top
                if(x - 1 < 0 || !grid[x - 1][y]) {
                    perimeter++;
                }

                // Bottom
                if(x + 1 >= r || !grid[x + 1][y]) {
                    perimeter++;
                }

                // Right
                if(y + 1 >= c || !grid[x][y + 1]) {
                    perimeter++;
                }

                // Left
                if(y - 1 < 0 || !grid[x][y - 1]) {
                    perimeter++;
                }
            }
        }
    }

    return perimeter;
};

console.log(islandPerimeter(
    [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    )
);