process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////
function quick_sort(array) {
    if(array.length === 0) return array;

    let pivote = array[0], left = [], right = [];

    for (let i = 1; i < array.length; i++) {
        if (array[i] >= pivote) {
            right.push(array[i]);
        } else {
            left.push(array[i]);
        }
    }

    let bundle = quick_sort(left).concat(pivote, quick_sort(right));
    if(bundle.length > 1) {
        console.log(bundle.join(' '));
    }
    return bundle;
}

function main() {
    // let Size = parseInt(readLine());
    // let Arr = readLine().split(' ').map(Number);

    let Size = 7, Arr = [5, 8, 1, 3, 7, 9, 2];
    //let Size = 6, Arr = [23, 42, 4, 16, 8, 15];

    quick_sort(Arr);
}

/////////////// ignore below this line ////////////////////
main();
