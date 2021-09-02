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
    //const
    //    [s, t] = readLine().split(' ').map(Number),
    //    [a, b] = readLine().split(' ').map(Number),
    //    [m, n] = readLine().split(' ').map(Number),
    //    apple_distance = readLine().split(' ').map(Number),
    //    orange_distance = readLine().split(' ').map(Number);

    const
        [s, t] = [7, 11],
        [a, b] = [5, 15],
        [m, n] = [3, 2],
        apple_distance = [-2, 2, 1],
        orange_distance = [5, -6];

    let apple_counter = 0, orange_counter = 0, i;
    for(i in apple_distance) {
        if(apple_distance[i] + a >= s && apple_distance[i] + a <= t) {
            apple_counter++;
        }
    }

    for(i in orange_distance) {
        if(orange_distance[i] + b >= s && orange_distance[i] + b <= t) {
            orange_counter++;
        }
    }

    console.log(apple_counter + "\n" + orange_counter);

}

/////////////// ignore below this line ////////////////////
main();
