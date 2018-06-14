let buttons = {
    id: ["btn1", "btn2", "btn3", "btn6", "btn9", "btn8", "btn7", "btn4"],
    label: [1, 2, 3, 6, 9, 8, 7, 4]
};
document.getElementById("btn5").onclick = function() {
    let last = buttons.label[7], i = 7;
    while (i >= 0) {
        buttons.label[i+1] = buttons.label[i];
        i--;
    }
    buttons.label[i+1] = last;
    buttons.label.splice(8, 1);
    buttons.id.forEach((id, index) => {
        document.getElementById(id).innerHTML = buttons.label[index];
    });
};