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
    //var q = parseInt(readLine());
    //for(var a0 = 0; a0 < q; a0++){
    //    var s = readLine();
    //    // your code goes here
    //}

    let q = 2, s = ['hereiamstackerrank', 'hackerworld'];

    let mapper = 'hackerrank', pointer, output = [], i = 0, j;

    while(i < q) {
        pointer = 0;
        for(j = 0; j < s[i].length; j++) {
            if(mapper.charAt(pointer) == s[i].charAt(j)) {
                pointer++;
            }
        }
        output.push(pointer == mapper.length ? 'YES' : 'NO');
        i++;
    }

    console.log(output.join('\n'));
}

/////////////// ignore below this line ////////////////////

main();

