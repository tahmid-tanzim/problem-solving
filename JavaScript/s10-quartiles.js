function processData(input) {
    let [n, X] = input.split('\n');
    n = parseInt(n);
    X = X.split(' ').map(Number).sort((a, b) => a - b);
    let Q = [n / 4, n / 2, n * 3 / 4];

    Q.forEach((q, index) => {
        let i = Math.floor(q);
        if (q % 1 === 0 || (q % 1 === 0.25 && index === 0)) {
            console.log((X[i] + X[i - 1]) / 2);
        } else if(q % 1 === 0.75 && index === 2) {
            console.log((X[i] + X[i + 1]) / 2);
        } else {
            console.log(X[i]);
        }
    });
}

// process.stdin.resume();
// process.stdin.setEncoding("ascii");
// _input = "";
// process.stdin.on("data", function (input) {
//     _input += input;
// });
//
// process.stdin.on("end", function () {
//     processData(_input);
// });

const str = `9
3 7 8 5 12 14 21 13 18`;
processData(str);