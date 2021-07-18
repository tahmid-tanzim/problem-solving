/*
TODO - Async Await
*/
const { readFile, writeFile } = require('fs');
const path = require('path');

readFile(path.join(__dirname, 'data', 'first.txt'), 'utf8', (err, first_result) => {
 if(err) {
     console.error(err);
 }
 const f = first_result;

 readFile(path.join(__dirname, 'data', 'second.txt'), 'utf8', (err, second_result) => {
    if(err) {
        console.error(err);
    }
    const s = second_result;

    writeFile(
        path.join(__dirname, 'data', 'result-async.txt'),
        `\nResult - \n${f}\n${s}`,
        {flag: 'a'},
        (err, result) => {
            if(err) {
                console.error(err);
            }
            console.log('Task Completed', result);
        }
    );

   });

});
