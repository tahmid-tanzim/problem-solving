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
    //let n = parseInt(readLine()), p = parseInt(readLine());

   let n = 6, p = 2;
    //let n = 5, p = 4;
    let step = Math.floor(n/2) + 1;

    console.log(step);
    console.log(Math.ceil(n/p));
}

/////////////// ignore below this line ////////////////////

main();