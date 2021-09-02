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
    //let n = parseInt(readLine()), p, output = [], dollar;

    let n = 2, input= ['abab', 'abcd'], s, p, output = [], dollar;

    while(n--) {
        //s = readLine();

        s = input[n];

        p = "";
        dollar = 0;
        for(let i in s) {
            if(p.indexOf(s.charAt(i)) == -1) {
                dollar++;
            }
            p += s.charAt(i);
        }

        output.push(dollar);
    }

    console.log(output.join('\n'));
}

/////////////// ignore below this line ////////////////////

main();