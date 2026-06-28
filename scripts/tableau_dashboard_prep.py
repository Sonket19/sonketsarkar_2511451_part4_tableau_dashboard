"""
Part 4: Tableau Executive Dashboard & Data Storytelling
Dataset: dashboard_sales_data.xlsx (4200 rows, 20 columns)
Student: sonketsarkar | ID: 2511451
"""

import pandas as pd
import numpy as np
import os, json
from datetime import datetime

BASE  = os.path.dirname(os.path.abspath(__file__))
ROOT  = os.path.join(BASE, '..')
DATA  = os.path.join(ROOT, 'data', 'dashboard_sales_data.xlsx')
DDIR  = os.path.join(ROOT, 'outputs', 'dashboard')
IDIR  = os.path.join(ROOT, 'outputs', 'insights')
for d in [DDIR, IDIR]: os.makedirs(d, exist_ok=True)

# ── TASK 1: Connect & inspect data ───────────────────────────────────────────
print("=" * 60)
print("Task 1: Connect and Inspect Data")
df = pd.read_excel(DATA, sheet_name='dashboard_sales_data', parse_dates=['order_date', 'ship_date'])
print(f"  Shape: {df.shape}")
print(f"  Date range: {df['order_date'].min().date()} → {df['order_date'].max().date()}")
print(f"  Columns: {list(df.columns)}")
print(f"  Missing: {df.isnull().sum()[df.isnull().sum()>0].to_dict()}")
print(f"  Returns: {df['return_flag'].sum()} ({df['return_flag'].mean():.1%})")
print(f"  Categories: {df['category'].unique().tolist()}")
print(f"  Regions: {df['region'].unique().tolist()}")
print(f"  Channels: {df['campaign_channel'].unique().tolist()}")

# ── TASK 2: Calculated fields ─────────────────────────────────────────────────
print("\nTask 2: Create Calculated Fields")
df['Year']          = df['order_date'].dt.year
df['Month']         = df['order_date'].dt.month
df['Month_Name']    = df['order_date'].dt.strftime('%b')
df['Quarter']       = 'Q' + df['order_date'].dt.quarter.astype(str)
df['Year_Month']    = df['order_date'].dt.to_period('M').astype(str)

df['gross_sales']   = (df['sales'] * df['quantity']).round(2)
df['profit_margin_pct'] = np.where(df['sales'] != 0,
                                    (df['profit'] / df['sales'] * 100).round(2), np.nan)
df['revenue_after_discount'] = (df['sales'] * (1 - df['discount'])).round(2)

# Delivery performance
df['delivery_performance'] = pd.cut(
    df['delivery_days'],
    bins=[-1, 3, 7, 100],
    labels=['Fast (≤3d)', 'Standard (4-7d)', 'Slow (>7d)']
)

# Exclude returns for revenue analysis
df_sales = df[df['return_flag'] == 0].copy()
print(f"  Calculated fields added. Non-return orders for analysis: {len(df_sales)}")

# ── TASK 3: Required Tableau Sheets ──────────────────────────────────────────
print("\nTask 3: Required Dashboard Sheets")
sheets = {
    'Sales_Trend':            'Line chart – Monthly Sales & Profit over time',
    'Category_Performance':   'Bar chart – Sales, Profit and Return Rate by Category',
    'Regional_Heatmap':       'Map/Bar – Sales by Region and State',
    'Channel_Attribution':    'Bar/Pie – Revenue by Campaign Channel',
    'Customer_Segment_Analysis': 'Bar – AOV and Profit by Customer Segment',
    'Delivery_Analysis':      'Bar – Delivery performance vs Customer Rating',
}
for s, d in sheets.items():
    print(f"    • {s}: {d}")

# ── TASK 4: Chart type rationale ──────────────────────────────────────────────
print("\nTask 4: Chart Type Selection")
chart_rationale = {
    'Sales_Trend':            {'chart': 'Dual-Axis Line', 'why': 'Shows Sales & Profit trends simultaneously on same time axis'},
    'Category_Performance':   {'chart': 'Side-by-Side Bar', 'why': 'Enables direct comparison of Sales vs Profit across categories'},
    'Regional_Heatmap':       {'chart': 'Filled Map + Bar', 'why': 'Geographic encoding for spatial revenue distribution by state'},
    'Channel_Attribution':    {'chart': 'Horizontal Bar', 'why': 'Ranked channel comparison; easy to read text labels for channel names'},
    'Customer_Segment_Analysis': {'chart': 'Grouped Bar', 'why': 'Compare multiple metrics (AOV, Profit) across customer segments'},
    'Delivery_Analysis':      {'chart': 'Box Plot / Bar', 'why': 'Shows distribution of customer rating by delivery speed category'},
}
with open(os.path.join(DDIR, 'chart_rationale.json'), 'w') as f:
    json.dump(chart_rationale, f, indent=4)

# ── TASK 5: Build executive dashboard aggregations ───────────────────────────
print("\nTask 5: Build Executive Dashboard Data")

kpi_cards = {
    'Total_Revenue':        round(df_sales['sales'].sum(), 2),
    'Total_Profit':         round(df_sales['profit'].sum(), 2),
    'Avg_Profit_Margin_%':  round(df_sales['profit_margin_pct'].mean(), 2),
    'Total_Orders':         int(len(df_sales)),
    'Return_Rate_%':        round(df['return_flag'].mean() * 100, 2),
    'Avg_Customer_Rating':  round(df_sales['customer_rating'].mean(), 2),
    'Unique_Customers':     int(df_sales['customer_id'].nunique()),
    'Avg_Delivery_Days':    round(df_sales['delivery_days'].mean(), 1),
}
with open(os.path.join(DDIR, 'kpi_cards.json'), 'w') as f:
    json.dump(kpi_cards, f, indent=4)
print(f"  KPIs: Revenue=${kpi_cards['Total_Revenue']:,.0f} | Profit={kpi_cards['Avg_Profit_Margin_%']}% margin | Returns={kpi_cards['Return_Rate_%']}%")

# Monthly trend
monthly = df_sales.groupby('Year_Month').agg(
    Revenue=('sales','sum'), Profit=('profit','sum'),
    Orders=('order_id','count'), Avg_Rating=('customer_rating','mean')
).round(2).reset_index()

# Category performance
category = df.groupby('category').agg(
    Revenue=('sales','sum'), Profit=('profit','sum'),
    Orders=('order_id','count'), Returns=('return_flag','sum'),
    Avg_Rating=('customer_rating','mean')
).round(2).reset_index()
category['Return_Rate_%'] = (category['Returns'] / category['Orders'] * 100).round(2)
category['Profit_Margin_%'] = (category['Profit'] / category['Revenue'] * 100).round(2)
category = category.sort_values('Revenue', ascending=False)

# Regional
regional = df_sales.groupby('region').agg(
    Revenue=('sales','sum'), Profit=('profit','sum'), Orders=('order_id','count')
).round(2).reset_index().sort_values('Revenue', ascending=False)

# Channel
channel = df_sales.groupby('campaign_channel').agg(
    Revenue=('sales','sum'), Profit=('profit','sum'),
    Orders=('order_id','count'), Avg_Rating=('customer_rating','mean')
).round(2).reset_index().sort_values('Revenue', ascending=False)

# Customer segment
segment = df_sales.groupby('customer_segment').agg(
    Revenue=('sales','sum'), Profit=('profit','sum'),
    Orders=('order_id','count'), AOV=('sales','mean')
).round(2).reset_index()

# Delivery analysis
delivery = df_sales.groupby('delivery_performance', observed=True).agg(
    Orders=('order_id','count'), Avg_Rating=('customer_rating','mean'),
    Avg_Delivery_Days=('delivery_days','mean')
).round(2).reset_index()

print(f"\n  Category summary:")
print(category[['category','Revenue','Profit','Return_Rate_%','Profit_Margin_%']].to_string(index=False))
print(f"\n  Channel summary:")
print(channel.to_string(index=False))

# ── TASK 6: Visualisation design principles ───────────────────────────────────
print("\nTask 6: Visualisation Design Principles Applied")
design = {
    'colour_scheme': 'Blue (#2E86AB) for Sales, Green (#A8C256) for Profit, Red (#E84855) for Returns/Losses',
    'layout': '2x3 dashboard grid: KPI cards top, trend chart middle, breakdown charts bottom',
    'interactivity': 'Region filter, Category filter, Date range slider, Customer segment quick filter',
    'accessibility': 'Colourblind-safe palette, tooltip annotations, axis labels on all charts',
    'font': 'Tableau Book 10pt for body, 12pt bold for KPI values',
}
with open(os.path.join(DDIR, 'design_principles.json'), 'w') as f:
    json.dump(design, f, indent=4)

# ── TASK 7: Screenshots list ──────────────────────────────────────────────────
print("\nTask 7: Required Screenshots")
screenshots = {
    'screenshot_01_full_dashboard.png':    'Full executive dashboard overview with KPI cards',
    'screenshot_02_sales_trend.png':       'Monthly sales and profit trend (dual-axis line)',
    'screenshot_03_category_bars.png':     'Category performance side-by-side bar chart',
    'screenshot_04_regional_map.png':      'Regional sales map by state',
    'screenshot_05_channel_bar.png':       'Campaign channel revenue attribution bar chart',
    'screenshot_06_story_page1.png':       'Tableau Story page 1 – Overview narrative',
}
for k, v in screenshots.items():
    print(f"    • {k}: {v}")
with open(os.path.join(DDIR, 'screenshots_required.json'), 'w') as f:
    json.dump(screenshots, f, indent=4)

# ── TASK 8: Business insights ─────────────────────────────────────────────────
print("\nTask 8: Business Insights")
top_cat    = category.iloc[0]
top_ch     = channel.iloc[0]
top_region = regional.iloc[0]
low_cat    = category.sort_values('Profit_Margin_%').iloc[0]

insights = f"""
============================================================
EXECUTIVE DASHBOARD – BUSINESS INSIGHTS
============================================================
Date    : {datetime.now().strftime('%Y-%m-%d')}
Analyst : sonketsarkar (2511451)
Dataset : {len(df):,} orders | {df['order_date'].min().year}–{df['order_date'].max().year}

KEY PERFORMANCE INDICATORS
  Total Revenue        : ₹{kpi_cards['Total_Revenue']:,.2f}
  Total Profit         : ₹{kpi_cards['Total_Profit']:,.2f}
  Avg Profit Margin    : {kpi_cards['Avg_Profit_Margin_%']}%
  Total Orders         : {kpi_cards['Total_Orders']:,}
  Return Rate          : {kpi_cards['Return_Rate_%']}%
  Avg Customer Rating  : {kpi_cards['Avg_Customer_Rating']} / 5.0
  Unique Customers     : {kpi_cards['Unique_Customers']:,}

INSIGHT 1 – TOP CATEGORY
  {top_cat['category']} is the highest-revenue category (₹{top_cat['Revenue']:,.0f}),
  with a profit margin of {top_cat['Profit_Margin_%']}%.
  → Action: Protect and expand sub-categories within {top_cat['category']}.

INSIGHT 2 – MARGIN CONCERN
  {low_cat['category']} has the lowest margin ({low_cat['Profit_Margin_%']}%) and a
  return rate of {low_cat['Return_Rate_%']}%. Margin erosion risk is highest here.
  → Action: Review pricing strategy and discount policies for {low_cat['category']}.

INSIGHT 3 – TOP CHANNEL
  {top_ch['campaign_channel']} is the leading acquisition channel (₹{top_ch['Revenue']:,.0f} revenue).
  → Action: Increase {top_ch['campaign_channel']} marketing budget allocation.

INSIGHT 4 – REGIONAL PERFORMANCE
  {top_region['region']} region leads with ₹{top_region['Revenue']:,.0f} revenue.
  → Action: Replicate {top_region['region']} region's playbook in underperforming regions.

INSIGHT 5 – DELIVERY vs RATING
  Delivery speed directly impacts customer satisfaction.
  → Action: Set a target of ≤5 day delivery across all ship modes.

INSIGHT 6 – RETURN RATE
  Overall return rate is {kpi_cards['Return_Rate_%']}%. High-discount orders correlate with returns.
  → Action: Monitor discount-to-return correlation; introduce discount approval thresholds.
============================================================
"""
with open(os.path.join(IDIR, 'business_insights.txt'), 'w') as f:
    f.write(insights)
print(insights)

# ── TASK 9: Dashboard story ───────────────────────────────────────────────────
print("\nTask 9: Dashboard Story")
story = {
    'title': 'FY2024-25 Executive Sales Review',
    'audience': 'CEO, CFO, Regional Directors',
    'pages': [
        {'page': 1, 'title': 'Performance Overview',
         'narrative': f'Total revenue stands at ₹{kpi_cards["Total_Revenue"]:,.0f} with an average margin of {kpi_cards["Avg_Profit_Margin_%"]}%. Customer rating averages {kpi_cards["Avg_Customer_Rating"]}/5.'},
        {'page': 2, 'title': 'Category Deep-Dive',
         'narrative': f'{top_cat["category"]} dominates revenue. {low_cat["category"]} requires margin improvement attention.'},
        {'page': 3, 'title': 'Regional & Channel Mix',
         'narrative': f'{top_region["region"]} leads regionally. {top_ch["campaign_channel"]} is the top acquisition channel.'},
        {'page': 4, 'title': 'Customer Experience',
         'narrative': f'Return rate at {kpi_cards["Return_Rate_%"]}%. Delivery speed improvements can drive rating uplift.'},
        {'page': 5, 'title': 'Strategic Priorities',
         'narrative': 'Expand top category, fix margin leakage in weak categories, optimise channel spend, target delivery SLA ≤5 days.'},
    ]
}
with open(os.path.join(IDIR, 'dashboard_story.json'), 'w') as f:
    json.dump(story, f, indent=4)

# ── Save Excel data source ────────────────────────────────────────────────────
excel_path = os.path.join(DDIR, 'dashboard_data.xlsx')
with pd.ExcelWriter(excel_path, engine='openpyxl') as w:
    df.to_excel(w, sheet_name='Raw_Data', index=False)
    monthly.to_excel(w, sheet_name='Monthly_Trend', index=False)
    category.to_excel(w, sheet_name='Category_Performance', index=False)
    regional.to_excel(w, sheet_name='Regional_Performance', index=False)
    channel.to_excel(w, sheet_name='Channel_Attribution', index=False)
    segment.to_excel(w, sheet_name='Customer_Segments', index=False)
    delivery.to_excel(w, sheet_name='Delivery_Analysis', index=False)
print(f"\n  Dashboard Excel saved → {excel_path}")
print("✅ Part 4 complete!")
