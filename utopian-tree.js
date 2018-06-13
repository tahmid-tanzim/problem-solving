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
function calculate_height(n) {
    if (n === 0) return 1;
    return n % 2 === 0 ? calculate_height(n - 1) + 1 : calculate_height(n - 1) * 2;
}

function main() {
    //let t = parseInt(readLine());

    let t = 3, input = ['0', '1', '4'];

    let n, output = [];
    while (t--) {
        //n = parseInt(readLine());
        n = parseInt(input[t]);
        output.push(calculate_height(n))
    }

    console.log(output.join('\n'));

}

/////////////// ignore below this line ////////////////////
main();
