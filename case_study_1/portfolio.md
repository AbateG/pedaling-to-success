# 🚴 Case Study 1: Cyclistic Bike-Share - Pedaling to Success 📊

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Tagline:** Pedaling to Success: Unlocking Bike-Share Insights 🚴

## 📖 Introduction

Did you know casual riders take trips **3x longer** on average than members? Dive into this data-driven analysis of Cyclistic's bike-share program to uncover user behavior patterns and drive membership growth.

This case study analyzed 12 months of Cyclistic bike-share trip data to understand usage differences between annual members and casual riders. Using Python and pandas, I processed the data by unzipping files, cleaning invalid entries, transforming columns (e.g., calculating ride length and day of week), and performing descriptive analysis.

## 🎯 Business Task

Maximize annual memberships by understanding how casual riders and members use Cyclistic bikes differently.

## 🛠️ Methodology

- **Data Sources:** Cyclistic trip data (Divvy, 2019-2020)
- **Tools:** Python, Pandas, Plotly, Streamlit
- **Steps:** Data cleaning, aggregation, visualization, interactive dashboard

## 📊 Key Discoveries

| User Type | Avg Ride Length | Peak Day | Insights |
|-----------|-----------------|----------|----------|
| Member | ~14 min | Tuesday (271k rides) | Short commutes |
| Casual | ~40 min | Saturday (144k rides) | Leisure activities |

- Casual riders prefer longer, weekend trips.
- Members use for daily commuting.
- Total rides: 3.8M over 12 months.

## 📈 Visualizations

![Avg Ride Length](docs/avg_ride_by_type.html)
![Rides by Day](docs/rides_by_day.html)

## 💡 Top Recommendations

1. **Weekend Promotions:** Target casuals with discounts on Saturdays/Sundays to boost conversions.
2. **Long-Ride Plans:** Offer perks for rides over 30 minutes to appeal to casual preferences.
3. **Commute Marketing:** Advertise weekday benefits to attract more members.

## 🚀 Interactive App

Explore the data interactively: [Streamlit App](https://your-streamlit-app-link.com) *(Host on Streamlit Cloud)*

## 📁 Repository Structure

```
case_study_1/
├── app.py                 # Streamlit web app
├── analyze.py             # Data analysis script
├── process_data.py        # Data processing
├── viz.py                 # Visualization generation
├── portfolio.md           # This file
├── data/
│   ├── csv_originals/     # Raw trip data
│   └── excel_copies/      # Processed summaries
└── docs/                  # HTML visualizations
```

## 🤝 Contributing

Contributions welcome! Fork and submit PRs.

## 📞 Contact

- **Author:** [Your Name]
- **Email:** your.email@example.com
- **LinkedIn:** [Your LinkedIn]
- **Portfolio:** [Your Portfolio Site]

## 📄 License

Licensed under MIT License.

---

⭐ Star this repo if you enjoyed the analysis!

[![Share on Twitter](https://img.shields.io/badge/Share-Twitter-blue.svg)](https://twitter.com/intent/tweet?text=Explore%20Cyclistic%20Bike-Share%20Insights!&url=https://github.com/your-repo)
[![Share on LinkedIn](https://img.shields.io/badge/Share-LinkedIn-blue.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/your-repo)
