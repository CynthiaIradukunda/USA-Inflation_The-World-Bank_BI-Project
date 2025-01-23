# USA Climate, Food Production, and Inflation Analysis 

## Project Summary
Using Python, analyzed relationships between climate factors, food production, and inflation employing ETL processes to clean and merge data. In addition, I developed Tableau dashboards to visualize key correlations.

## Problem
This project investigates the relationship between USA climate variables, food production, and inflation. Extreme weather conditions affect crop and livestock productivity, leading to supply chain disruptions and spikes in inflation rates. The study aims to assess how changes in precipitation and temperature impact food production and how food production affects inflation.

## Data
1. NOAA Climate Data (1895–2021):
- Annual Precipitation
- Average, Minimum, and Maximum Temperatures
  
2. FAO Food Production Data (1961–2020):
- Area Harvested, Yield, and Production (focused on production in tonnes)
  
3. World Bank Inflation Data (1960–2021):
- Annual consumer prices (% change) for the United States

## Methodology and Tools

1. Data Cleaning with Python:
  - Reformatted years for consistency across datasets.
  - Removed redundant or irrelevant rows and columns.
  - Converted data types for compatibility during analysis.
2. Data Merging:
  - Merged datasets on the “Year” column using left joins.
3. Statistical Analysis:
  - Correlation analysis to evaluate relationships.
  - R and p-values were used to derive statistical significance.
4. Programming and Visualization Tools:
  - Python: for ETL and initial cleaning.
  - R: for statistical analysis and trends derivation
  - Tableau Dashboards: For correlation and trends 

## Results and Key Takeaways

### Results
1. Climate and Food Production Correlations:
- Annual Precipitation vs Food Production:
    - Significant positive relationship (10% variance explained; p = 0.01).
- Average Temperature vs Food Production:
    - Strong positive relationship (39% variance explained; p < 0.001).
- Minimum Temperature vs Food Production:
    - Strongest positive relationship (47% variance explained; p < 0.001).
- Maximum Temperature vs Food Production:
    - Positive relationship (27% variance explained; p < 0.001).
      
2. Food Production and Inflation:
    - Significant negative relationship between food production and inflation rates (8% variance explained; p = 0.03).

![image](https://github.com/user-attachments/assets/5d2b3aac-ffb1-4181-8b50-8c39fd2ee0c3)


### Key Takeaways
- Climate variables, especially temperature, significantly affect food production, highlighting the need for predictive climate monitoring to mitigate risks.
- Food production fluctuations correlate with inflation, offering insights for policy and supply chain planning.
