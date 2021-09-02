/* Factory Pattern */
function Vehicle(wheels, passengers, hasGas) {
    var v = {};

    v.wheels = wheels || 0;
    v.passengers = passengers || 0;
    v.hasGas = hasGas || false;

    v.set_num_of_wheels = function(wheels) {
        v.wheels = wheels;
        return this.wheels;
    }

    v.set_num_of_passengers = function(passengers) {
        v.passengers = passengers;
        v.passengers;
    }

    v.has_gas = function() {
        return v.hasGas;
    }

    v.print = function() {
        console.log("No of wheels: " + v.wheels);
        console.log("No of passengers: " + v.passengers);
        console.log("Gas: " + v.hasGas + "\n");
    }

    return v;
}

var car = Vehicle(4, 5, false);
var plane = Vehicle(3, 100, true);

car.set_num_of_passengers(2);
plane.set_num_of_wheels(18);

car.print();
plane.print();