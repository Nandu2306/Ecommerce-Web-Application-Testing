CREATE DATABASE ecommerce_qa;
USE ecommerce_qa;


CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_status VARCHAR(30)
);


INSERT INTO products VALUES
(1, 'Laptop', 50000, 10),
(2, 'Mouse', 500, 25),
(3, 'Keyboard', 1200, 15),
(4, 'Monitor', 10000, 8);

INSERT INTO customers VALUES
(101, 'Anu', 'anu@example.com'),
(102, 'Ravi', 'ravi@example.com'),
(103, 'Priya', 'priya@example.com');

INSERT INTO orders VALUES
(1001, 101, 1, 1, 'Completed'),
(1002, 102, 2, 2, 'Pending'),
(1003, 103, 3, 1, 'Completed'),
(1004, 101, 4, 1, 'Cancelled');

SELECT * FROM products;

SELECT product_name, price
FROM products
WHERE price > 1000;

SELECT *
FROM products
WHERE stock < 10;

SELECT product_name, price
FROM products
ORDER BY price ASC;

SELECT COUNT(*) AS total_products
FROM products;

SELECT product_name FROM products WHERE price < 5000;

SELECT product_name, product_id, stock
FROM products
WHERE stock > 10;

SELECT product_name
FROM products
WHERE price BETWEEN 1000 AND 20000;

SELECT product_name
FROM products
ORDER BY price DESC;

SELECT COUNT(*) AS total_products
FROM products;

SELECT SUM(quantity)
FROM orders
GROUP BY product_id;

SELECT
    o.order_id,
    c.customer_name,
    p.product_id,
    o.quantity,
    o.order_status
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN products p
    ON o.product_id = p.product_id;