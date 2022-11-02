"use strict";
/* Module 4: Develop typed functions using TypeScript
   Lab Start  */
let sortDescending = function (a, b) {
    if (a > b) {
        return -1;
    }
    else if (b > a) {
        return 1;
    }
    else {
        return 0;
    }
};
let sortAscending = (a, b) => {
    if (a > b) {
        return 1;
    }
    else if (b > a) {
        return -1;
    }
    else {
        return 0;
    }
};
/*  The buildArray function builds an array of unique random numbers containing the number
    of items based on the number passed to it. The sortOrder parameter determines
    whether to sort the array in ascending or descending order. */
/*  TODO: Update the BuildArray function. */
function buildArray(items, sortOrder) {
    let randomNumbers = [];
    let nextNumber;
    for (let counter = 0; counter < items; counter++) {
        nextNumber = Math.ceil(Math.random() * (100 - 1));
        if (randomNumbers.indexOf(nextNumber) === -1) {
            randomNumbers.push(nextNumber);
        }
        else {
            counter--;
        }
    }
    if (sortOrder === 'ascending') {
        return randomNumbers.sort(sortAscending);
    }
    else {
        return randomNumbers.sort(sortDescending);
    }
}
let myArray1 = buildArray(12, 'ascending');
let myArray2 = buildArray(8, 'descending');
console.log(myArray1);
console.log(myArray2);
function loanCalculator(loanCalculatorData) {
    let interest = loanCalculatorData.interestRate / 1200; // Calculates the monthly interest rate
    let payment;
    payment = loanCalculatorData.principle * interest / (1 - (Math.pow(1 / (1 + interest), loanCalculatorData.months)));
    return payment.toFixed(2);
}
let res = loanCalculator({
    principle: 5,
    interestRate: 100,
    months: 3
});
console.log('res: ', res);
