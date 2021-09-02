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
    //let T = parseInt(readLine()), S, R;

    let T = 2, S, s = ['acxz', 'bcxz'], R; //delete

    let size, flag, output = [];
    while(T--) {
        //S = readLine();

        S = s[T]; // delete

        size = S.length;
        flag = true;
        for(let i = 1; i < S.length; i++) {
            if(Math.abs(S[i].charCodeAt(0) - S[i - 1].charCodeAt(0)) !== Math.abs(S[size - i - 1].charCodeAt(0) - S[size - i].charCodeAt(0))) {
                flag = false;
                break;
            }
        }

        output.push(flag ? 'Funny' : 'Not Funny');
    }

    console.log(output.join('\n'));
}

/////////////// ignore below this line ////////////////////

main();