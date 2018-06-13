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
function arrayLeftRotation(a, k) {
    let temp, n = a.length;
    while(k--) {
        temp = a[n - 1];
        for(let i = n - 2; i >= 0; i--) {
            a[i+1] = a[i];
        }
        a[0] = temp;
    }
    return a;
}

function main() {
//    const [n, k, q] = readLine().split(' ').map(Number);
//    let a = readLine().split(' ').map(Number); // a.length == n

    const [n, k, q] = [3, 2, 3];
    let a = [1, 2, 3], input = [0, 1, 2]; // a.length == n delete

    /* Rotation */
    a = arrayLeftRotation(a, k);

    let i, m, output = [];
    for (i = 0; i < q; i++) {
        //m = parseInt(readLine());
        m = input[i];
        output.push(a[m]);
    }

    console.log(output.join('\n'));
}

/////////////// ignore below this line ////////////////////

main();