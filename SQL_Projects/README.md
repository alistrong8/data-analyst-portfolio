# SQL Projects Case Studies

This collection demonstrates my ability to write efficient, complex queries to extract meaning from raw relational data.

---

## 1. E-commerce Sales Analysis
**File:** [ecommerce_analysis.sql](ecommerce_analysis.sql)

### 🎯 Business Goal
To understand monthly revenue trends and identify the most valuable customers.

### 🛠 Techniques Used
- **CTEs (Common Table Expressions)**: To structure the analysis of "Top Performing Regions" before joining back to main sales data.
- **Window Functions (`RANK()`)**: Used to rank products by revenue *within each region* to find local bestsellers.
- **Date Functions (`TO_CHAR`)**: Aggregated daily transactions into monthly cohorts.

```sql
-- Snippet: Finding Top Products per Region
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
```
*Relevance: Shows ability to perform advanced segmentation.*

---

## 2. Customer Churn Investigation
**File:** [churn_analysis.sql](churn_analysis.sql)

### 🎯 Business Goal
To determine if contract type influences customer retention.

### 🛠 Techniques Used
- **CASE Statements**: Used to create binary flags (`Churned_Num`) for statistical calculation from text columns.
- **Aggregate Functions**: Calculated `Churn Rate %` across different dimensions (Contract, Age Group).

```sql
-- Snippet: Calculating Churn Rate
SELECT 
    ContractType,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as ChurnRatePct
FROM customer_churn
GROUP BY ContractType;
```
*Relevance: Critical for subscription-based businesses.*

---

## 3. Marketing Campaign ROI
**File:** [marketing_roi_analysis.sql](marketing_roi_analysis.sql)

### 🎯 Business Goal
To optimize marketing spend by identifying channels with the highest Return on Ad Spend (ROAS).

### 🛠 Techniques Used
- **Arithmetic Operations**: Calculated `ROAS` (Revenue/Spend) and `CPA` (Spend/Conversions).
- **NULL Handling (`NULLIF`)**: Prevented division-by-zero errors in calculations.

### 💡 Key Insight
- **Facebook Ads** had the highest volume, but **Email Marketing** had the highest ROAS (4.5x), suggesting we should increase the email budget.

---

## 4. Supply Chain Stockout Risk
**File:** [supply_chain_analysis.sql](supply_chain_analysis.sql)

### 🎯 Business Goal
To proactively identify products at risk of running out of stock.

### 🛠 Techniques Used
- **Complex Filtering**: Isolated products where `Inventory < Monthly Demand` but `Supplier Rating < 3.0` (High Risk).
- **Subqueries**: Validated reorder points against theoretical minimums.

### 💡 Key Insight
- Suppliers with ratings below 3.0 have a **20% longer lead time**, contributing to stockouts.
