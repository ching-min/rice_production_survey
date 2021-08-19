import pandas as pd
#df=pd.read_csv('average-monthly-precipitation.csv')
#print(len(df))
def rain(df):
	#print(df.columns)
	df_copy=df.copy()
	#df_copy.columns=['Entity','Code','Year','Average monthly precipitation']
	print(type(df_copy.Year[0]))
	year=[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991]
	ussr=['RUS','UKR','UZB','KAZ','AZE','LTU','LVA','TJK','ARM','TKM','EST','GEO','MDA','KGZ'] # 1961-1991
	yugoslav=['SVK','HRV','MKD','OWID_KOS','XKX','BIH','MNE','SRB'] # 1961-1991
	df_temp=[]
	for y in year:
		temp=df_copy[(df_copy['Year']==y)]
		print(temp)
		t=temp[temp['Code'].isin(ussr)]  
		
		print(len(t))
		if len(t)>0:df_temp.append({'Entity':'USSR','Code':'228','Year':y,'Average monthly precipitation':sum(t['Average monthly precipitation'])/len(t)})
		t=temp[temp['Code'].isin(yugoslav)]
		if len(t)>0:df_temp.append({'Entity':'Yugoslav','Code':'248','Year':y,'Average monthly precipitation':sum(t['Average monthly precipitation'])/len(t)})
			
		
	print(len(df_temp))
	df_copy=pd.concat([df_copy,pd.DataFrame(df_temp)],axis=0)
	return df_copy
			
#print(len(temperature(df))	)		
			
			
			
def get_output_schema():       
  return pd.DataFrame({
	'Entity':prep_string(),
	'Code':prep_string(),
	'Year':prep_int(),
	'Average monthly precipitation':prep_decimal()
})			