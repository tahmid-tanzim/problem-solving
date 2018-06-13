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
    //let [n, k] = readLine().split(' ').map(Number), c = readLine().split(' ').map(Number);

    let n = 8, k = 2, c = [0, 0, 1, 0, 0, 1, 1, 0]; // 4

    let E = 100, i;
    for (i = 0; i < n; i += k) {
        if(c[i]) {
            E -= 3;
        } else {
            E -= 1;
        }
    }
    console.log(E);
}

/////////////// ignore below this line ////////////////////
main();
