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
    // let n = parseInt(readLine());
    // let a = readLine().split(' ').map(Number);

    let n = 1, a = [1]; // delete
    //let n = 3, a = [1, 1, 2]; // delete
    //let n = 5, a = [0, 0, 1, 2, 1]; // delete

    a.sort(function(a, b) { return a - b; });
    let output, i;
    for(i = 0; i < n; i += 2) {
        if(a[i] !== a[i+1]) {
            output = a[i];
            break;
        }
    }
    console.log(output);
}

/////////////// ignore below this line ////////////////////

main();
