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
    //let n = parseInt(readLine()), px = readLine().split(' ').map(Number), x = 0;

    let n = 3, px = [2, 3 ,1]; // 4

    let x = 0;

    while(x < n) {
        console.log(px.indexOf(px.indexOf(x + 1) + 1) + 1);
        x++;
    }



}

/////////////// ignore below this line ////////////////////
main();
