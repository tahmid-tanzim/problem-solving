const Shopper = require('./Shopper');
const Employee = require('./Employee');

const userFactory = (type, name, money=0, employer='') => {
    switch(type) {
        case "shopper":
            return new Shopper(name, money);
        case "employee":
            return new Employee(name, money, employer);
        default:
            return null;
    }
};

module.exports = userFactory;