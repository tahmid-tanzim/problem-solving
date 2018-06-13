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

function getMoneySpent(keyboards, drives, s) {
    let price, min = {price: null, diff: -1};
    for (let k = 0; k < keyboards.length; k++) {
        for (let d = 0; d < drives.length; d++) {
            price = keyboards[k] + drives[d];
            if (s - price > -1 && (min.diff == -1 || min.diff > s - price)) {
                min = {price, diff: s - price};
            }
        }
    }

    return min.price || -1;
}

function main() {
    //let temp = readLine().split(' ').map(Number),
    //    [s, n ,m] = temp,
    //    keyboards = readLine().split(' ').map(Number),
    //    drives = readLine().split(' ').map(Number);

    let s = 5, n = 1, m = 1, keyboards = [4], drives = [5];
    //let s = 10, n = 2, m = 3, keyboards = [3, 1], drives = [5, 2, 8];
    let moneySpent = getMoneySpent(keyboards, drives, s);

    console.log(moneySpent);
}

/////////////// ignore below this line ////////////////////
main();
