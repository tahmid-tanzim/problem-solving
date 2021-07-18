const { readFile, writeFile } = require('fs');
const path = require('path');

const readFilePromise = (file_name) => {
    return new Promise((resolve, reject) => {
        readFile(path.join(__dirname, 'data', file_name), 'utf8', (err, result) => {
            if (err) {
                reject(err);
            }
            resolve(result);
        });
    });
};

const writeFilePromise = (file_name, content) => {
    return new Promise((resolve, reject) => {
        writeFile(
            path.join(__dirname, 'data', file_name),
            content,
            { flag: 'a' },
            (err, result) => {
                if (err) {
                    reject(err);
                }
                resolve(result);
            }
        );
    });
};

(async (params) => {
    try {
        const first = await readFilePromise(params[0] + '.txt');
        const second = await readFilePromise(params[1] + '.txt');
        const final = await writeFilePromise('result-async-await.txt', `\nResult - \n${first}\n${second}`);
        
        console.log(first + "|" + second +"|"+final);
    } catch (error) {
        console.error(error);
    }
})(['first', 'second']);
