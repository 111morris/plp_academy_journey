-- we retrieve checkNumber, paymentDate, and amount from the payments table
SELECT checkNumber, paymentDate, amount
FROM payments;

-- we etrieve orderDate, requiredDate, and status from orders table
-- that is only where status is 'In Process', sorted by orderDate in descending order
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

-- we display firstName, lastName, and email of employees
-- that is only those with jobTitle 'Sales Rep', ordered by employeeNumber descending
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- we retrieve all columns and records from the offices table
SELECT *
FROM offices;

-- we fetch productName and quantityInStock from products table
-- and sort by buyPrice ascending and limit the output to 5 records
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
