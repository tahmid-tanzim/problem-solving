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
    // let Size = parseInt(readLine());
    // let Arr = readLine().split(' ').map(Number);

    let Size = 5, Arr = [2, 4, 6, 8, 3];
    //let Size = 6, Arr = [23, 42, 4, 16, 8, 15];

    for(let i = 1, j, x; i < Size; i++) {
        x = Arr[i];
        j = i - 1;
        while(j >= 0 && Arr[j] > x) {
            Arr[j + 1] = Arr[j];
            j--;
            console.log(Arr.join(' '));
        }
        Arr[j + 1] = x;
    }
    console.log(Arr.join(' '));
}

/////////////// ignore below this line ////////////////////
main();
