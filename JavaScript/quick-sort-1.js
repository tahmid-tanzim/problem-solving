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
    // let Size = parseInt(readLine());
    // let Arr = readLine().split(' ').map(Number);

    //let Size = 5, Arr = [4, 5, 3, 7, 2];
    //let Size = 6, Arr = [23, 42, 4, 16, 8, 15];
    let Size = 7, Arr = [5, 8, 1, 3, 7, 9, 2];


    let pivote = Arr[0], left = [], right = [];
    for(let i = 1; i < Size; i++) {
        if(Arr[i] >= pivote) {
            right.push(Arr[i]);
        } else {
            left.push(Arr[i]);
        }
    }
    console.log(left.join(' ') + " " + pivote + " " + right.join(' '));
}

/////////////// ignore below this line ////////////////////
main();
