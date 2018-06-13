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
    //let [n, k] = readLine().split(' ').map(Number), l, t, contest = {'0': [], '1': []};

    let n = 100, k = 28, l, t, contest = {'0': [], '1': []}, input = (`5725 1
 7712 1
 2083 1
 4085 1
 1479 1
 2860 1
 4605 1
 8254 1
 2317 1
 1539 1
 9359 1
 4967 1
 6945 1
 6542 1
 492 1
 2996 1
 1841 1
 154 1
 6963 1
 3903 1
 1324 1
 6869 1
 9630 1
 7530 1
 5548 1
 2392 1
 7645 1
 5437 1
 4772 1
 293 1
 5891 1
 42 1
 2649 1
 7674 1
 9913 1
 5448 1
 7377 1
 6309 1
 8146 1
 9265 1
 1843 1
 8724 1
 779 1
 9170 1
 8757 1
 9719 1
 5668 1
 1539 1
 2440 1
 8704 1
 3932 1
 9041 1
 4394 1
 9955 1
 1870 1
 8943 1
 4665 1
 1943 1
 6300 1
 2191 1
 7422 1
 38 1
 289 1
 5538 1
 5706 1
 1323 1
 5142 1
 3806 1
 3549 1
 107 1
 4371 1
 7036 1
 9742 1
 3036 1
 5007 1
 2663 1
 9962 1
 9895 1
 6335 1
 7447 1
 1727 1
 2624 1
 4465 1
 2930 1
 334 1
 8468 1
 9896 1
 5351 1
 6730 1
 8717 1
 4828 1
 1102 1
 3282 1
 6119 1
 2383 1
 3812 1
 2758 1
 6828 1
 6501 1
 4627 1`).split('\n');

    while(n--) {
        //[l, t] = readLine().split(' ').map(Number);

        [l, t] = input[n].trim().split(' ').map(Number);

        contest[t].push(l);
    }

    contest[1] = contest[1].sort((a, b) => a - b);

    let totalLuckBalance = contest[0].reduce((a, b) => a + b, 0);

    for(let i = contest[1].length - 1; i >= 0; i--) {
        if(k > 0) {
            totalLuckBalance += contest[1][i];
            k--;
        } else {
            totalLuckBalance -= contest[1][i];
        }
    }

    console.log(totalLuckBalance);
    //console.log(contest);


}

main();

// -13242
/*
 100 28
 5725 1
 7712 1
 2083 1
 4085 1
 1479 1
 2860 1
 4605 1
 8254 1
 2317 1
 1539 1
 9359 1
 4967 1
 6945 1
 6542 1
 492 1
 2996 1
 1841 1
 154 1
 6963 1
 3903 1
 1324 1
 6869 1
 9630 1
 7530 1
 5548 1
 2392 1
 7645 1
 5437 1
 4772 1
 293 1
 5891 1
 42 1
 2649 1
 7674 1
 9913 1
 5448 1
 7377 1
 6309 1
 8146 1
 9265 1
 1843 1
 8724 1
 779 1
 9170 1
 8757 1
 9719 1
 5668 1
 1539 1
 2440 1
 8704 1
 3932 1
 9041 1
 4394 1
 9955 1
 1870 1
 8943 1
 4665 1
 1943 1
 6300 1
 2191 1
 7422 1
 38 1
 289 1
 5538 1
 5706 1
 1323 1
 5142 1
 3806 1
 3549 1
 107 1
 4371 1
 7036 1
 9742 1
 3036 1
 5007 1
 2663 1
 9962 1
 9895 1
 6335 1
 7447 1
 1727 1
 2624 1
 4465 1
 2930 1
 334 1
 8468 1
 9896 1
 5351 1
 6730 1
 8717 1
 4828 1
 1102 1
 3282 1
 6119 1
 2383 1
 3812 1
 2758 1
 6828 1
 6501 1
 4627 1
* */
