process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////
function main() {
    //let T = parseInt(readLine()), N, K, a, output = [], i;

    let T = 2, N, K, a, i, output = [], count, input = {
        "0": [[4, 2], [0, -1, 2, 1]],
        "1": [[4, 3], [-1, -3, 4, 2]]
    };

    while (T--) {
        //[N, K] = readLine().split(' ').map(Number);
        //a = readLine().split(' ').map(Number);

        [N, K] = input[T][0];
        a = input[T][1];
        count = 0;

        for(i = 0; i < a.length; i++) {
            if(a[i] <= 0) {
                count++;
            }
        }

        output.push(count < K ? "YES" : "NO" );

    }

    console.log(output.join('\n'));

}

/////////////// ignore below this line ////////////////////
main();
