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
    // let n = parseInt(readLine());

    let n = 10, input = ['4 that','3 be','0 to','1 be','5 question','1 or','2 not','4 is','2 to','4 the'];

    let frequency = Array(100).fill(0), i = 0, x, output = [];

    while(i < n) {
        //[x] = readLine().split(' ');

        [x] = input[i];
        x = parseInt(x);
        frequency[x]++;

        i++;
    }

    x = 0;
    for(i = 0; i < frequency.length; i++) {
        x += frequency[i];
        output.push(x);
    }

    console.log(output.join(' '));
}

/////////////// ignore below this line ////////////////////
main();
