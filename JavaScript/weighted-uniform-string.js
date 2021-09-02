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
function getUniformSubstring(string) {
    let freq = [], prev = null, char;

    for (let i = 0; i < string.length; i++) {
        char = string.charAt(i);

        if (prev === char) {
            freq.push(freq[freq.length - 1] + char.charCodeAt(0) - 96);
        } else {
            freq.push(char.charCodeAt(0) - 96);
            prev = char;
        }
    }

    return freq;
}

function main() {
    //let s = readLine(),
    //    n = parseInt(readLine()), x;

    let s = 'abccddde', x,
        n = 6, input = [10, 9, 5, 12, 3, 1];

    const weight = getUniformSubstring(s);
    //const weight = [1, 2, 3, 6, 4, 8, 12, 5];

    //console.log(weight);


    while (n--) {
        //x = parseInt(readLine());

        x = input[n];
        console.log(weight.indexOf(x) !== -1 ? 'Yes' : 'No');
    }
}

main();
