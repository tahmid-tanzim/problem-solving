var n = 6;
var inputs = [3, 2, 4, 2, 1, 5];
//var inputs = [5, 3, 4, 2, 3, 1];
//var inputs = [1, 2, 4, 4, 5];

var max = inputs[0];
var min = inputs[0];
var p = 0;

for (var i = 1, vx, vx_1, diff; i < n; i++) {
    vx = inputs[i];
    vx_1 = inputs[i - 1];

    diff = vx - vx_1;
    if(diff < 0 && p === 0) {
        p = diff;
    }

}

// Write an action using print()
// To debug: printErr('Debug messages...');

console.log('Base: ', base);
console.log('Max: ', max);
console.log('Min: ', min);