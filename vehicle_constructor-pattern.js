/* Constructor Pattern */
function Vehicle(wheels, passengers, hasGas) {
    this.wheels = wheels || 0;
    this.passengers = passengers || 0;
    this.hasGas = hasGas || false;

    this.set_num_of_wheels = function(wheels) {
        this.wheels = wheels;
        return this.wheels;
    }

    this.set_num_of_passengers = function(passengers) {
        this.passengers = passengers;
        this.passengers;
    }

    this.has_gas = function() {
        return this.hasGas;
    }

    this.print = function() {
        console.log("No of wheels: " + this.wheels);
        console.log("No of passengers: " + this.passengers);
        console.log("Gas: " + this.hasGas + "\n");
    }
}

var car = new Vehicle(4, 5, false);
var plane = new Vehicle(3, 100, true);

car.set_num_of_passengers(2);
plane.set_num_of_wheels(18);

car.print();
plane.print();