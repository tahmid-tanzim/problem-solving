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
function palindrome(str) {
    let index = -1, i, size = str.length;
    for (i = 0; i < Math.floor(size / 2); i++) {
        if (str.charAt(i) !== str.charAt(size - i - 1) && index == -1) {
            if (str.charAt(i) == str.charAt(size - i - 2)) {
                index = size - i - 1;
            }
            if (str.charAt(i + 1) == str.charAt(size - i - 1)) {
                index = i;
            }
        }

        if (str.charAt(i) !== str.charAt(size - i - 1) && index !== -1) {
            index = -1;
            break;
        }
    }

    return index;
}

function main() {
    //let T = parseInt(readLine()), s;

    let T = 3, input = ['aaa', 'baa', 'aaab'], s, output = [];

    while (T--) {
        //s = readLine();

        s = input[T];

        output.push(palindrome(s));
    }

    console.log(output.join('\n'));

}

main();
