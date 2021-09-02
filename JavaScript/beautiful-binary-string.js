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
    //let n = parseInt(readLine()), B = readLine();

    //let n = 7, B = '0101010';
    //let n = 5, B = '01100';
    let n = 10, B = '0100101010';

    let index, count = 0;

    index = B.indexOf('010');

    while(index !== -1) {
        B = B.substr(0, index + 2) + '1' + B.substr(index + 3);
        count++;
        index = B.indexOf('010');
    }

    //process.stdout.writeln(`${index}`);
    console.log(`${count}`);
    console.log(`${B}`);

}

main();
