import pandas as pd
import numpy as np

# load data
#land=pd.read_csv(r'C:/Users/minhu/Desktop/rice/API_AG.LND.TOTL.K2_DS2_en_csv_v2_2708609.csv',encoding='utf-8')



def land_p(land):
	land=land[~(land['Country Name'].str.contains("&"))]
	land.drop(columns=["Indicator Name","Indicator Code"],inplace=True)
	land_pivot=[]
	land=land.reset_index(drop=True)
	year=land.columns.tolist()[2:]
	year=["1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
	
	for ind in range(len(land)):
		for y in year:
			land_pivot.append({'country':land['Country Name'][ind],'country_code':land['Country Code'][ind],'year':y,'land':str(land[y][ind])})
			
	land_pivot=pd.DataFrame(land_pivot)
	land_pivot=land_pivot[land_pivot.land!='nan']
	land_pivot=land_pivot[land_pivot.land!='None']
	land_pivot.land=land_pivot.land.astype(float)
	ussr=['RUS','UKR','UZB','KAZ','AZE','LTU','LVA','TJK','ARM','TKM','EST','GEO','MDA','KGZ'] # 1961-1991
	yugoslav=['SVK','HRV','MKD','OWID_KOS','XKX','BIH','MNE','SRB'] # 1961-1991
	for y in year:
		temp=land_pivot[(land_pivot.year==y) & (land_pivot.country_code.isin(ussr))]		
		land_pivot=land_pivot.append({'country':'USSR','country_code':'228','year':y,'land':sum(temp.land)},ignore_index=True)
		temp=land_pivot[(land_pivot.year==y) & (land_pivot.country_code.isin(yugoslav))]		
		land_pivot=land_pivot.append({'country':'Yugoslav','country_code':'248','year':y,'land':sum(temp.land)},ignore_index=True)
		if y=='1991':break
	return land_pivot

def get_output_schema():       
  return pd.DataFrame({
    'country' : prep_string(),
	'country_code' : prep_string(),
    'year' : prep_string(),
    'land' : prep_decimal()#prep_decimal()
})



