// 'use strict';
//
// const fs = require('fs');
//
// process.stdin.resume();
// process.stdin.setEncoding('utf-8');
//
// let inputString = '';
// let currentLine = 0;
//
// process.stdin.on('data', inputStdin => {
//     inputString += inputStdin;
// });
//
// process.stdin.on('end', _ => {
//     inputString = inputString.replace(/\s*$/, '')
//         .split('\n')
//         .map(str => str.replace(/\s*$/, ''));
//
//     main();
// });
//
// function readLine() {
//     return inputString[currentLine++];
// }

// Complete the introTutorial function below.
function introTutorial(V, arr) {
    return arr.indexOf(V);
}

function main() {
    // const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    // const V = parseInt(readLine(), 10);
    const V = 4;

    // const n = parseInt(readLine(), 10);
    const n = 6;

    // const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    const arr = [1, 4, 5, 7, 9, 12];

    let result = introTutorial(V, arr);
    console.log(result);

    // ws.write(result + "\n");
    //
    // ws.end();
}

main();