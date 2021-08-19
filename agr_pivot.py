import pandas as pd
import numpy as np

# load data
#agri=pd.read_csv(r'C:/Users/minhu/Desktop/rice/API_AG.LND.AGRI.ZS_DS2_en_csv_v2_2711690.csv',encoding='utf-8')
agri=pd.read_excel(r'C:/Users/minhu/Desktop/rice/API_AG.LND.AGRI.ZS_DS2_en_csv_v2_2711690.xlsx',encoding='utf-8')



def per_p(agri):
	agri=agri[~(agri['Country Name'].str.contains("&"))]
	agri.drop(columns=["Indicator Name","Indicator Code"],inplace=True)
	agri_pivot=[]
	agri=agri.reset_index(drop=True)
	#year=agri.drop(columns=['Country Code','Country Name'])columns.tolist()
	year=["1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
	#agri.fillna(0,inplace=True)
	for ind in range(len(agri)):
		for y in year:
			agri_pivot.append({'country':agri['Country Name'][ind],'country_code':agri['Country Code'][ind],'year':y,'per':str(agri[y][ind])})
			#agri_pivot.append({'country':agri['Country Name'][ind]})
		#if ind==10:break
	
	agri_pivot=pd.DataFrame(agri_pivot)
	#agri_pivot.dropna(inplace=True)
	agri_pivot=agri_pivot[agri_pivot.per!='nan']
	agri_pivot=agri_pivot[agri_pivot.per!='None']
	agri_pivot.per=agri_pivot.per.astype(float)
	ussr=['RUS','UKR','UZB','KAZ','AZE','LTU','LVA','TJK','ARM','TKM','EST','GEO','MDA','KGZ'] # 1961-1991
	yugoslav=['SVK','HRV','MKD','OWID_KOS','XKX','BIH','MNE','SRB'] # 1961-1991
	for y in year:
		temp=agri_pivot[(agri_pivot.year==y) & (agri_pivot.country_code.isin(ussr))]		
		agri_pivot=agri_pivot.append({'country':'USSR','country_code':'228','year':y,'per':sum(temp.per)},ignore_index=True)
		temp=agri_pivot[(agri_pivot.year==y) & (agri_pivot.country_code.isin(yugoslav))]		
		agri_pivot=agri_pivot.append({'country':'Yugoslav','country_code':'248','year':y,'per':sum(temp.per)},ignore_index=True)
		if y=='1991':break
	return agri_pivot
	

def get_output_schema():       
  return pd.DataFrame({
    'country' : prep_string(),
	'country_code': prep_string(),
    'year' : prep_string(),
    'per' : prep_decimal() #prep_string()
})



