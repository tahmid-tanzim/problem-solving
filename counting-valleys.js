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
    // let n = parseInt(readLine()), steps = readLine();

    let n = 8, steps = 'UDDDUDUU';

    let i, count = 0, index = 0, flag = false;
    for(i = 0; i < n; i++) {
        if(steps.charAt(i) == 'D') {
            index--;
        } else {
            index++;
        }

        if (index == 0 && flag) {
            count++;
            flag = false;
        } else if (index < 0) {
            flag = true;
        } else {
            flag = false;
        }
    }

    console.log(count);
}

/////////////// ignore below this line ////////////////////

main();