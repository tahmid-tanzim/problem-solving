const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    return res.send('Good Morning ...');
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
