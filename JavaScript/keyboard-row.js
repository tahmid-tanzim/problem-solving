/**
 * @param {string[]} words
 * @return {string[]}
 */

var getKeyboardRow = function(char) {
    var keybord = [
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm'
    ], row = '';

    for(var r in keybord) {
        if(keybord[r].indexOf(char) > -1) {
            row = keybord[r];
            break;
        }
    }
    return row;
};

var findWords = function(words) {
    var output = [];
    for(var i in words) {
        var flag = true, keyboard_row = getKeyboardRow(words[i].charAt(0).toLowerCase());
        for(var j = 1; j < words[i].length; j++) {
            var char = words[i].charAt(j).toLowerCase();
            if(keyboard_row.indexOf(char) === -1) {
                flag = false;
                break;
            }
        }

        if(flag) {
            output.push(words[i]);
        }
    }
    return output
};

console.log(findWords(["Aasdfghjkl","Qwertyuiop","zZxcvbnm"]));

/**
 * Output: ["Aasdfghjkl","Qwertyuiop"]
 * Expected: ["Aasdfghjkl","Qwertyuiop","zZxcvbnm"]
 * */