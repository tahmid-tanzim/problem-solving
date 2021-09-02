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


function main() {
    //let N = parseInt(readLine()),
    //    S = readLine(),
    //    K = parseInt(readLine()) % 26, i, ascii, output = '';

    let N = 11, S = 'middle-Outz', K = 2, i, ascii, output = '';

    for(i = 0; i < N; i++) {
        ascii = S.charAt(i).charCodeAt(0);
        if(ascii >= 65 && ascii <= 90) {
            ascii += K;
            while(ascii > 90) {
                ascii = 64 + ascii - 90;
            }
            output += String.fromCharCode(ascii);
        } else if(ascii >= 97 && ascii <= 122) {
            ascii += K;
            while(ascii > 122) {
                ascii = 96 + ascii - 122;
            }
            output += String.fromCharCode(ascii);
        } else {
            output += S.charAt(i);
        }
    }

    console.log(output);

}

/////////////// ignore below this line ////////////////////
main();
