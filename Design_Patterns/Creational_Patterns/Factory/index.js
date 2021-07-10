const userfactory = require('./userFactory');

const alex = userfactory('shopper', 'Alex Banks', 100);
const eve = userfactory('employee', 'Eve Porcello', 100, 'This and That');

eve.payDay(75);

console.log( alex.toString() )
console.log( eve.toString() )
