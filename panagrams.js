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
    //let s = readLine().toLowerCase();

    //let s = 'We promptly judged antique ivory buckles for the next prize'.toLowerCase();
    let s = 'We promptly judged antique ivory buckles for the prize'.toLowerCase();

    let mapper = 'qwertyuiopasdfghjklzxcvbnm', flag = true;
    for(let i = 0; i < mapper.length; i++) {
        if(s.indexOf(mapper.charAt(i)) == -1) {
            flag = false;
            break;
        }
    }

    console.log(flag ? 'pangram' : 'not pangram');
}

/////////////// ignore below this line ////////////////////

main();