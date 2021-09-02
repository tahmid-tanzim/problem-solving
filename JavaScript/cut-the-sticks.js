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
    //let n = parseInt(readLine()),
    //    a = readLine().split(' ').map(Number);

    //let n = 6, a = [5, 4, 4, 2, 2, 8];
    let n = 8, a = [1, 2, 3, 4, 3, 3, 2, 1];

    let min, i;
    while(a.length > 0) {
        min = Math.min( ...a );
        console.log(a.length);

        for(i in a) {
            a[i] -= min;
        }
        a = a.filter(x => x !== 0);
    }
}

/////////////// ignore below this line ////////////////////

main();