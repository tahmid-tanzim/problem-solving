var width = 2;// parseInt(readline()); // the number of cells on the X axis
var height = 2; //parseInt(readline()); // the number of cells on the Y axis

const readlines = ['0 0', '0 .'];

for (var i = 0; i < height; i++) {
    var line = readlines[i].split(' '); // width characters, each either 0 or .
    console.log(line);
}

// Write an action using print()
// To debug: printErr('Debug messages...');


// Three coordinates: a node, its right neighbor, its bottom neighbor
console.log('0 0 1 0 0 1');