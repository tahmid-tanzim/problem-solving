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
    //let N = parseInt(readLine());

    let N = 4, i = 0, read_line = ['aba', 'baba', 'aba','xzxb']; // delete

    let str = [], output = [];
    while(N--) {
        str.push(read_line[i]);
        i++;
    }

    //let Q = parseInt(readLine());

    let Q = 3, j = 0, read_line2 = ['aba', 'xzxb', 'ab']; // delete
    while(Q--) {
        output.push(str.filter(x => x == read_line2[j]).length);
        j++;
    }

    console.log(output.join('\n'));
}

/////////////// ignore below this line ////////////////////

main();