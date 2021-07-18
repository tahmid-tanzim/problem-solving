const { readFileSync, writeFileSync } = require('fs');
const path = require('path');

const f = readFileSync(path.join(__dirname, 'data', 'first.txt'), 'utf8');
const s = readFileSync(path.join(__dirname, 'data', 'second.txt'), 'utf8');

writeFileSync(
    path.join(__dirname, 'data', 'result.txt'), 
    `\nResult - \n${f}\n${s}`,
    {flag: 'a'}
);