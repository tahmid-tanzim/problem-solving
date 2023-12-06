const getDateXDaysAgo = (numOfDaysAgo, endDate = new Date()) => {
    const startDate = new Date(endDate.getTime());
    startDate.setDate(endDate.getDate() - numOfDaysAgo + 1);
    startDate.setUTCHours(0, 0, 0, 0);
    endDate.setUTCHours(23, 59, 59, 999);
    return {fromDate: startDate, toDate: endDate};
};

const getDateRangeLabel = (fromDate, toDate, showSingleDate = false) => {
    const month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const endDateString = `${month[toDate.getMonth()]} ${toDate.getDate()}, ${toDate.getFullYear()}`;
    if (showSingleDate) {
        return endDateString;
    }
    fromDate.setUTCHours(23, 59, 59, 999);
    const startDateString = `${month[fromDate.getMonth()]} ${fromDate.getDate()}, ${fromDate.getFullYear()}`;
    return startDateString + ' - ' + endDateString;
};

const calculateChartsDateRanges = (comparison, currentDate, showSingleDate = false) => {
    const dateRanges = [];
    let startDate;
    let endDate = new Date(currentDate).toLocaleString('en-US', {timeZone: 'America/Los_Angeles' });
    endDate = new Date(endDate);
    endDate.setHours(endDate.getHours() - 6);
    for (let i = 0; i < comparison.xAxisTotalNumberOfDurations; i++) {
        startDate = new Date(endDate.getTime());
        startDate.setDate(endDate.getDate() - comparison.xAxisSingleDurationInDays + 1);
        startDate.setUTCHours(0, 0, 0, 0);
        endDate.setUTCHours(23, 59, 59, 999);
        const obj = {
            fromDate: new Date(startDate.getTime()),
            toDate: new Date(endDate.getTime())
        };
        obj.label = getDateRangeLabel(obj.fromDate, obj.toDate, showSingleDate);
        dateRanges.unshift({...obj});
        startDate.setTime(startDate.getTime() - 1);
        endDate = startDate;
    }
    return dateRanges;
};

/*
* xAxisSingleDurationInDays: '1 = daily', '7 = weekly', '30 = monthly', '90 = quarterly', '365 = yearly'
* xAxisTotalNumberOfDurations: No of x-axis points
* */

// const currentDate = new Date(2023, 0, 2, 12, 0, 0);
// console.log(calculateChartsDateRanges({
//     xAxisSingleDurationInDays: 7,
//     xAxisTotalNumberOfDurations: 3,
//
// }, currentDate, false));

// const testDate = new Date().toLocaleString('en-US', {timeZone: 'America/Los_Angeles' });
// console.log(typeof testDate, testDate);
// const testDate2 = new Date(testDate);
// console.log('Before: ', testDate2);
// testDate2.setHours(testDate2.getHours() - 6);
// console.log('After: ', testDate2);

const calculateRate = (type, total) => {
    let nominator = 0;
    let denominator = 0;
    const {approval, decline, failure, conflict} = total;
    switch (type) {
        case 'APPROVAL':
            nominator = approval;
            denominator = approval + decline;
            break;
        case 'CHECKOUT':
            nominator = approval;
            denominator = approval + decline + failure + conflict;
            break;
        case 'CONVERSION':
            nominator = approval + decline + conflict;
            denominator = approval + decline + failure + conflict;
            break;
        default:
            return 0;
    }
    return denominator ? nominator / denominator * 100 : 0;
};

const type = 'APPROVAL';
const total = {
    approval: 0,
    decline: 0,
    failure: 0,
    conflict: 0
};

console.log(calculateRate(type, total));
