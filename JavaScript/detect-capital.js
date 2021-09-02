// https://leetcode.com/problems/detect-capital/description/
/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    var code = word.charAt(0).charCodeAt(0);
    var isCapital = code >= 65 && code <= 90;

    for(var i = 1; word.length; i++) {
        code = word.charAt(i).charCodeAt(0);
        if(isCapital && ) {

        }

    }
};

console.log(detectCapitalUse('USA'));

/**
 * if 1st Letter Capital
 *  then rest all letter should be either small or capital
 *
 * if 1st Letter Small
 *  then rest must be small
 * */