function insertion_sort(x, f, n) {
    for(let i = 1, j, key; i < n; i++) {
        key = [x[i], f[i]];
        j = i - 1;

        while (j >= 0 && x[j] > key[0]) {
            x[j+1] = x[j];
            f[j+1] = f[j];
            j--;
        }
        x[j + 1] = key[0];
        f[j + 1] = key[1];
    }
    return [x, f];
}

function processData(input) {
    let Q = [], S = [], [n, X, F] = input.split('\n');
    n = parseInt(n);
    X = X.split(' ').map(Number);
    F = F.split(' ').map(Number);
    [X, F] = insertion_sort(X, F, n);

    for(let i = 0, count; i < n; i++) {
        count = F[i];
        while(count--) {
            S.push(X[i]);
        }
    }

    const {length: len} = S;
    [len / 4, len / 2, len * 3 / 4].forEach((v, index) => {
        let i = Math.floor(v);
        if (v % 1 === 0 || (v % 1 === 0.25 && index === 0)) {
           Q[index] = (S[i] + S[i - 1]) / 2;
        } else if(v % 1 === 0.75 && index === 2) {
            Q[index] = (S[i] + S[i + 1]) / 2;
        } else {
            Q[index] = S[i];
        }
    });

    console.log((Q[2] - Q[0]).toFixed(1));
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

const str = `6
6 12 8 10 20 16
5 4 3 2 1 5`;
processData(str);