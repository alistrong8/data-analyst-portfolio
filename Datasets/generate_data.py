import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set seed for reproducibility
np.random.seed(42)

BASE_DIR = "/Users/mac/Desktop/App/portfolio/data-analyst-portfolio/Datasets"
os.makedirs(BASE_DIR, exist_ok=True)

def generate_ecommerce_data(n_rows=2000):
    print("Generating Ecommerce Data...")
    products = {
        'Electronics': [('Laptop', 1200), ('Headphones', 150), ('Smartphone', 800), ('Monitor', 300)],
        'Clothing': [('T-Shirt', 25), ('Jeans', 60), ('Jacket', 120), ('Sneakers', 90)],
        'Home': [('Coffee Maker', 80), ('Blender', 45), ('Desk', 150), ('Chair', 100)]
    }
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(n_rows):
        cat = random.choice(list(products.keys()))
        prod, price = random.choice(products[cat])
        
        # Add some price variation
        actual_price = round(price * np.random.uniform(0.9, 1.1), 2)
        qty = np.random.randint(1, 5)
        
        date = start_date + timedelta(days=np.random.randint(0, 365*2))
        
        row = {
            'TransactionID': f'TRX-{10000+i}',
            'Date': date.strftime('%Y-%m-%d'),
            'CustomerID': f'CUST-{np.random.randint(100, 500)}',
            'Region': random.choice(['North', 'South', 'East', 'West']),
            'Category': cat,
            'Product': prod,
            'Quantity': qty,
            'UnitPrice': actual_price,
            'TotalPrice': round(actual_price * qty, 2),
            'PaymentMethod': random.choice(['Credit Card', 'PayPal', 'Debit Card'])
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_DIR}/ecommerce_sales.csv", index=False)
    print(f"Saved {BASE_DIR}/ecommerce_sales.csv")

def generate_churn_data(n_rows=1000):
    print("Generating Churn Data...")
    data = []
    start_date = datetime(2022, 1, 1)
    
    for i in range(n_rows):
        sub_date = start_date + timedelta(days=np.random.randint(0, 700))
        contract = random.choice(['Month-to-Month', 'One Year', 'Two Year'])
        monthly_bill = round(np.random.uniform(30, 120), 2)
        
        # Correlation: Month-to-month + High Bill = Higher Churn Probability
        base_churn_prob = 0.2
        if contract == 'Month-to-Month': base_churn_prob += 0.3
        if monthly_bill > 100: base_churn_prob += 0.1
        
        churn = 'Yes' if np.random.random() < base_churn_prob else 'No'
        
        row = {
            'CustomerID': f'SUB-{1000+i}',
            'SubscriptionDate': sub_date.strftime('%Y-%m-%d'),
            'ContractType': contract,
            'MonthlyBill': monthly_bill,
            'Age': np.random.randint(18, 70),
            'Gender': random.choice(['Male', 'Female']),
            'TechSupportCalls': np.random.choice([0, 1, 2, 3, 4], p=[0.5, 0.2, 0.15, 0.1, 0.05]),
            'Churn': churn
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_DIR}/customer_retention.csv", index=False)
    print(f"Saved {BASE_DIR}/customer_retention.csv")

def generate_financial_data():
    print("Generating Financial Data...")
    dates = pd.date_range(start='2021-01-01', end='2023-12-31', freq='ME')
    data = []
    
    base_revenue = 50000
    trend = 1000 # Monthly growth
    
    for i, date in enumerate(dates):
        # Seasonality (peak in Dec)
        seasonality = 1.2 if date.month == 12 else 1.0
        
        revenue = (base_revenue + (i * trend)) * seasonality * np.random.uniform(0.95, 1.05)
        cogs = revenue * 0.4 # 40% margin cost
        opex = 15000 + (i * 200) # Fixed + slight growth
        
        row = {
            'Month': date.strftime('%Y-%m'),
            'Revenue': round(revenue, 2),
            'COGS': round(cogs, 2),
            'OpEx': round(opex, 2),
            'NetIncome': round(revenue - cogs - opex, 2),
            'BudgetedRevenue': round(revenue * np.random.uniform(0.9, 1.1), 2)
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_DIR}/financial_forecast.csv", index=False)
    print(f"Saved {BASE_DIR}/financial_forecast.csv")

def generate_hr_data(n_rows=500):
    print("Generating HR Data...")
    depts = ['Sales', 'R&D', 'HR', 'Marketing', 'Finance', 'IT']
    data = []
    
    for i in range(n_rows):
        age = np.random.randint(22, 60)
        dept = random.choice(depts)
        dist_home = np.random.randint(1, 30)
        satisfaction = np.random.randint(1, 5)
        monthly_income = np.random.randint(3000, 15000)
        ot = random.choice(['Yes', 'No'])
        years_at_company = np.random.randint(1, 20)
        
        # Attrition Logic: Low satisfaction + overtime + low income = Higher risk
        attrition_prob = 0.1
        if satisfaction <= 2: attrition_prob += 0.3
        if ot == 'Yes': attrition_prob += 0.15
        if monthly_income < 5000: attrition_prob += 0.1
        
        attrition = 'Yes' if np.random.random() < attrition_prob else 'No'
        
        row = {
            'EmployeeID': f'EMP-{100+i}',
            'Age': age,
            'Department': dept,
            'DistanceFromHome_KM': dist_home,
            'JobSatisfaction': satisfaction,
            'MonthlyIncome': monthly_income,
            'OverTime': ot,
            'YearsAtCompany': years_at_company,
            'Attrition': attrition
        }
        data.append(row)
    
    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_DIR}/hr_employee_attrition.csv", index=False)
    print(f"Saved {BASE_DIR}/hr_employee_attrition.csv")

def generate_marketing_data(n_rows=200):
    print("Generating Marketing Data...")
    channels = ['Facebook', 'Google Ads', 'Email', 'LinkedIn', 'Instagram']
    data = []
    
    for i in range(n_rows):
        campaign_id = f'CMP-{100+i}'
        channel = random.choice(channels)
        spend = round(np.random.uniform(500, 5000), 2)
        
        # Performance correlations
        cpc = np.random.uniform(0.5, 5.0)
        clicks = int(spend / cpc)
        ctr = np.random.uniform(0.01, 0.05)
        impressions = int(clicks / ctr)
        
        conv_rate = np.random.uniform(0.02, 0.10)
        conversions = int(clicks * conv_rate)
        revenue = conversions * np.random.uniform(50, 200)
        
        row = {
            'CampaignID': campaign_id,
            'Channel': channel,
            'Spend': spend,
            'Impressions': impressions,
            'Clicks': clicks,
            'Conversions': conversions,
            'Revenue': round(revenue, 2),
            'StartDate': (datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 300))).strftime('%Y-%m-%d')
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_DIR}/marketing_campaigns.csv", index=False)
    print(f"Saved {BASE_DIR}/marketing_campaigns.csv")

def generate_supply_chain_data(n_rows=100):
    print("Generating Supply Chain Data...")
    data = []
    
    for i in range(n_rows):
        prod_id = f'SKU-{1000+i}'
        category = random.choice(['Electronics', 'Clothing', 'Home', 'Industrial'])
        demand = np.random.randint(50, 500)
        stock = np.random.randint(0, 600)
        lead_time = np.random.randint(5, 60)
        
        stockout_risk = 'High' if stock < demand else 'Low'
        
        row = {
            'ProductID': prod_id,
            'Category': category,
            'InventoryLevel': stock,
            'MonthlyDemand': demand,
            'LeadTimeDays': lead_time,
            'ReorderPoint': int(demand * (lead_time/30) * 1.5),
            'StockoutRisk': stockout_risk,
            'SupplierRating': round(np.random.uniform(2.0, 5.0), 1)
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_DIR}/supply_chain_inventory.csv", index=False)
    print(f"Saved {BASE_DIR}/supply_chain_inventory.csv")

def generate_web_traffic_data(n_rows=5000):
    print("Generating Web Traffic Data...")
    sources = ['Organic Search', 'Direct', 'Social', 'Referral', 'Paid Search']
    devices = ['Mobile', 'Desktop', 'Tablet']
    data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(n_rows):
        session_date = start_date + timedelta(days=np.random.randint(0, 365))
        source = random.choice(sources)
        device = random.choice(devices)
        
        # Behavior Logic
        bounce_prob = 0.4
        if device == 'Mobile': bounce_prob += 0.15
        if source == 'Social': bounce_prob += 0.1
        
        is_bounce = 'Yes' if np.random.random() < bounce_prob else 'No'
        
        # Funnel
        viewed_product = 'Yes' if is_bounce == 'No' else 'No'
        add_to_cart = 'Yes' if viewed_product == 'Yes' and np.random.random() < 0.3 else 'No'
        purchase = 'Yes' if add_to_cart == 'Yes' and np.random.random() < 0.4 else 'No'
        
        row = {
            'SessionID': f'SES-{10000+i}',
            'Date': session_date.strftime('%Y-%m-%d'),
            'Source': source,
            'Device': device,
            'IsBounce': is_bounce,
            'ViewedProduct': viewed_product,
            'AddToCart': add_to_cart,
            'Purchase': purchase,
            'SessionDurationSec': np.random.randint(5, 600) if is_bounce == 'No' else np.random.randint(0, 10)
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_DIR}/web_traffic_funnel.csv", index=False)
    print(f"Saved {BASE_DIR}/web_traffic_funnel.csv")

def generate_public_health_data():
    print("Generating Public Health Data...")
    # Time series of a hypothetical outbreak or health metric (e.g., Flu Cases)
    dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='W')
    data = []
    
    base_cases = 500
    
    for date in dates:
        # Seasonal trend (higher in winter)
        month = date.month
        seasonality = 1.5 if month in [11, 12, 1, 2] else 0.8
        
        # Random noise + Trend
        cases = int(base_cases * seasonality * np.random.uniform(0.8, 1.2))
        hospitalizations = int(cases * 0.15 * np.random.uniform(0.9, 1.1))
        recoveries = int(cases * 0.95)
        
        row = {
            'WeekEnding': date.strftime('%Y-%m-%d'),
            'Region': 'National',
            'NewCases': cases,
            'Hospitalizations': hospitalizations,
            'Recoveries': recoveries,
            'VaccinationRate': min(100, 5 + (date.year - 2020) * 30 + np.random.randint(0, 5)) # Increasing trend
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_DIR}/public_health_trends.csv", index=False)
    print(f"Saved {BASE_DIR}/public_health_trends.csv")

if __name__ == "__main__":
    generate_ecommerce_data()
    generate_churn_data()
    generate_financial_data()
    generate_hr_data()
    generate_marketing_data()
    generate_supply_chain_data()
    generate_web_traffic_data()
    generate_public_health_data()
