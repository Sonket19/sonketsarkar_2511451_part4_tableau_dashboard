# Part 4: Tableau Executive Dashboard & Data Storytelling

**Assignment:** Final Capstone Project – Business Analytics
**Student:** sonketsarkar
**Student ID:** 2511451
**Part:** 4 of 4

---

## 1. Assignment Title
Tableau Executive Dashboard & Data Storytelling

## 2. Business Problem Summary
Senior leadership needs a comprehensive executive dashboard delivering visibility into sales performance, profitability, regional trends, return rates, and channel effectiveness across 2024–2025. The dashboard enables fast evidence-based decisions without requiring stakeholders to run their own queries.

## 3. Dataset Used
- **Source:** Google Drive (provided by instructor)
- **File:** `dashboard_sales_data.xlsx` placed in `data/` folder
- **Records:** 4200 orders from January 2024 to December 2025
- **Key fields:** order_id, order_date, ship_date, customer_id, customer_segment, region, state, city, category, sub_category, product_name, ship_mode, sales, quantity, discount, profit, return_flag, delivery_days, customer_rating, campaign_channel

## 4. Tools Used
- **Tableau Desktop / Tableau Public** – dashboard and story creation
- **Python 3.9+** – data preparation and aggregation
- **pandas** – data wrangling
- **openpyxl** – Excel data source generation

## 5. Steps Performed

| Task | Description |
|------|-------------|
| Task 1 | Connect and inspect data – shape, date range, missing values, return rate |
| Task 2 | Create calculated fields – gross_sales, profit_margin_pct, revenue_after_discount, delivery_performance |
| Task 3 | Build required Tableau sheets – 6 visualisation sheets |
| Task 4 | Select chart types with rationale for each sheet |
| Task 5 | Build executive dashboard – KPI cards and aggregation tables |
| Task 6 | Apply visualisation design principles – colour, layout, accessibility |
| Task 7 | Capture required screenshots as evidence |
| Task 8 | Write business insights from dashboard findings |
| Task 9 | Create Tableau Story with 5 narrative pages |

## 6. Dashboard Sheets

| Sheet | Chart Type | Purpose |
|-------|-----------|---------|
| Sales_Trend | Dual-Axis Line | Monthly Revenue and Profit over time |
| Category_Performance | Side-by-Side Bar | Sales, Profit and Return Rate by Category |
| Regional_Heatmap | Filled Map and Bar | Sales by Region and State |
| Channel_Attribution | Horizontal Bar | Revenue by Campaign Channel |
| Customer_Segment_Analysis | Grouped Bar | AOV and Profit by Customer Segment |
| Delivery_Analysis | Bar | Delivery performance vs Customer Rating |

## 7. Calculated Fields in Tableau

| Field | Formula |
|-------|---------|
| Gross Sales | [sales] * [quantity] |
| Profit Margin % | [profit] / [sales] * 100 |
| Revenue After Discount | [sales] * (1 - [discount]) |
| Delivery Performance | IF [delivery_days] <= 3 THEN "Fast" ELSEIF [delivery_days] <= 7 THEN "Standard" ELSE "Slow" END |

## 8. Key Outputs

| Output File | Description |
|-------------|-------------|
| `tableau/dashboard.twb` | Tableau workbook |
| `outputs/dashboard/dashboard_data.xlsx` | Prepared Excel data source with all aggregations |
| `outputs/dashboard/kpi_cards.json` | KPI summary values |
| `outputs/insights/business_insights.txt` | Written business insights |
| `outputs/insights/dashboard_story.json` | Tableau Story narrative structure |

## 9. Business Insights
- Total Revenue ₹208,255,582 across 4009 non-return orders
- Average profit margin 13.26% with 4.55% return rate
- Technology dominates revenue (74%) with highest margin (18.22%)
- Furniture has lowest margin (6.89%) and highest return rate (7.67%)
- Organic is the top acquisition channel at ₹85M revenue
- South region leads all regions in total revenue

## 10. Assumptions Made
- Return orders (return_flag=1) excluded from revenue and profit analysis
- delivery_days already calculated in dataset as difference between order and ship date
- Missing customer_rating (32 rows) and campaign_channel (24 rows) excluded from those aggregations
- Dashboard designed for 1920x1080 resolution

## 11. Screenshots
Screenshots are in the `screenshots/` folder showing the Tableau dashboard and each sheet.

## Folder Structure
## How to Run
```bash
pip install pandas numpy openpyxl
python scripts/tableau_dashboard_prep.py
```
Then open dashboard_data.xlsx in Tableau to build the dashboard.
