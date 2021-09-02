function search(arr, val, index = 0) {
    if(arr.length == index) return -1;
    else if(arr[index] == val) return index;
    else return search(arr, val, ++index);
}

function main() {
    console.log(search([1, 2, 3, 4, 5, 6], 2));
}

main();
