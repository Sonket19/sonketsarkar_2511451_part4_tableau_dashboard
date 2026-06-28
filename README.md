# Part 4: Tableau Executive Dashboard & Data Storytelling

**Assignment:** Final Capstone Project – Business Analytics  
**Student:** sonketsarkar  
**Student ID:** 2511451  
**Part:** 4 of 4  

---

## 1. Assignment Title
Tableau Executive Dashboard & Data Storytelling

## 2. Business Problem Summary
Senior leadership needs a comprehensive, self-service **Executive Dashboard** that delivers real-time visibility into sales performance, profitability, regional trends, and channel effectiveness. The dashboard must tell a clear data story that enables fast, evidence-based decisions without requiring stakeholders to run their own queries.

## 3. Dataset Used
- **Source:** Google Drive (provided by instructor)
- **File:** `dashboard_data.csv` → placed in `data/` folder
- **Records:** ~2,000 orders spanning Jan 2023 – Jun 2024
- **Key fields:** Order_ID, Customer_ID, Order_Date, Category, Sub_Category, Region, Channel, Sales_Manager, Loyalty_Tier, Sales, Profit, Discount, Quantity, Shipping_Days

## 4. Tools Used
- **Tableau Desktop / Tableau Public** – dashboard and story creation
- **Python 3.10+** – data preparation and calculated field documentation
- **pandas** – data wrangling and aggregation
- **openpyxl** – Excel data source generation

## 5. Steps Performed

| Task | Description |
|------|-------------|
| Task 1 | Connect and inspect data in Tableau |
| Task 2 | Create calculated fields (Gross Sales, Profit Margin %, Discount Category, etc.) |
| Task 3 | Build required Tableau sheets (6 visualisation sheets) |
| Task 4 | Select appropriate chart types with rationale |
| Task 5 | Build executive dashboard with KPI cards and filters |
| Task 6 | Apply visualisation design principles (colour, layout, accessibility) |
| Task 7 | Capture required screenshots as evidence |
| Task 8 | Write business insights derived from the dashboard |
| Task 9 | Create Tableau Story with 5 narrative pages |
| Task 10 | Explain chart selection for each visualisation |

## 6. Dashboard Sheets

| Sheet Name | Chart Type | Purpose |
|------------|-----------|---------|
| Sales Overview | Dual-Axis Line Chart | Monthly Revenue & Profit trend |
| Category Profitability | Horizontal Bar Chart | Sales & Profit ranked by category |
| Regional Performance | Filled Map | Geographic revenue distribution |
| Channel Mix | Treemap | Revenue share by channel |
| Manager Leaderboard | Bar Chart with Labels | Top performers ranking |
| Discount Impact | Scatter Plot | Discount rate vs Profit margin |

## 7. Calculated Fields (Tableau)

| Field Name | Formula |
|------------|---------|
| Gross Sales | `[Sales] * [Quantity]` |
| Profit Margin % | `[Profit] / [Sales] * 100` |
| Revenue After Discount | `[Sales] * (1 - [Discount])` |
| Estimated CLV | `[Avg Order Value] * [Purchase Frequency] * 12` |
| Shipping Performance | `IF [Shipping Days] <= 3 THEN "Fast" ELSEIF [Shipping Days] <= 7 THEN "Standard" ELSE "Slow" END` |

## 8. Key Outputs

| Output File | Description |
|-------------|-------------|
| `tableau/dashboard.twb` | Tableau workbook with full dashboard |
| `outputs/dashboard/dashboard_data.xlsx` | Prepared Excel data source |
| `outputs/dashboard/kpi_cards.json` | KPI summary values |
| `outputs/insights/business_insights.txt` | Written business insights |
| `outputs/insights/dashboard_story.json` | Tableau Story narrative structure |

## 9. Business Insights
1. **Electronics** drives 30% of total revenue; highest absolute profit
2. **Home Decor** has the best profit margin at ~28% — ideal for margin-focused growth
3. **Online channel** accounts for 50% of orders; Mobile growing fastest at 2x rate
4. **High discounts (>20%)** erode margins by 8+ percentage points vs low-discount orders
5. **Q4 seasonality** is pronounced — holiday season represents 32% of annual revenue
6. **North region** leads but South and West show untapped growth potential

## 10. Assumptions Made
- Order-level data is grain for all calculations
- Profit is pre-tax and excludes overhead allocation
- Tableau filters applied: Date range, Region, Category (as dashboard parameters)
- Dashboard designed for 1920×1080 resolution (Executive presentation format)
- Colour scheme: Corporate blue (#2E86AB) for positive metrics, orange (#E84855) for alerts

## 11. Screenshots
Screenshots in the `screenshots/` folder:
- `screenshot_01_dashboard_overview.png` – Full executive dashboard
- `screenshot_02_sales_trend.png` – Monthly sales line chart
- `screenshot_03_category_analysis.png` – Category profitability bar chart
- `screenshot_04_regional_map.png` – Geographic sales map
- `screenshot_05_discount_scatter.png` – Discount vs margin scatter
- `screenshot_06_story_view.png` – Tableau Story narrative

## Folder Structure
```
sonketsarkar_2511451_part4_tableau_dashboard/
├── data/
│   └── dashboard_data.csv
├── scripts/
│   └── tableau_dashboard_prep.py
├── tableau/
│   └── dashboard.twb
├── outputs/
│   ├── dashboard/
│   │   ├── dashboard_data.xlsx
│   │   └── kpi_cards.json
│   └── insights/
│       ├── business_insights.txt
│       └── dashboard_story.json
├── screenshots/
│   ├── screenshot_01_dashboard_overview.png
│   ├── screenshot_02_sales_trend.png
│   ├── screenshot_03_category_analysis.png
│   ├── screenshot_04_regional_map.png
│   ├── screenshot_05_discount_scatter.png
│   └── screenshot_06_story_view.png
└── README.md
```

## How to Run

### Step 1 – Prepare data
```bash
# Install dependencies
pip install pandas numpy openpyxl

# Generate/prepare dashboard data
python scripts/tableau_dashboard_prep.py
```

### Step 2 – Open in Tableau
1. Open **Tableau Desktop** or **Tableau Public**
2. Connect to `outputs/dashboard/dashboard_data.xlsx`
3. Open `tableau/dashboard.twb` (or build from scratch using the sheet specs above)
4. All calculated fields are documented in the script and README

### Step 3 – Export
- Export dashboard as PDF for submission evidence
- Take screenshots of each required sheet
