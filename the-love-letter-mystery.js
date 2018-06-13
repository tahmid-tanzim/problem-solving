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
    //let T = parseInt(readLine()), s, i, half, end, sum, output = [];

    let T = parseInt('4'), s, input = ['cba', 'abcd', 'abcba', 'abc'], i, half, end, sum, output = [];

    while (T--) {
        //s = readLine();

        s = input[T];
        sum = 0;
        end = s.length - 1;
        half = Math.floor(s.length / 2);
        for (i = 0; i < half; i++) {
            sum += Math.abs(s.charAt(i).charCodeAt(0) - s.charAt(end - i).charCodeAt(0));
        }
        output.push(sum);
    }

    console.log(output.join('\n'));
}

/////////////// ignore above this line ////////////////////
main();
