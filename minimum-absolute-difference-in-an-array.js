//process.stdin.resume();
//process.stdin.setEncoding('ascii');
//
//var input_stdin = "";
//var input_stdin_array = "";
//var input_currentline = 0;
//
//process.stdin.on('data', function (data) {
//    input_stdin += data;
//});
//
//process.stdin.on('end', function () {
//    input_stdin_array = input_stdin.split("\n");
//    main();
//});
//
//function readLine() {
//    return input_stdin_array[input_currentline++];
//}

/////////////// ignore above this line ////////////////////

function main() {
    //let n = parseInt(readLine()), a = readLine().split(' ').map(Number);

    let n = 3, a = [3, -7, 0];

    a.sort((a, b) => a - b);

    let i, min = a[1] - a[0];
    for (i = 0; i < n - 1; i++) {
        if (a[i + 1] - a[i] < min) {
            min = a[i + 1] - a[i];
        }
    }

    console.log(min);
}

/////////////// ignore below this line ////////////////////
main();