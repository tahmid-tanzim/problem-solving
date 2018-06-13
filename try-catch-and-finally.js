/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try {
        console.log(s.split('').reverse().join(''));
    }
    catch(err) {
        console.log(err.message);
    }
    finally {
        console.log(s);
    }
}

reverseString(Number(1234));