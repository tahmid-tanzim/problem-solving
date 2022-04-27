class Graph {
    constructor() {
        this.fx_rates = {};
        this.max_exchange_rate = -1.0;
    }

    add_edge(from_currency, to_currency, ex_rate) {
        if(!(from_currency in this.fx_rates)) {
            this.fx_rates[from_currency] = [];
        } 
        this.fx_rates[from_currency].push([to_currency, ex_rate]);
    }

    dfs(current_currency, target_currency, visited, path, amount) {
        visited[current_currency] = true;
        path.push(amount)
    
        if(current_currency === target_currency) {
            let current_amount = path.reduce((a, b) => a * b, 1);

            if(current_amount !== 1.0 && current_amount > this.max_exchange_rate) {
                this.max_exchange_rate = current_amount;
            }

            // console.log(path, current_amount);
        }
        else {
            for(const [currency, rate] of this.fx_rates[current_currency]) {
                if(!visited[currency]) {
                    this.dfs(currency, target_currency, visited, path, rate);
                }
            }
        }

        path.pop();
        visited[current_currency] = false;
    }

    traverse_path(original_currency, target_currency) {
        let visited = {}, path = [];

        for(const currency of Object.keys(this.fx_rates)) {
            visited[currency] = false;
        }

        this.dfs(original_currency, target_currency, visited, path, 1.0);

        // const m = Number((Math.abs(this.max_exchange_rate) * 100).toPrecision(15));
        // return Math.round(m) / 100 * Math.sign(this.max_exchange_rate);
        return this.max_exchange_rate.toFixed(2);
    }
}

const generate_graph = fx_rates => {
    let graph_obj = new Graph();
    hash_table = {};

    for(const [from_currency, to_currency, rate] of fx_rates) {
        graph_obj.add_edge(from_currency, to_currency, rate);
        hash_table[`${from_currency}-${to_currency}`] = rate;
    }
       
    for(const [from_currency, to_currency, rate] of fx_rates) {
        if(!(`${to_currency}-${from_currency}` in hash_table)) {
            graph_obj.add_edge(to_currency, from_currency, 1 / rate);
        }
    }
       
    return graph_obj;
};


(function () {
    const inputs = [
        {
            "fx_rates": [
                ['USD', 'JPY', 110],
                ['USD', 'AUD', 1.45],
                ['JPY', 'GBP', 0.0070]

            ],
            "original_currency": 'GBP',
            "target_currency": 'AUD',
            "expected": 1.88
        },
        {
            "fx_rates": [
                ['USD', 'JPY', 109],
                ['USD', 'GBP', 0.71],
                ['GBP', 'JPY', 155]
            ],
            "original_currency": 'USD',
            "target_currency": 'JPY',
            "expected": 110.05
        },
        {
            "fx_rates": [
                ['USD', 'GBP', 0.7],
                ['USD', 'JPY', 109],
                ['GBP', 'JPY', 155],
                ['CAD', 'CNY', 5.27],
                ['CAD', 'KRW', 921]

            ],
            "original_currency": 'USD',
            "target_currency": 'CNY',
            "expected": -1.0
        },
        {
            "fx_rates": [
                ['USD', 'CAD', 1.3],
                ['USD', 'GBP', 0.71],
                ['USD', 'JPY', 109],
                ['GBP', 'JPY', 155]

            ],
            "original_currency": 'USD',
            "target_currency": 'JPY',
            "expected": 110.05
        },
        {
            "fx_rates": [
                ['MVR', 'BDT', 5.17728],
                ['GYD', 'BDT', 0.39521],
                ['BDT', 'MVR', 0.17772],
                ['BDT', 'GYD', 2.43054]

            ],
            "original_currency": 'MVR',
            "target_currency": 'GYD',
            "expected": 12.58
        },
        {
            "fx_rates": [
                ['USD', 'EUR', 0.9],
                ['EUR', 'CAD', 1.46]

            ],
            "original_currency": 'CAD',
            "target_currency": 'USD',
            "expected": 0.76
        },
        {
            "fx_rates": [
                ['USD', 'CAD', 0.5],
                ['GBP', 'USD', 0.5],
                ['CAD', 'JPY', 1.75],
                ['JPY', 'GBP', 3],
                ['EUR', 'JPY', 1 / 5],
                ['BDT', 'JPY', 4],
                ['JPY', 'BDT', 0.3],
                ['GBP', 'EUR', 10],
                ['GBP', 'BDT', 3]
            ],
            "original_currency": 'USD',
            "target_currency": 'EUR',
            "expected": 120.0
        }
    ];

    let test_passed = 0, i = 0;
    for(const val of inputs) {
        const g = generate_graph(val["fx_rates"]);
        const output = g.traverse_path(val["original_currency"], val["target_currency"]);
        if(output == val['expected']) {
            console.log(`${i}. CORRECT Answer\nOutput:${output}\nExpected:${val['expected']}\n\n`);
            test_passed += 1;
        }
        else {
            console.log(`${i}. WRONG Answer\nOutput:${output}\nExpected:${val['expected']}\n\n`)
        }
        i += 1;
    }
       
    console.log(`Passed - ${test_passed}/${i}\n`);
})();