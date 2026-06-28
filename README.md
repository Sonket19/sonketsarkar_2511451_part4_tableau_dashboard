# Part 4: Tableau Executive Dashboard & Data Storytelling

**Student:** sonketsarkar | **ID:** 2511451 | **Part:** 4 of 4

## Business Problem
Senior leadership needs an executive dashboard delivering visibility into sales performance, profitability, regional trends, return rates, and channel effectiveness across 2024-2025.

## Dataset
- File: dashboard_sales_data.xlsx
- Records: 4200 orders, 20 columns
- Date range: January 2024 to December 2025
- Fields: order_id, order_date, ship_date, customer_id, customer_segment, region, state, city, category, sub_category, product_name, ship_mode, sales, quantity, discount, profit, return_flag, delivery_days, customer_rating, campaign_channel

## Tools
Tableau Desktop/Public, Python 3.9, pandas, openpyxl

## Tasks Completed
| Task | Description |
|------|-------------|
| Task 1 | Connect and inspect data - shape, date range, missing values, return rate |
| Task 2 | Create calculated fields - gross_sales, profit_margin_pct, revenue_after_discount, delivery_performance |
| Task 3 | Build required Tableau sheets - 6 visualisation sheets |
| Task 4 | Select chart types with rationale for each sheet |
| Task 5 | Build executive dashboard - KPI cards and filters |
| Task 6 | Apply visualisation design principles - colour, layout, accessibility |
| Task 7 | Capture required screenshots as evidence |
| Task 8 | Write business insights from dashboard findings |
| Task 9 | Create Tableau Story with 5 narrative pages |

## Dashboard Sheets
| Sheet | Chart Type | Purpose |
|-------|-----------|---------|
| Sales_Trend | Dual-Axis Line | Monthly Revenue and Profit over time |
| Category_Performance | Side-by-Side Bar | Sales, Profit and Return Rate by Category |
| Regional_Heatmap | Filled Map | Sales by Region and State |
| Channel_Attribution | Horizontal Bar | Revenue by Campaign Channel |
| Customer_Segment_Analysis | Grouped Bar | AOV and Profit by Customer Segment |
| Delivery_Analysis | Bar | Delivery performance vs Customer Rating |

## Calculated Fields in Tableau
| Field | Formula |
|-------|---------|
| Gross Sales | [sales] * [quantity] |
| Profit Margin % | [profit] / [sales] * 100 |
| Revenue After Discount | [sales] * (1 - [discount]) |
| Delivery Performance | IF [delivery_days] <= 3 THEN "Fast" ELSEIF [delivery_days] <= 7 THEN "Standard" ELSE "Slow" END |

## Outputs
| File | Description |
|------|-------------|
| tableau/dashboard.twb | Tableau workbook file |
| outputs/dashboard/dashboard_data.xlsx | Prepared Excel data source |
| outputs/dashboard/kpi_cards.json | KPI summary values |
| outputs/insights/business_insights.txt | Written business insights |
| outputs/insights/dashboard_story.json | Tableau Story narrative |

## Key Findings
- Total Revenue 208255582 across 4009 non-return orders
- Average profit margin 13.26% with 4.55% return rate
- Technology dominates revenue at 74% with highest margin of 18.22%
- Furniture has lowest margin 6.89% and highest return rate 7.67%
- Organic is the top acquisition channel at 85 million revenue
- South region leads all regions in total revenue

## Assumptions
- Return orders excluded from revenue and profit analysis
- Missing customer_rating and campaign_channel excluded from those aggregations
- Dashboard designed for 1920x1080 resolution

## How to Run
pip install pandas numpy openpyxl

python scripts/tableau_dashboard_prep.py
Then open dashboard_data.xlsx in Tableau to build the dashboard.
