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
    //let n = parseInt(readLine()), c = readLine().split(' ').map(Number);

    //let n = 7, c = [0, 0, 1, 0, 0, 1, 0]; // 4
    let n = 6, c = [0, 0, 0, 1, 0, 0]; // 3

    let i = 0, jumps = 0;
    while (i < n - 1) {
        jumps++;
        if(c[i+1] === 0 && c[i+2] === 1) {
            i += 1;
        } else {
            i += 2;
        }

    }
    console.log(jumps);
}

/////////////// ignore below this line ////////////////////
main();
