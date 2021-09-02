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
    //let p = parseInt(readLine()), a, b;

    let p = 2, a, b, input = [['hi', 'world'], ['hello', 'world']];

    let i, found, output = [];
    while(p--) {
        //a = readLine();
        //b = readLine();

        [a, b] = input[p];
        found = false;

        for(i in a) {
            if(b.indexOf(a.charAt(i)) > -1) {
                found = true;
                break;
            }
        }

        output.push(found ? 'YES' : 'NO');
    }

    console.log(output.join('\n'));
}

/////////////// ignore below this line ////////////////////

main();