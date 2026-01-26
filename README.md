# 🌊 Boknis Eck Temperature Forecasting

A time series forecasting project analyzing and predicting water temperature from the Boknis Eck marine observation station in the Baltic Sea.

## 📋 Project Overview

**Author:** Jannik Melcher  
**Dataset:** Boknis Eck Timeseries / GEOMAR ([Data Source](https://timeseries.geomar.de/boknis/app/))  
**Target Variable:** CTD Temperature (°C)  
**Date Range:** 1957-05-14 to 2023-03-14  
**Forecast Horizon:** 12 months (24 periods of ~15 days)

## 🎯 Objectives

The Boknis Eck time series is one of the longest continuous marine time series in the Baltic Sea. This project aims to:

1. **Quantify long-term warming trends** against natural seasonal variability
2. **Develop accurate forecasting models** for marine temperature prediction
3. **Support climate monitoring** and ecosystem health assessment
4. **Inform environmental policy** regarding marine protection

## 📊 Key Findings

- **Historical Warming Trend:** ~0.035°C per year
- **Strong Seasonality:** Clear annual cycle with peaks in August/September and troughs in February
- **Best Model:** SARIMA(1,0,1)(1,1,1,24) with MAE of ~1.65°C
- **Baseline Comparison:** Seasonal-Naïve baseline achieves MAE of ~1.54°C

## 🛠️ Methods

### Data Preprocessing
- Resampled to regular 15-day frequency
- Filled gaps (including a 4-year gap from 1979-1983) using **Seasonal Anomaly Interpolation**
- Preserved winter/summer cycles during gap filling

### Models Evaluated
| Model | MAE | RMSE |
|-------|-----|------|
| Random Forest | 1.39 | 1.68 |
| Seasonal-Naïve | 1.54 | 2.13 |
| Ridge Regression | 1.56 | 1.94 |
| SARIMA | 1.65 | 2.05 |
| Naïve Baseline | 6.79 | 8.62 |

### Stationarity Analysis
- ADF and KPSS tests confirmed non-stationarity due to seasonality
- Seasonal differencing (D=1, m=24) successfully achieved stationarity
- No ordinary differencing required (d=0)

## 📁 Project Structure

```
.
├── Capstone/
│   ├── boknis_eck_temperature_jannik_melcher.ipynb  # Main analysis notebook
│   ├── boknis_eck.csv                                # Raw dataset
│   └── Data/
│       ├── LICENSE
│       └── setup.py
├── Practise/
│   ├── ARIMA_GTrends_Apple_Walkthrough_Learner_final (1).ipynb
│   ├── Practise Notebook.ipynb
│   └── [various practice datasets and outputs]
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib statsmodels scikit-learn
```

### Running the Analysis
1. Clone the repository
2. Open `Capstone/boknis_eck_temperature_jannik_melcher.ipynb`
3. Run all cells sequentially

## 📈 Visualizations

The notebook includes:
- Time series plots at various resolutions (15-day, monthly, quarterly, yearly)
- Seasonal decomposition (trend, seasonality, residuals)
- ACF/PACF correlograms for stationarity diagnostics
- Forecast comparison plots with confidence intervals
- 10-year climate trend projections

## ⚠️ Limitations

- **Interpolated Gap:** The 1979-1983 data gap introduces uncertainty in trend estimates
- **Univariate Model:** Does not account for external drivers (Atlantic circulation, salinity, etc.)
- **Linear Trend Assumption:** Assumes historical warming trend continues without acceleration

## 🔮 Future Work

- Incorporate **exogenous variables** (NAO index, air temperature forecasts)
- Explore **deep learning approaches** (LSTM, Transformer models)
- Implement **ensemble methods** combining SARIMA and ML models
- Add **uncertainty quantification** for long-term projections

## 📄 License

See `Capstone/Data/LICENSE` for dataset licensing information.

## 🙏 Acknowledgments

- **GEOMAR Helmholtz Centre for Ocean Research Kiel** for providing the Boknis Eck dataset
- **Tomorrow University** - Advanced Machine Learning: Time Series course
