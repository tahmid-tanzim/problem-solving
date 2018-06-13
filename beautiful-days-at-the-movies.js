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
function reversed(n) {
    var post_one, pre_all = n, stack = [];

    do {
        post_one = pre_all % 10;
        pre_all = Math.floor(pre_all / 10);
        stack.push(post_one);

    } while (pre_all !== 0);

    return parseInt(stack.join(''));
}

function main() {
    //var c = readLine().split(' ');
    //c = c.map(Number);

    var c = [20, 23, 6];

    var count = 0, i = c[0], j = c[1], k = c[2];

    while(i <= j) {
        if(Math.abs(i - reversed(i)) % k == 0) {
            count++;
        }
        i++;
    }
    console.log(count);
}


main();
