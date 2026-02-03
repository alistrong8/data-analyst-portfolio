-- Web Traffic & Conversion Funnel Analysis
-- Goal: Analyze user drop-off points to optimize conversion rates.

-- 1. Setup: Create Table
CREATE TABLE web_traffic (
    SessionID VARCHAR(20) PRIMARY KEY,
    Date DATE,
    Source VARCHAR(20),
    Device VARCHAR(20),
    IsBounce VARCHAR(3),
    ViewedProduct VARCHAR(3),
    AddToCart VARCHAR(3),
    Purchase VARCHAR(3),
    SessionDurationSec INT
);

-- 2. Analysis: Conversion Funnel
-- Insight: Where are we losing the most users?
SELECT 
    COUNT(*) as TotalSessions,
    SUM(CASE WHEN ViewedProduct = 'Yes' THEN 1 ELSE 0 END) as ViewedProduct,
    SUM(CASE WHEN AddToCart = 'Yes' THEN 1 ELSE 0 END) as AddedToCart,
    SUM(CASE WHEN Purchase = 'Yes' THEN 1 ELSE 0 END) as Purchased,
    -- Calculate Drop-off Rates
    ROUND(SUM(CASE WHEN Purchase = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as OverallConversionRate
FROM web_traffic;

-- 3. Analysis: Bounce Rate by Device
-- Insight: Is the mobile experience causing users to leave?
SELECT 
    Device,
    COUNT(*) as Sessions,
    ROUND(SUM(CASE WHEN IsBounce = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as BounceRate
FROM web_traffic
GROUP BY Device
ORDER BY BounceRate DESC;

-- 4. Analysis: Source Quality
-- Insight: Which marketing source brings the most engaged users (longest duration)?
SELECT 
    Source,
    AVG(SessionDurationSec) as AvgDurationSeconds,
    ROUND(SUM(CASE WHEN Purchase = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as ConversionRate
FROM web_traffic
GROUP BY Source
ORDER BY ConversionRate DESC;
