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
function getNthPrime(n) {
    find: for (var primes = [2], i = 3, root; primes.length < n; i += 2) {
        for (root = Math.sqrt(i), j = 0; primes[j] <= root; j++) {
            if (i % primes[j] === 0) continue find;
        }
        primes.push(i);
    }
    return primes[n - 1];
}

function main() {
    //let [N, Q] = readLine().split(' ').map(Number);
    //let A = readLine().split(' ').map(Number);

    let N = 5, Q = 2, A = [3, 4, 7, 6, 5]; // delete

    let i = 1, B = {}, temp, val;
    while(i <= Q) {
        temp = A;
        A = [];

        while(temp.length > 0) {
            val = temp.pop();
            if(val % getNthPrime(i) == 0) {
                (B[i] = B[i] || []).push(val);
            } else {
                A.push(val);
            }
        }

        i++;
    }

    B[i] = A;

    /* Output */
    for (let k in B) {
        if (B.hasOwnProperty(k)) {
            while(B[k].length > 0) {
                console.log(B[k].pop());
            }
        }
    }
}

/////////////// ignore below this line ////////////////////

main();