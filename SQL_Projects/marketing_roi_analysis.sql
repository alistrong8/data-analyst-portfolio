-- Marketing Campaign ROI Analysis
-- Goal: Evaluate campaign performance across channels to optimize spend.

-- 1. Setup: Create Table
CREATE TABLE marketing_campaigns (
    CampaignID VARCHAR(20) PRIMARY KEY,
    Channel VARCHAR(50),
    Spend DECIMAL(10,2),
    Impressions INT,
    Clicks INT,
    Conversions INT,
    Revenue DECIMAL(10,2),
    StartDate DATE
);

-- 2. Analysis: ROAS (Return on Ad Spend) by Channel
-- Insight: Which channel gives the best bang for the buck?
SELECT 
    Channel,
    SUM(Spend) as TotalSpend,
    SUM(Revenue) as TotalRevenue,
    ROUND(SUM(Revenue) / NULLIF(SUM(Spend),0), 2) as ROAS
FROM marketing_campaigns
GROUP BY Channel
ORDER BY ROAS DESC;

-- 3. Analysis: Conversion Rates (CTR & CVR)
-- Insight: Identify engagement vs purchase intent.
SELECT 
    Channel,
    SUM(Clicks) * 100.0 / NULLIF(SUM(Impressions), 0) as CTR_Pct,
    SUM(Conversions) * 100.0 / NULLIF(SUM(Clicks), 0) as CVR_Pct
FROM marketing_campaigns
GROUP BY Channel;

-- 4. Analysis: Cost Per Acquisition (CPA)
-- Insight: How much does it cost to acquire a paying customer?
SELECT 
    CampaignID,
    Channel,
    Spend / NULLIF(Conversions, 0) as CPA
FROM marketing_campaigns
ORDER BY CPA ASC -- Lower is better
LIMIT 10;
