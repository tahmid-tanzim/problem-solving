function reverse(str) {

    if(str.length == 0) return;
    else {
        console.log('Val: ', str[0]);
        return reverse(str.substr(-1));
    }

}

function main() {
    console.log(reverse('lupin'));
}

main();
