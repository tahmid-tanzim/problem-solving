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
    //let t = readLine();

    let t = 2, input = ['12', '1012']; // delete

    let count, n, numbers, i, output = [];
    while (t--) {
        //n = parseInt(readLine());
        n = parseInt(input[t]); // delete

        numbers = n.toString().split('').map(Number);
        count = 0;

        for (i = 0; i < numbers.length; i++) {
            if (n % numbers[i] === 0) {
                count++;
            }
        }

        output.push(count);
    }

    console.log(output.join('\n'));
}

/////////////// ignore below this line ////////////////////
main();
