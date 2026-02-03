-- Supply Chain & Inventory Analysis
-- Goal: Optimize stock levels and prevent stockouts.

-- 1. Setup: Create Table
CREATE TABLE supply_chain_inventory (
    ProductID VARCHAR(20) PRIMARY KEY,
    Category VARCHAR(50),
    InventoryLevel INT,
    MonthlyDemand INT,
    LeadTimeDays INT,
    ReorderPoint INT,
    StockoutRisk VARCHAR(10),
    SupplierRating DECIMAL(3,1)
);

-- 2. Analysis: Stockout Risk Assessment
-- Insight: Identify products where inventory is critically low compared to demand.
SELECT 
    ProductID,
    Category,
    InventoryLevel,
    MonthlyDemand,
    CASE 
        WHEN InventoryLevel < MonthlyDemand * 0.5 THEN 'Critical'
        WHEN InventoryLevel < MonthlyDemand THEN 'Warning'
        ELSE 'Safe' 
    END as Status
FROM supply_chain_inventory
WHERE InventoryLevel < MonthlyDemand
ORDER BY InventoryLevel ASC;

-- 3. Analysis: Supplier Performance
-- Insight: Do lower-rated suppliers cause longer lead times?
SELECT 
    CASE 
        WHEN SupplierRating >= 4.0 THEN 'High Rated'
        WHEN SupplierRating >= 3.0 THEN 'Medium Rated'
        ELSE 'Low Rated' 
    END as SupplierTier,
    AVG(LeadTimeDays) as AvgLeadTime
FROM supply_chain_inventory
GROUP BY 1
ORDER BY AvgLeadTime DESC;

-- 4. Analysis: Reorder Point Validation
-- Insight: Are current reorder points sufficient?
SELECT 
    ProductID,
    ReorderPoint,
    (MonthlyDemand / 30 * LeadTimeDays) as TheoreticalMinimumStock
FROM supply_chain_inventory
WHERE ReorderPoint < (MonthlyDemand / 30 * LeadTimeDays);
