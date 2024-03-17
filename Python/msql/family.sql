-- Create a new database
CREATE DATABASE IF NOT EXISTS family_loans;

-- Switch to the new database
USE family_loans;

-- Create a 'loans' table to track individual loans
CREATE TABLE IF NOT EXISTS loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    borrower_name VARCHAR(100) NOT NULL,
    loan_amount DECIMAL(10, 2) NOT NULL,
    interest_rate DECIMAL(4, 2) DEFAULT 0.00,
    start_date DATE NOT NULL,
    payoff_date DATE,
    status ENUM('active', 'paid_off') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create a 'transactions' table to track payments
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    loan_id INT,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- Insert a new loan
INSERT INTO loans (borrower_name, loan_amount, start_date) VALUES ('Blue', 900.00, '2022-11-14');

-- Insert a payment for a loan
INSERT INTO transactions (loan_id, payment_amount, payment_date) VALUES (1, 1000.00, '2024-03-01');

-- Retrieve loan information with payments
SELECT loans.*, transactions.*
FROM loans
LEFT JOIN transactions ON loans.loan_id = transactions.loan_id;
