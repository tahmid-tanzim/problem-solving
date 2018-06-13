var reverseWords = function(n) {
    n = n.split(" ");
    var result = "", len = 0, x;

    for(var i in n) {
        len = n[i].length;
        for(x = len - 1; x >=0 ; x--) {
           result += n[i][x];  
        }
        result += " ";
    }

    return result.trim();
};

console.log(reverseWords("Hello World Tanzim!")); // 3