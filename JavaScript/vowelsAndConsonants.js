/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    let output = s.split(''), consonants = [], c;

    for(let i = 0; i < output.length; i++) {
        c = output[i];
        if(vowels.indexOf(c) > -1) {
            console.log(c);
        } else {
            consonants.push(c);
        }
    }
    console.log(consonants.join('\n'));
}

vowelsAndConsonants('javascriptloops');