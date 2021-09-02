function binary_search(A, x) {
    let left = 0, right = A.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if(A[mid] === x) {
            return mid;
        }
        if(A[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

const index = binary_search([1, 4, 6, 7, 10, 19, 22, 23, 30, 35, 39, 46, 49, 50, 52, 55, 61, 67, 70, 71], 35);
console.log(index);