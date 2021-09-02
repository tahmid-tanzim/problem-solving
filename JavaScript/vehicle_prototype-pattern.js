/* Prototype Pattern */
var vehiclePrototype = {
    set_num_of_wheels: function(wheels) {
        this.wheels = wheels;
        return this.wheels;
    },
    set_num_of_passengers: function(passengers) {
        this.passengers = passengers;
        this.passengers;
    },
    has_gas: function() {
        return this.hasGas;
    },
    print: function() {
        console.log("No of wheels: " + this.wheels);
        console.log("No of passengers: " + this.passengers);
        console.log("Gas: " + this.hasGas + "\n");
    }
};

function Vehicle(wheels, passengers, hasGas) {
    function init(wheels, passengers, hasGas) {
        this.wheels = wheels || 0;
        this.passengers = passengers || 0;
        this.hasGas = hasGas || false;
    }

    init.prototype = vehiclePrototype;

    return new init(wheels, passengers, hasGas);
}

var car = Vehicle(4, 5, false);
var plane = Vehicle(3, 100, true);

car.set_num_of_passengers(2);
plane.set_num_of_wheels(18);

car.print();
plane.print();