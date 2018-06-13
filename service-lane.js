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
    //let [N, T] = readLine().split(' ').map(Number),
    //width = readLine().split(' ').map(Number), i, j, min, output = [];

    let [N, T] = [8, 5], i, j, min,
        width = [2, 3, 1, 2, 3, 2, 3, 3],
        output = [],
        input = [[0, 7], [3, 5], [6, 7], [4, 6], [0, 3]];

   while(T--) {
       //[i, j] = readLine().split(' ').map(Number);
       [i, j] = input[T];
       min = 4;

       while(i <= j) {
           if(min > width[i]) {
               min = width[i];
           }
           i++;
       }

       output.push(min);

   }
    console.log(output.join('\n'));
}

/////////////// ignore above this line ////////////////////
main();
