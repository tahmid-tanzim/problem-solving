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

function main() {
    // let n = parseInt(readLine()), a = readLine().split(' ').map(Number);

    //let n = 6, a = [7, 1, 3, 4, 1, 7]; //3
    //let n = 5, a = [1, 2, 3, 4, 5]; // -1
    let n = 5, a = [1, 9, 3, 9, 9, 5]; // 1

    let min = -1, i, j, diff, index = {};
    for(i = 0; i < n; i++) {
        (index[a[i]] = index[a[i]] || []).push(i);
    }

    for(i in index) {
        if(index[i].length > 1) {
            for(j = 0; j < index[i].length - 1; j++) {
                diff = Math.abs(index[i][j] - index[i][j + 1]);
                if(min > diff || min == -1) {
                    min = diff;
                }
            }
        }
    }

    console.log(min);
}

/////////////// ignore below this line ////////////////////

main();