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
    //let q = parseInt(readLine()), s;

    let s,
        q = 7,
        input = [
            '1',
            '13',
            '010203',
            '101103',
            '99100',
            '91011',
            '1234'
        ];

    while(q--) {
        s = readLine();
    }

    console.log(isTwoDistinctAlternatingCharacters(s));
}

main();
