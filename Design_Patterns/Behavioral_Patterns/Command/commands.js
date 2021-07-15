const { writeFile } = require('fs');
const path = require('path');

class ExitCommand {
    constructor() {
        this.time = Date.now();
    }

    get name() {
        return "Exit ...";
    }

    execute() {
        process.exit(0);
    }
}

class CreateCommand {
    constructor(fileName, text) {
        this.fileName = fileName;
        this.body = text;
        this.fullPath = path.join(__dirname, fileName);
        
    }

    get name() {
        return "Create ...";
    }

    get time() {
        return Date.now();
    }

    execute(){
        writeFile(this.fullPath, this.body, f => f);
    }
}

module.exports = {
    ExitCommand,
    CreateCommand
};