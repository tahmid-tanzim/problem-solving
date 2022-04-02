const express = require("express")
const os = require("os")
const cluster = require("cluster")

const PORT = process.env.PORT || 3001

const clusterWorkerSize = os.cpus().length

function fibonacci(num) {
    if(num < 2) {
        return num;
    }
    else {
        return fibonacci(num - 1) + fibonacci(num - 2);
    }
}

function randomIntFromInterval(min, max) { 
    return Math.floor(Math.random() * (max - min + 1) + min)
}

if (clusterWorkerSize > 1) {
    if (cluster.isMaster) {
      for (let i=0; i < clusterWorkerSize; i++) {
        cluster.fork()
      }

      cluster.on("exit", function(worker) {
        console.log("Worker", worker.id, " has exitted.")
      })
    } else {
        const app = express()

        app.get('/', (req, res) => {
            const start = Date.now();
            let i = 30
            let key = []
            let value = []
            while(i > 0) {
                const rInt = randomIntFromInterval(5, 45)
                key.push(rInt)
                value.push(fibonacci(rInt))
                console.log(`Processing ... ${process.pid} - ${rInt}`)
                i -= 1
            }
            console.log(`\nPROCESSING COMPLETE ${process.pid}\n`)
            res.json({
                elapsedTime: `${(Date.now() - start) / 1000}s`, 
                message: `Response from the multi worker ${process.pid}`, 
                key, 
                value
            })
        })

        app.listen(PORT, () => {
            console.log(`Express server listening on port ${PORT} and worker ${process.pid}`)
        })
    }
} else {
    const app = express()

    app.listen(PORT, () => {
        console.log(`Express server listening on port ${PORT} with the single worker ${process.pid}`)
    })
}