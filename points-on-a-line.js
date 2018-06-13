// 'use strict';
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

function main() {
    // const n = parseInt(readLine(), 10);
    const n = 5, V = ['0 1', '0 2', '1 3', '0 4', '0 5'];
    let sum = [0, 0], flag = 'YES';

    for (let nItr = 0; nItr < n; nItr++) {
        // const xy = readLine().split(' ');
        const xy = V[nItr].split(' ');

        const x = parseInt(xy[0], 10);

        const y = parseInt(xy[1], 10);

        sum[0] += x;
        sum[1] += y;
        if(!((sum[0]/(nItr + 1)) === x || (sum[1]/(nItr + 1)) === y)) {
            flag = 'NO';
            break;
        }
    }


    console.log(flag);
}

main();
