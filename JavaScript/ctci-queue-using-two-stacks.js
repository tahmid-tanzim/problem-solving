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
    //let q = parseInt(readLine());

    let q = 10; // delete

    let output = [], queue = [];
    while(q--) {
        let [type, val] = readLine().split(' ').map(Number);

        switch (type) {
            case 1:
                queue.push(val);
                break;
            case 2:
                queue.shift();
                break;
            case 3:
                output.push(queue[0]);
                break;
        }
    }
    console.log(output.join('\n'));
}

/////////////// ignore below this line ////////////////////

main();