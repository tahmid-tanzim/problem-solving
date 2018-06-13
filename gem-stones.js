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
    //let N = parseInt(readLine()), s, mapper = {}, i, count = 0, x = 0;

    let N = parseInt('3'), input = ['eeabg', 'baccd', 'abcdde'], s, mapper = {}, i, count = 0, x = 0;

    while (x < N) {
        //s = readLine().split('');
        s = input[x].split('').filter((value, index, self) => self.indexOf(value) === index);

        for(i in s) {
            if(mapper[s[i]]) {
                mapper[s[i]]++;
                if(mapper[s[i]] == N) {
                    count++;
                }
            } else {
                mapper[s[i]] = 1;
            }
        }

        x++;
    }

    console.log(count);

}

/////////////// ignore above this line ////////////////////
main();
