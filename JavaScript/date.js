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

// const {fromDate, toDate} = getDateXDaysAgo(7);
// console.log(fromDate, toDate);
// const l = getDateRangeLabel(fromDate, toDate);
// console.log(l)

const calculateChartsDateRanges = (comparison, showSingleDate = false) => {
    const dateRanges = [];
    let endDate = new Date();
    for (let i = 0; i < comparison.xAxisTotalNumberOfDurations; i++) {
        let startDate = new Date(endDate.getTime());
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

//
console.log(calculateChartsDateRanges({
    xAxisSingleDurationInDays: 1,
    xAxisTotalNumberOfDurations: 7,

}, true));

console.log(new Date());
