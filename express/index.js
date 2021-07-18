const express = require('express');
const app = express();
const port = 3000;

function who(a) {
    return new Promise((resolve, reject) => {
        const val = Math.round(Math.random() * 1); // 0 or 1, at random
        setTimeout(() => {
            val ? resolve('🤡' + a) : reject('Nope 😠');
        }, 2000);
    });
}

function what(b) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('lurks' + b);
        }, 3000);
    });
}

function where(c) {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('in the shadows' + c);
        }, 5000);
    });
}


app.get('/', async (req, res) => {
    const b = await what(200);
    const c = await where(300);
    try {
        const a = await who(100);
        return res.send('Good Morning ...' + `${a} ${b} ${c}`);
    } catch(err) {
        return res.send('Bad Morning ...' + `${err} ${b} ${c}`);
    }

});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});


const events = require('events');
const myEmitter = new events.EventEmitter();
// const EventEmitter = require('events');
// class MyEmitter extends EventEmitter {}
// const myEmitter = new MyEmitter();
myEmitter.on('fire', (callback) => {
    callback();
 console.log('an event occurred!');
});
setTimeout(() => {
    myEmitter.emit('fire', () => {
        console.log('Bye');
    });
}, 1000);