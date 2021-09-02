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
//    var n = parseInt(readLine());
//    var c = readLine().split(' ');
//    c = c.map(Number);

    var n = 5;
    var a = [3, 3, 2, 1, 3];

    var frequency = {}, i, sum = 0, max_val = 0;

    for(i = 0; i < a.length; i++) {
        if(frequency[a[i]]) {
            frequency[a[i]]++;
        } else {
            frequency[a[i]] = 1;
        }
    }

     for (i in frequency) {
        if (frequency.hasOwnProperty(i)) {
            sum += frequency[i];
            if(frequency[i] > max_val) {
                max_val = frequency[i];
            }
        }
     }

    console.log(sum - max_val);
}


main();
