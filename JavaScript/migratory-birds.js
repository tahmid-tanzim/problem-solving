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
    //var n = parseInt(readLine());
    //var t = readLine().split(' ');
    //t = t.map(Number);

    var n = 6;
    var t = [1, 4, 5, 4, 3, 4];

    let freq = [0, 0, 0, 0, 0], i = 0, max = {key: 0, val: 0};
    while(i < n) {
        freq[t[i] - 1]++;
        i++;
    }

    max.val = freq[0];
    for(i = 1; i < freq.length; i++) {
        if(max.val < freq[i]) {
            max = {key: i, val: freq[i]};
        }
    }

    console.log(max.key + 1);
}


main();
