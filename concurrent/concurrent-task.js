let logUpdate = require('log-update');
let delay = seconds => new Promise((resolves) => {
    setTimeout(resolves, seconds * 1000);
});

let tasks = [
    delay(4),
    delay(6),
    delay(4),
    delay(3),
    delay(5),
    delay(7),
    delay(9),
    delay(10),
    delay(3),
    delay(5)
];

class PromiseQueue {
    constructor(promises = [], concurrentCount = 1) {
        this.concurrent = concurrentCount;
        this.total = promises.length;
        this.todoTask = promises;
        this.runningTask = [];
        this.completedTask = [];
    }

    get canRunAnother() {
        return (this.runningTask.length < this.concurrent && this.todoTask.length > 0);
    }

    graphTasks() {
        logUpdate(`
        todo: [${this.todoTask.map(() => 'x')}] (${this.todoTask.length})
        running: [${this.runningTask.map(() => 'x')}] (${this.runningTask.length})
        complete: [${this.completedTask.map(() => 'x')}] (${this.completedTask.length})
        `);
    }

    run() {
        while (this.canRunAnother) {
            let promise = this.todoTask.shift();
            promise.then(() => {
                this.completedTask.push(this.runningTask.shift());
                this.graphTasks();
                this.run();
            });
            this.runningTask.push(promise);
            this.graphTasks();
        }
    }
}

let delayQueue = new PromiseQueue(tasks, 3);
delayQueue.run();