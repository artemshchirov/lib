"use strict";
/*  Module 7: Working with external libraries
    Lab Start */
exports.__esModule = true;
/*  TODO Add the import statement. */
var module07_loan_programs_1 = require("./module07_loan-programs");
/*  TODO Update the function calls. */
var interestOnlyPayment = (0, module07_loan_programs_1.calculateInterestOnlyLoanPayment)({ principle: 30000, interestRate: 5 });
var conventionalLoanPayment = (0, module07_loan_programs_1.calculateConventionalLoanPayment)({ principle: 30000, interestRate: 5, months: 180 });
console.log(interestOnlyPayment); //* Returns "The interest only loan payment is 125.00" 
console.log(conventionalLoanPayment); //* Returns "The conventional loan payment is 237.24"
