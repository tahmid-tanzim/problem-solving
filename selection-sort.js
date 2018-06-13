function selection_sort(A) {
    let n = A.length, index_min, temp;

    for (let i = 0; i < n - 1; i++) {
        index_min = i;
        for (let j = i + 1; j < n; j++) {
            if(A[j] < A[index_min]){
                index_min = j;
            }
        }
        if(index_min !== i) {
            temp = A[i];
            A[i] = A[index_min];
            A[index_min] = temp;
        }
    }

    return A;
}

const arr = selection_sort([3, 44, 38, 5, 15, 26, 27, 2, 46, 4]);
console.log(arr);