const votes = [
    'angular',
    'ember',
    'angular',
    'react',
    'react',
    'react',
    'angular',
    'ember',
    'react',
    'vanilla'
];

const frequency = votes.reduce((obj, vote) => {
    obj[vote] = obj[vote] || 0;
    obj[vote]++;
    return obj;
}, {});

console.log(frequency);