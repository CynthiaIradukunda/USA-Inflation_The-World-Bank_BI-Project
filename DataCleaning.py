
import pandas as pd
import numpy as np

# Path for file input. Change as needed
path_in = 'C:\\Data\\ISQS_6339\\Final\\'

# Datasets
file_in_1 = 'USA Inflation Data_The World Bank.csv'
file_in_2 = 'NOAA Annual precip. Data.csv'
file_in_3 = 'NOAA Average Temperatures.csv'
file_in_4 = 'NOAA Max Temperatures.csv'
file_in_5 = 'NOAA Min Temperatures.csv'
file_in_6 = 'FAO Food Production Data.csv'

# Datasets import in python for manipulation
inflation = pd.read_csv(path_in + file_in_1)
precip = pd.read_csv(path_in + file_in_2)
avg_temp = pd.read_csv(path_in + file_in_3)
max_temp = pd.read_csv(path_in + file_in_4)
min_temp = pd.read_csv(path_in + file_in_5)
production = pd.read_csv(path_in + file_in_6)


#Path for file outputs. Change as needed
path_out = 'C:\\Data\\ISQS_6339\\Final\\'

#File name for file outputs. Change as needed
file_out_1 = 'output1.csv'


#-------------------------CLEANING----------------------------
#Clean each dataframe to prepare for merging

#precip File
#Drop the first three rows of the dataset as they are irrelevant to the data values
precip.drop([0,1,2], axis=0, inplace=True)

#Drop Jan-Dec Column
precip.drop(' January-December', axis=1, inplace=True)

#Reset the index after dropping the rows
precip.reset_index(drop=True, inplace=True)

#Rename the first column to Year 
precip.rename(columns = {'Contiguous U.S.':'Year'}, inplace=True)

#Change to datatypes of the two columns to numeric
precip['Year'] = pd.to_numeric(precip['Year'])
precip[' Precipitation'] = pd.to_numeric(precip[' Precipitation'])

#Drop the month value from year column
precip['Year'] = precip['Year'].astype(str).str[:-2].astype(np.int64)


precip.dtypes

#Average Temperature File
#Drop the first three rows of the dataset as they are irrelevant to the data values
avg_temp.drop([0,1,2], axis=0, inplace=True)

#Drop Jan-Dec Column
avg_temp.drop(' January-December', axis=1, inplace=True)

#Reset the index after dropping the rows
avg_temp.reset_index(drop=True, inplace=True)

#Rename the first column to Year 
avg_temp.rename(columns = {'Contiguous U.S.':'Year'}, inplace=True)

#Change to datatypes of the two columns to numeric
avg_temp['Year'] = pd.to_numeric(avg_temp['Year'])
avg_temp[' Average Temperature'] = pd.to_numeric(avg_temp[' Average Temperature'])

#Drop the month value from year column
avg_temp['Year'] = avg_temp['Year'].astype(str).str[:-2].astype(np.int64)

avg_temp.dtypes


#Max Temperature File
#Drop the first three rows of the dataset as they are irrelevant to the data values
max_temp.drop([0,1,2], axis=0, inplace=True)

#Drop Jan-Dec Column
max_temp.drop(' January-December', axis=1, inplace=True)

#Reset the index after dropping the rows
max_temp.reset_index(drop=True, inplace=True)

#Rename the first column to Year 
max_temp.rename(columns = {'Contiguous U.S.':'Year'}, inplace=True)

#Change to datatypes of the two columns to numeric
max_temp['Year'] = pd.to_numeric(max_temp['Year'])
max_temp[' Maximum Temperature'] = pd.to_numeric(max_temp[' Maximum Temperature'])

#Drop the month value from year column
max_temp['Year'] = max_temp['Year'].astype(str).str[:-2].astype(np.int64)

max_temp.dtypes


#Min Temperature File
#Drop the first three rows of the dataset as they are irrelevant to the data values
min_temp.drop([0,1,2], axis=0, inplace=True)

#Drop Jan-Dec Column
min_temp.drop(' January-December', axis=1, inplace=True)

#Reset the index after dropping the rows
min_temp.reset_index(drop=True, inplace=True)

#Rename the first column to Year 
min_temp.rename(columns = {'Contiguous U.S.':'Year'}, inplace=True)

#Change to datatypes of the two columns to numeric
min_temp['Year'] = pd.to_numeric(min_temp['Year'])
min_temp[' Minimum Temperature'] = pd.to_numeric(min_temp[' Minimum Temperature'])

#Drop the month value from year column
min_temp['Year'] = min_temp['Year'].astype(str).str[:-2].astype(np.int64)

min_temp.dtypes

precip
avg_temp
max_temp
min_temp

# inflation Data Cleaning
# drop the first four rows of the dataset as they are irrelevant to the data values
inflation.drop([0, 1, 2, 3], axis=0, inplace=True)

# Reset the index after dropping the rows
inflation.reset_index(drop=True, inplace=True)

# Rename "United States Inflation, Consumer Prices (Annual %) | Indicator Name: Inflation,
# consumer prices (annual %) | Indicator Code: FP.CPI.TOTL.ZG" AND
# "Unnamed : 1" Columns to "Year" AND "Inflation, Consumer Prices(%)" respectively
inflation.rename(columns={'United States Inflation, Consumer Prices (Annual %) | Indicator Name: Inflation, consumer prices (annual %) | Indicator Code: FP.CPI.TOTL.ZG': 'Year'}, inplace=True)
inflation.rename(
    columns={'Unnamed: 1': 'Inflation, Consumer Prices(%)'}, inplace=True)

# Change Year and Consumer Prices(%) data types to numeric and to float respectively
inflation['Year'] = pd.to_numeric(inflation['Year'])
inflation['Inflation, Consumer Prices(%)'] = inflation['Inflation, Consumer Prices(%)'].astype(
    float)

inflation.dtypes
inflation


# Food Production Cleaning 
# Filter dataset to just include 'Year Code', 'Element', 'Unit', 'Value'
# Filter rows to only show production totals (eliminate  Yield and Area harvested)
production = production.loc[production['Element'] == 'Production']
production = production[['Year','Value']] 
production.reset_index(drop=True, inplace=True)


#--------------------------Merging----------------------------
#merge the NOAA datasets
combined_data = precip.merge(avg_temp, how = 'left', on = 'Year')
combined_data = combined_data.merge(max_temp, how = 'left', on = 'Year')
combined_data = combined_data.merge(min_temp, how = 'left', on = 'Year')

#Start the Year at 1961 to ensure that the data will start in the same year after merging the #NOAA data with other datasets. (This is part of the data cleaning process)

combined_data = combined_data[combined_data.Year > 1960]

#merge Food Production into combined_data
combined_data= combined_data.merge(production, how = 'left', on = 'Year')
combined_data

# Merge inflation into combined_data
combined_data= combined_data.merge(inflation, how = 'left', on = 'Year')

#Export the merged dataframe to csv file to import into Tableau
combined_data.to_csv(path_out + file_out_1, index=False)





