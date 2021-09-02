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

    //let Size = 5, Arr = [2, 4, 6, 8, 3];
    //let Size = 6, Arr = [23, 42, 4, 16, 8, 15];
    //let Size = 6, Arr = [1, 4, 3, 5, 6, 2];
    let Size = 5, Arr = [2, 1, 3, 1, 2];

    let count = 0, temp;
    for(let i = 1, j; i < Size; i++) {
        j = i;
        while(j > 0 && Arr[j - 1] > Arr[j]) {
            temp = Arr[j];
            Arr[j] = Arr[j - 1];
            Arr[j - 1] = temp;
            count++;
            j--;
        }
    }
    console.log(count);
}

/////////////// ignore below this line ////////////////////
main();
