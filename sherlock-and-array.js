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

function sum_elements(a) {
    return a.length ? a.reduce((a, b) => a + b, 0) : 0;
}

function main() {
    let T = parseInt(readLine()), n, A, i, flag, output = [], left, right;

    //let T = 10, input = [
    //    {n: '1', A: '1'}, // YES
    //    {n: '3', A: '6 23 6'}, // YES
    //    {n: '1', A: '20000'}, // YES
    //    {n: '1', A: '234'}, // YES
    //    {n: '3', A: '1 5 1'}, // YES
    //    {n: '3', A: '1 4 1'}, // YES
    //    {n: '2', A: '1 2'}, // NO
    //    {n: '1', A: '3'}, // YES
    //    {n: '1', A: '2'}, // YES
    //    {n: '1', A: '1'} // YES
    //], n, A, i, flag, output = [], left, right;

    while (T--) {
        n = parseInt(readLine());
        A = readLine().split(' ').map(Number);

        //n = parseInt(input[T].n);
        //A = input[T].A.split(' ').map(Number);

        left = 0;
        right = sum_elements(A.slice(1, n));

        if(left == right) {
            output.push('YES');
        } else {
            flag = 'NO';
            for (i = 1; i < n; i++) {
                left += A[i-1];
                right -= A[i];

                if (left == right) {
                    flag = 'YES';
                    break;
                }
            }
            output.push(flag);
        }
    }

    console.log(output.join('\n'));

}

main();

/** Input

 10
 1
 1
 1
 2
 1
 3
 2
 1 2
 3
 1 4 1
 3
 1 5 1
 1
 234
 1
 20000
 3
 6 23 6
 1
 1

 * */

/** Output

 YES
 YES
 YES
 NO
 YES
 YES
 YES
 YES
 YES
 YES

 * */
