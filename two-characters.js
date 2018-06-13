//process.stdin.resume();
//process.stdin.setEncoding('ascii');
//
//var input_stdin = "";
//var input_stdin_array = "";
//var input_currentline = 0;
//
//process.stdin.on('data', function (data) {
//    input_stdin += data;
//});
//
//process.stdin.on('end', function () {
//    input_stdin_array = input_stdin.split("\n");
//    main();
//});
//
//function readLine() {
//    return input_stdin_array[input_currentline++];
//}

/////////////// ignore above this line ////////////////////
function getFrequency(string) {
    let freq = {}, character;
    for (let i = 0; i < string.length; i++) {
        character = string.charAt(i);
        if (freq[character]) {
            freq[character]++;
        } else {
            freq[character] = 1;
        }
    }
    return freq;
}

function isTwoDistinctAlternatingCharacters(s) {
    let temp = getFrequency(s);

    return temp;
}

function main() {
    //let n = parseInt(readLine()), s = readLine();

    let n = 10,
        s = 'beabeefeab';

    console.log(isTwoDistinctAlternatingCharacters(s));
}

main();
