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
    //let h = readLine().split(' ').map(Number);
    //let s = readLine();

    let h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], s = 'abc';

    let max_height = h[s.charAt(0).charCodeAt(0) - 97], i, height;
    for(i = 1; i < s.length; i++) {
        height = h[s.charAt(i).charCodeAt(0) - 97];
        if(max_height < height) {
            max_height = height;
        }
    }

    console.log(max_height * s.length);
}

/////////////// ignore below this line ////////////////////
main();
