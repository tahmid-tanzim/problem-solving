function main() {
    var n = 9;
    var c = [10, 20, 20, 10, 10, 30, 50, 10, 20];

    var frequency = {}, i, count = 0;

    for(i = 0; i < c.length; i++) {
        if(frequency[c[i]]) {
            frequency[c[i]]++;
        } else {
            frequency[c[i]] = 1;
        }
    }

     for (var k in frequency) {
        if (frequency.hasOwnProperty(k)) {
            count += Math.floor(frequency[k]/2);
        }
     }

     console.log(count);
}

main();