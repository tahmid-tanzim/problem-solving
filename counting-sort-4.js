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

    let n = 20, input = ['0 ab','6 cd','0 ef','6 gh','4 ij','0 ab','6 cd','0 ef','6 gh','0 ij','4 that','3 be','0 to','1 be','5 question','1 or','2 not','4 is','2 to','4 the'];

    let frequency = Array(100).fill(null), i = 0, x, s;

    while(i < n) {
        //[x, s] = readLine().split(' ');

        [x, s] = input[i].split(' ');

        x = parseInt(x);
        (frequency[x] = frequency[x] || []).push(i < (n/2) ? '-' : s);
        i++;
    }


    console.log(frequency.reduce((a, b) => { return b ? a.concat(b) : a;}, []).join(' '));
}

/////////////// ignore below this line ////////////////////
main();
