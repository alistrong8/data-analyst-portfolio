-- Customer Churn Analysis
-- Goal: Identify key drivers of customer churn.

-- 1. Setup: Create Table
CREATE TABLE customer_churn (
    CustomerID VARCHAR(20) PRIMARY KEY,
    SubscriptionDate DATE,
    ContractType VARCHAR(20),
    MonthlyBill DECIMAL(10,2),
    Age INT,
    Gender VARCHAR(10),
    TechSupportCalls INT,
    Churn VARCHAR(3) -- 'Yes' or 'No'
);

-- 2. Analysis: Overall Churn Rate
SELECT 
    COUNT(*) as TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) as ChurnedCustomers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as ChurnRatePct
FROM customer_churn;

-- 3. Analysis: Churn by Contract Type
-- Insight: Month-to-month contracts likely have higher churn.
SELECT 
    ContractType,
    COUNT(*) as Total,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) as Churned,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as ChurnRatePct
FROM customer_churn
GROUP BY ContractType
ORDER BY ChurnRatePct DESC;

-- 4. Analysis: Tech Support Calls vs Churn
-- Insight: Does poor service (more calls) lead to churn?
SELECT 
    TechSupportCalls,
    COUNT(*) as Total,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as ChurnRatePct
FROM customer_churn
GROUP BY TechSupportCalls
ORDER BY TechSupportCalls;

-- 5. Analysis: High Value Customers at Risk
-- Insight: Find high-paying customers on month-to-month contracts who might churn.
SELECT * 
FROM customer_churn
WHERE MonthlyBill > 100 
  AND ContractType = 'Month-to-Month'
  AND Churn = 'No' -- Currently active but at risk
ORDER BY MonthlyBill DESC;
