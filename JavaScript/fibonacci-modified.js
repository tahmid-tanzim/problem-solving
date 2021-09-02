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
function fibonacci(t1, t2, n) {

    if(n === 1) {
        return t1;
    } else if(n === 2) {
        return t2;
    } else {
        return fibonacci(t1, t2, n - 2) + Math.pow(fibonacci(t1, t2, n - 1), 2);
    }

}

function main() {
    //var x = readLine().split(' ');
    var x = '0 1 5';
    var [t1, t2, n] = x.split(' ').map(Number);

    console.log(fibonacci(t1, t2, n));
}

main();

