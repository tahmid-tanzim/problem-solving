function main() {
    var n = 5, k = 7, height = [2, 5, 4, 5, 2];

    var max = Math.max(...height);
    console.log(max > k ? max - k : 0);
}

main();
