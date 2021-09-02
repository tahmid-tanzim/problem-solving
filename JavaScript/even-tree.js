//process.stdin.resume();
//process.stdin.setEncoding('ascii');
//
//var input_stdin = "";
//var input_stdin_array = "";
//var input_currentline = 0;
//
//process.stdin.on('data', function (data) {
//    input_stdin += data;
//});
//
//process.stdin.on('end', function () {
//    input_stdin_array = input_stdin.split("\n");
//    main();
//});
//
//function readLine() {
//    return input_stdin_array[input_currentline++];
//}

/////////////// ignore above this line ////////////////////
function DFS(graph, v, bypass) {
    let stack = [], u, adjacent, visited_counter = 0, visited = [];
    stack.push(v);

    for (let i = 0; i < graph.length; i++) {
        visited[i] = false;
    }

    while(stack.length > 0) {
        u = stack.pop();
        if(!visited[u - 1]) {
            visited[u - 1] = true;
            //console.log('Visited: ', u);
            visited_counter++;
            adjacent = graph[u - 1];
            for(let i = 0; i < adjacent.length; i++) {
                if(!visited[adjacent[i] - 1] && adjacent[i] !== bypass) {
                    stack.push(adjacent[i]);
                }
            }
        }
    }

    return visited_counter;
}

function main() {
    //const [N, M] = readLine().split(' ').map(Number); // Uncomment

    const N = 10, M = 9, O = [[2, 1], [3, 1], [4, 3], [5, 2], [6, 1], [7, 2], [8, 6], [9, 8], [10, 8]]; // Delete Later

    let i, graph = [], visited = [], edges = [], remove_counter = 0, x_counter, y_counter;
    for (i = 0; i < N; i++) {
        graph[i] = [];
        visited[i] = false;
    }

    /* Build Graph & Edges from input */
    for (i = 0; i < M; i++) {
        //let [x, y] = readLine().split(' ').map(Number); // Uncomment

        let [x, y] = O[i];// Delete later

        edges.push([x, y]);
        graph[x - 1].push(y);
        graph[y - 1].push(x);

    }

    /* Process for remove MAX edges */
    for (i = 0; i < M; i++) {
        let [x, y] = edges[i];

        x_counter = DFS(graph, x, y);
        y_counter = DFS(graph, y, x);
        if(x_counter % 2 == 0 && y_counter % 2 == 0) {
            //console.log(x,y,x_counter,y_counter);
            remove_counter++;
        }
    }

    //x_counter = DFS(graph, 2, 1);
    //y_counter = DFS(graph, 1, 2);
    //console.log(x_counter,y_counter);
    //x_counter = DFS(graph, 3, 1);
    //y_counter = DFS(graph, 1, 3);
    //console.log(x_counter,y_counter);

    console.log(remove_counter);
}


main();
