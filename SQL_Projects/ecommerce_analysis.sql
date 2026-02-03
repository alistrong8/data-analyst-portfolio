-- E-commerce Sales Analysis Project
-- Database: PostgreSQL / MySQL Compatible
-- Goal: Analyze sales performance, identify top products, and understand regional trends.

-- 1. Setup: Create Table to import the CSV data
CREATE TABLE ecommerce_sales (
    TransactionID VARCHAR(20) PRIMARY KEY,
    Date DATE,
    CustomerID VARCHAR(20),
    Region VARCHAR(20),
    Category VARCHAR(50),
    Product VARCHAR(50),
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    TotalPrice DECIMAL(10,2),
    PaymentMethod VARCHAR(20)
);

-- 2. Analysis: Monthly Sales Trends
-- Insight: Determine which months have the highest revenue to optimize marketing spend.
SELECT 
    TO_CHAR(Date, 'YYYY-MM') as Month, 
    SUM(TotalPrice) as TotalRevenue,
    COUNT(TransactionID) as TotalOrders
FROM ecommerce_sales
GROUP BY 1
ORDER BY 1;

-- 3. Analysis: Top Performing Products by Region
-- Insight: Identify regional preferences to tailor inventory and promotions.
WITH RankedProducts AS (
    SELECT 
        Region,
        Product,
        SUM(TotalPrice) as Revenue,
        RANK() OVER (PARTITION BY Region ORDER BY SUM(TotalPrice) DESC) as Rank
    FROM ecommerce_sales
GROUP BY Region, Product
)
SELECT * FROM RankedProducts WHERE Rank <= 3;

-- 4. Analysis: Customer Value (RFM Proxy)
-- Insight: Identify high-value customers based on spending.
SELECT 
    CustomerID,
    COUNT(TransactionID) as Frequency,
    SUM(TotalPrice) as MonetaryValue,
    MAX(Date) as LastPurchaseDate
FROM ecommerce_sales
GROUP BY CustomerID
ORDER BY MonetaryValue DESC
LIMIT 10;

-- 5. Analysis: Category Performance vs Payment Method
-- Insight: Do customers buying expensive electronics prefer Credit Cards?
SELECT 
    Category,
    PaymentMethod,
    COUNT(TransactionID) as Transactions,
    AVG(TotalPrice) as AvgOrderValue
FROM ecommerce_sales
GROUP BY Category, PaymentMethod
ORDER BY Category, AvgOrderValue DESC;
