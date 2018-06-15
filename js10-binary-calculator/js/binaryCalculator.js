/* https://www.hackerrank.com/challenges/js10-binary-calculator?hr_b=1 */

let res = "";
let operator = "";

/* Parameter 'e' is the click Event */
function action(e) {
    /* Older IE browsers have a srcElement property,
    but other browsers have a 'target' property;
    Set btn to whichever exists. */
    let btn = e.target || e.srcElement;

    /* Get the clicked element's innerHTML */
    if (btn.id === "btnEql") {
        const [operand1, operand2] = res.split(operator);
        const expression = parseInt(operand1, 2) + operator + parseInt(operand2, 2);
        res = (eval(expression) >>> 0).toString(2);
    } else if (btn.id === "btnClr") {
        res = "";
    } else if (['btnSum', 'btnSub', 'btnMul', 'btnDiv'].indexOf(btn.id) !== -1) {
        operator = document.getElementById(btn.id).innerHTML;
        res += operator;
    } else {
        res += document.getElementById(btn.id).innerHTML;
    }
    document.getElementById("res").innerHTML = res;
}

/* Add a click event listener that calls action(e) when clicked */
document.getElementById('btn0').addEventListener('click', action);
document.getElementById('btn1').addEventListener('click', action);
document.getElementById('btnSum').addEventListener('click', action);
document.getElementById('btnSub').addEventListener('click', action);
document.getElementById('btnMul').addEventListener('click', action);
document.getElementById('btnDiv').addEventListener('click', action);
document.getElementById('btnClr').addEventListener('click', action);
document.getElementById('btnEql').addEventListener('click', action);