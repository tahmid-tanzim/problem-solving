function main() {
    //var s = readLine();
    //var n = parseInt(readLine());

    var s = 'aba';
    var n = 10;

    var s_len = s.length, count = 0, a_frequency = (s.match(new RegExp("a", "g")) || []).length;
    if (a_frequency) {
        count = Math.floor(n / s_len) * a_frequency + (s.substr(0, n % s_len).match(new RegExp("a", "g")) || []).length;
    }
    console.log(count);
}

main();
