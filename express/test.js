const process_element = (arr) => {
    return new Promise((resolve, reject) => {
        let o = [];
        let timer = {};
        for (let i = 0; i < arr.length; i++) {
            let str = arr[i];
            if (typeof str !== 'string') {
                for (let t in timer) {
                    clearTimeout(timer[t]);
                }
               
                reject(`String required - ${str}`);
                break
            }

            timer[i] = setTimeout(() => {
                let r = str.split("").reverse().join("");
                o.push(r);
                console.log(r);
                if (o.length == arr.length) {
                    resolve(o);
                }
            }, 500);
        };
    });
};

(async () => {
    try {
        const reverse = await process_element(["Docker", "Python", "Tahmid", "Tanzim", "Java", 5])
        console.log(reverse)
    } catch (err) {
        console.error(err)
    }
})()



/*
 Create a event handler.
 where processes can register themselves for a type of event
 a process can then trigger the event and
 the event handler can then notify
 the listeners that event occurred with the event
  */

//  const events = require('events');
//  const emitter = new events.EventEmitter();
//  const eventType = {
//      reverse: "reverseString",
//      palindrome: "isPalindrome"
//  };

//   emitter.on(eventType["reverse"], (data) => {
//      console.log('\nBefore Reverse: ' + data);
//      console.log('After Reverse: ' + data.split('').reverse().join(''));
//   });

//   emitter.on(eventType["palindrome"], (data) => {
//      const len = data.length;
//      let isPalindromeFlag = true
//      for (let i = 0; i < len / 2; i++) {
//          if (data[i] !== data[len - 1 - i]) {
//              isPalindromeFlag = false;
//              break;
//          }
//      }

//      if(isPalindromeFlag) {
//          console.log(data + ' - is a palindrome\n');
//      } else {
//          console.log(data + ' - is NOT a palindrome\n');
//      }
//   });


//  let arr = ["Python", "TypeScript", "Java", "madam"];
//  for(let i = 0; i < arr.length; i++) {
//      let str = arr[i];
//      emitter.emit(eventType["reverse"], str);
//      emitter.emit(eventType["palindrome"], str);
//  }

//  console.time("loop");
//  for (var i = 0; i < 1000000; i += 1){
//      // Do nothing
//  }
//  console.timeEnd("loop");