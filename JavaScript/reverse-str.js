var reverseStr = function(a, k) {
      a = a.split('');
      var temp, n = a.length;
        while( k > 0 ) {
            temp = a[0];
            for(var i = 1; i < n; i++) {
                a[i - 1] = a[i];
            }
            a[n - 1] = temp;
            
            k--;
        }
        return a.join('');
};

console.log(reverseStr("abcdefg", 2));