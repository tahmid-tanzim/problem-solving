/* Singleton Pattern */

var vehicle = (function() {
    var v;

    function init(wheels, passengers, hasGas) {
        var wheels = wheels || 0;
        var passengers = passengers || 0;
        var hasGas = hasGas || false;

        return {
            set_num_of_wheels: function(wheels) {
                wheels = wheels;
                return wheels;
            },
            set_num_of_passengers: function(passengers) {
                passengers = passengers;
                passengers;
            },
            has_gas: function() {
                return hasGas;
            },
            print: function() {
                console.log("No of wheels: " + wheels);
                console.log("No of passengers: " + passengers);
                console.log("Gas: " + hasGas + "\n");
            }
        };
    }

    return {
        create: function(wheels, passengers, hasGas) {
            if(typeof obj === 'undefined') {
                v = init(wheels, passengers, hasGas);
            }

            return v;
        }
    };
})();

var car = vehicle.create(4, 5, false);
var plane = vehicle.create(3, 100, true);

car.set_num_of_passengers(2);
plane.set_num_of_wheels(18);

car.print();
plane.print();