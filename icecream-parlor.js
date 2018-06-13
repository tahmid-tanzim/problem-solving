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
    //let t = parseInt(readLine()), m ,n, c, i,j, output = [];

    let t = 2, m, n, c, output = [], i,j, input = {
        '0': [4, 4, [2,2,4,3]],
        '1': [4, 5, [1, 4, 5, 3, 2]]
    };

    while (t--) {
        //m = parseInt(readLine());
        //n = parseInt(readLine());
        //c = readLine().split(' ').map(Number);

        m = input[t][0];
        n = input[t][1];
        c = input[t][2];

        for(i = 0; i < c.length; i++) {
            if(m > c[i]) {
                j = c.indexOf(m - c[i]);
                if(j > -1 && i !== j) {
                    output.push(i > j ? `${j + 1} ${i + 1}` : `${i + 1} ${j + 1}`);
                    break;
                }
            }
        }
    }

    console.log(output.join('\n'));

}

/////////////// ignore below this line ////////////////////
main();
