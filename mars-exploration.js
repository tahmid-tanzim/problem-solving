function main() {
    var S = 'SOSSPSSQSSOR';
    var i = 0, j, temp = null, count = 0, map = ['S','O','S'];

    while(i < S.length ) {
        temp = S.substr(i, 3);
        if(temp !== 'SOS') {
            for(j = 0; j < 3; j++) {
                if(map[j] !== temp[j]) {
                    count++;
                }
            }
        }
        i += 3;
    }

    console.log(count);
}

main();
