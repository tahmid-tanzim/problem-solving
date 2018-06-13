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
    //let H = parseInt(readLine());
    //let M = parseInt(readLine());

    let H = 6;
    let M = parseInt('35');

    const mapper = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'];
    let output = "";

    if(M === 0) {
        output = `${mapper[H - 1]} o' clock`;
    } else if(M == 15) {
        output = `quarter past ${mapper[H - 1]}`;
    } else if(M >= 1 && M <= 20) {
        output = `${mapper[M - 1]} minute${M !== 1 ? 's' : ''} past ${mapper[H - 1]}`;
    } else if(M >= 21 && M <= 29) {
        output = `twenty ${mapper[(M % 10) - 1]} minutes past ${mapper[H - 1]}`;
    } else if(M == 30) {
        output = `half past ${mapper[H - 1]}`;
    } else if(M == 45) {
        output = `quarter to ${mapper[H]}`;
    } else if(M >= 31 && M <= 38){
        output = `twenty ${mapper[(59 - M) % 10]} minutes to ${mapper[H]}`;
    } else if(M >= 39 && M <= 59){
        output = `${mapper[59 - M]} minutes to ${mapper[H]}`;
    }

    console.log(output);
}

/////////////// ignore below this line ////////////////////
main();
