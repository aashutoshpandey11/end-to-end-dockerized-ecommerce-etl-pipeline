SELECT COUNT(*) FROM products;

SELECT AVG(product_price) FROM products;

SELECT category,
       COUNT(*)
FROM products
GROUP BY category;