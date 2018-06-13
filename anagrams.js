function anagrams(a, b) {
    var ai = 0, bi = 0, common = 0;

    while (ai < a.length && bi < b.length) {
        if (a[ai] < b[bi]) {
            ai++;
        } else if (a[ai] > b[bi]) {
            bi++;
        } else {
            common++;
            ai++;
            bi++;
        }
    }

    return a.length + b.length - (common * 2);
}

function main() {
    var a = readLine().split('').sort(), b = readLine().split('').sort();
    console.log(anagrams(a, b));
}
