// process.stdin.resume();
// process.stdin.setEncoding('ascii');
//
// var input_stdin = "";
// var input_stdin_array = "";
// var input_currentline = 0;
//
// process.stdin.on('data', function (data) {
//     input_stdin += data;
// });
//
// process.stdin.on('end', function () {
//     input_stdin_array = input_stdin.split("\n");
//     main();
// });
//
// function readLine() {
//     return input_stdin_array[input_currentline++];
// }

/////////////// ignore above this line ////////////////////

function main() {
    // const
    // n = parseInt(readLine()),
    // n_array = readLine().split(' ').map(Number),
    // m = parseInt(readLine()),
    // m_array = readLine().split(' ').map(Number);

    const
        n = 11,
        n_array = [209, 203, 205, 204, 206, 207, 208, 204, 205, 203, 206],
        m = 13,
        m_array = [206, 207, 205, 203, 204, 205, 208, 203, 206, 204, 205, 206, 204];

    n_array.sort((a, b) => a - b);
    m_array.sort((a, b) => a - b);

    /* This are the pointers to traverse n_array & m_array */
    let ni = 0, mi = 0, missing = [];

    while(ni < n_array.length && mi < m_array.length) {
        if(n_array[ni] === m_array[mi]) {
            ni++;
            mi++;
        } else if(n_array[ni] > m_array[mi]) {
            missing.push(m_array[mi]);
            mi++;
        } else if(n_array[ni] < m_array[mi]) {
            missing.push(n_array[ni]);
            ni++;
        }
    }

    if(ni < n_array.length) {
        missing.push(n_array[ni]);
        ni++;
    }

    if(mi < m_array.length) {
        missing.push(m_array[mi]);
        mi++;
    }

    missing.sort((a, b) => a - b);
    console.log(missing.join(' '));
}

/////////////// ignore below this line ////////////////////
main();
// Output: 204 205 206 209

// 7251 7259 7276 7279 7292 7293