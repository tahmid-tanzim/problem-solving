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
function decimal_binary(number) {
    let bit_str = '', bit, quotient;
    while (number > 0) {
        bit = number % 2;
        quotient = Math.floor(number / 2);
        bit_str = bit + bit_str;
        number = quotient;
    }
    return bit_str;
}

function binary_decimal(bit_str) {
    let i = bit_str.length, size = i, number = 0;
    while (i--) {
        if (parseInt(bit_str.charAt(i))) {
            number += Math.pow(2, size - i - 1);
        }
    }
    return number;
}

function XOR(x, y) {
    x = decimal_binary(x);
    y = decimal_binary(y);

    let bit_str = '', i, xi, yi, len_diff = x.length - y.length;

    /* Equalize two string */
    if (len_diff !== 0) {
        if (len_diff > 0) {
            while (y.length < x.length) {
                y = "0" + y;
            }
        } else {
            while (x.length < y.length) {
                x = "0" + x;
            }
        }
    }

    for (i = 0; i < x.length; i++) {
        xi = parseInt(x.charAt(i));
        yi = parseInt(y.charAt(i));
        bit_str += ((xi && !yi) || (!xi && yi)) ? '1' : '0';
    }

    return binary_decimal(bit_str);
}

function main() {
    // let L = parseInt(readLine());
    // let R = parseInt(readLine());

    let L = 1, R = 10; // delete
    let maximal = -1, i, temp;

    while(L <= R) {
        for(i = L; i <= R; i++) {
            temp = XOR(L, i);
            if(maximal < temp) {
                maximal = temp;
            }
        }
        L++;
    }

    console.log(maximal);
}

/////////////// ignore below this line ////////////////////

main();

/*
 10 '1010'
 11 '1011'
 12 '1100'
 13 '1101'
 14 '1110'
 15 '1111'
 */