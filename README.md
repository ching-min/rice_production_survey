# rice_production_survey

In this project, I want to analyze the factors of rice production quantity with mean monthly temperature, mean precipitation, and agriculture land size by data visualization.

tool: Tableau Desktop, Tableau Prep, Python

Data
1.	rice annual production from 1961 to 2019. 
Source: http://www.fao.org/faostat/en/#data/QCL
columns:
●	Domain Code:	string, code of domain.
●	Domain: string, category of data, in this project, only “Crops and livestock products”.
●	Area Code (ISO3): string, country code in ISO3.	
●	Area: string, country name.
●	Element Code: int, code of element.
●	Element: string, subcategory of item, in this project, only “Production” 
●	Item Code (FAO): int, code of item.
●	Item: string, the item which want to search, in this project, only “Rice, paddy”.
●	Year Code: int, the year of statistical figures.
●	Year: int, same as “Year Code”.
●	Unit: string, the unit of “Value”. In this project, only “tones”.
●	Value: float, the number of items.
●	Flag: string, code of “Flag Description”.
●	Flag Description: string, source of statistic figure.
2.	Mean monthly temperature from 1901 to 2020.
Source: https://climateknowledgeportal.worldbank.org/download-data
columns:
●	Temperature - (Celsius): float, mean monthly temperature in each month and year (Celsius).
●	Year: int, the year of statistical figures.
●	Statistics: float, the month of statistical figures.
●	Country: string, country name.
●	ISO3: string, country code in ISO3.
3.	Average precipitation in depth (mm per year) from 1900 to 2014.
Source: https://data.worldbank.org/indicator/AG.LND.PRCP.MM?most_recent_year_desc=false
columns: 
●	Entity: string, country name.
●	Code: string, country code in ISO3.
●	Year: int, the year of statistical figures.
●	Average monthly precipitation: float, average precipitation (mm).
4.	Agriculture land from 1961 to 2018
source: https://data.worldbank.org/indicator/AG.LND.AGRI.ZS
columns: 
●	Country Name:  string, country name.
●	Country Code: string, country code in ISO3.
●	Indicator Name: string, data category, in this data, only “Agricultural land (% of land area)”.
●	Indicator Code: string, code of “Indicator Name”.
●	1960 - 2020: float, total 61 columns, the column names are represented as years, the data in it is the percentage of agricultural land of the whole country land. 
5.	Land Area from 1961 to 2018
source: https://data.worldbank.org/indicator/AG.LND.TOTL.K2?most_recent_value_desc=true
columns: 
●	Country Name:  string, country name.
●	Country Code: string, country code in ISO3.
●	Indicator Name: string, data category, in this data, only “Land area (sq. km)”.
●	Indicator Code: string, code of “Indicator Name”.
●	1960 - 2020: float, total 61 columns, the column names are represented as years, the data in it is the area of country land (sq km). 
