class Conductor {
    run(command) {
        console.log(`Executing command ${command.name} | ${command.time}`);
        command.execute();
    }
};

module.exports = new Conductor();