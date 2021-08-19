import pandas as pd
#df=pd.read_csv('tas_1901_2020.csv')
#print(len(df))
def temperature(df):
	#print(df.columns)
	df_copy=df.copy()
	#df_copy.columns=['Temperature - (Celsius)','Year','Statistics','Country','ISO3']
	print(type(df_copy.Year[0]))
	s=set(df_copy['Statistics'])
	year=[1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991]
	ussr=['RUS','UKR','UZB','KAZ','AZE','LTU','LVA','TJK','ARM','TKM','EST','GEO','MDA','KGZ'] # 1961-1991
	yugoslav=['SVK','HRV','MKD','OWID_KOS','XKX','BIH','MNE','SRB'] # 1961-1991
	df_temp=[]
	print(df_copy['ISO3'][0])
	for y in year:
		#print(y)
		for m in s:
			#print(m)
			temp=df_copy[(df_copy['Statistics']==m) & (df_copy['Year']==y)]
			print(temp)
			t=temp[temp['ISO3'].isin(ussr)]  
			
			print(len(t))
			if len(t)>0:df_temp.append({'Temperature - (Celsius)':sum(t['Temperature - (Celsius)'])/len(t),'Year':y,'Statistics':m,'Country':'USSR','ISO3':'228'})
			t=temp[temp['ISO3'].isin(yugoslav)]
			if len(t)>0:df_temp.append({'Temperature - (Celsius)':sum(t['Temperature - (Celsius)'])/len(t),'Year':y,'Statistics':m,'Country':'Yugoslav','ISO3':'248'})
			
		
	print(len(df_temp))
	df_copy=pd.concat([df_copy,pd.DataFrame(df_temp)],axis=0)
	return df_copy
			
#print(len(temperature(df))	)		
			
			
			
def get_output_schema():       
  return pd.DataFrame({
	'Temperature - (Celsius)':prep_decimal(),
	'Year':prep_int(),
	'Statistics':prep_string(),
	'Country':prep_string(),
	'ISO3':prep_string()
})			