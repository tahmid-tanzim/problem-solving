function isAnagram (s1, s2) {
    if (s1.length !== s2.length) {
        return false;
    }

    // Calculate frequency of letters in string 1
    var s1_frequency = {};
    for (var i = 0; i < s1.length; i++) {
      var char = s1[i];
      s1_frequency[char] = s1_frequency[char] ? 1 + s1_frequency[char] : 1;
    }

    // Check letters of string 2 exist in string 1
    for (var i = 0; i < s2.length; i++) {
        if(!s1_frequency[s2[i]]) {
            return false;
        } else {
            s1_frequency[s2[i]] -= 1;
        }
    }
    return true;
}

console.log(isAnagram('bleat','table')); // true
console.log(isAnagram('eat','tar')); // false
