import pandas as pd
import numpy as np

def get_output_schema():       
  return pd.DataFrame({
    'Area' : prep_string(),
	'Area_Code':prep_string(),
    'Unit' : prep_string(),
    'Year' : prep_int(),
	'Flag Description': prep_string(),
	'Value': prep_decimal()
})

def rice_selection(df):
	country=set(df.Area)
	year=set(df.Year)
	data=[]
	for c in country:
		temp=df[(df.Area==c) ]
		
		for y in year:
			temp_y=temp[(temp.Year==y)  ]
			data_type=set(temp_y['Flag Description'])
			if len(temp_y)==1:
				data.append({'Area':c,'Area_Code':temp_y['Area Code (ISO3)'].iloc[0],'Unit':'tonnes','Year':y,'Flag Description':temp_y['Flag Description'].iloc[0],'Value':temp_y.Value.iloc[0]})
			elif len(temp_y)==0:
				continue
			elif 'Official data' in data_type:
				data.append({'Area':c,'Area_Code':temp_y['Area Code (ISO3)'].iloc[0],'Unit':'tonnes','Year':y,'Flag Description':'Official data','Value':temp_y[temp_y['Flag Description']=='Official data'].Value.iloc[0]})
			elif 'Calculated data' in data_type:
				data.append({'Area':c,'Area_Code':temp_y['Area Code (ISO3)'].iloc[0],'Unit':'tonnes','Year':y,'Flag Description':'Calculated data','Value':temp_y[temp_y['Flag Description']=='Calculated data'].Value.iloc[0]})
			elif 'Aggregate, may include official, semi-official, estimated or calculated data' in data_type:
				data.append({'Area':c,'Area_Code':temp_y['Area Code (ISO3)'].iloc[0],'Unit':'tonnes','Year':y,'Flag Description':'Aggregate, may include official, semi-official, estimated or calculated data','Value':temp_y[temp_y['Flag Description']=='Aggregate, may include official, semi-official, estimated or calculated data'].Value.iloc[0]})
			elif 'Unofficial figure' in data_type:
				data.append({'Area':c,'Area_Code':temp_y['Area Code (ISO3)'].iloc[0],'Unit':'tonnes','Year':y,'Flag Description':'Unofficial figure','Value':temp_y[temp_y['Flag Description']=='Unofficial figure'].Value.iloc[0]})
			elif 'FAO data based on imputation methodology' in data_type:
				data.append({'Area':c,'Area_Code':temp_y['Area Code (ISO3)'].iloc[0],'Unit':'tonnes','Year':y,'Flag Description':'FAO data based on imputation methodology','Value':temp_y[temp_y['Flag Description']=='FAO data based on imputation methodology'].Value.iloc[0]})
			elif 'FAO estimate' in data_type:
				data.append({'Area':c,'Area_Code':temp_y['Area Code (ISO3)'].iloc[0],'Unit':'tonnes','Year':y,'Flag Description':'FAO estimate','Value':temp_y[temp_y['Flag Description']=='FAO estimate'].Value.iloc[0]})
			else:
				data.append({'Area':c,'Area_Code':temp_y['Area Code (ISO3)'].iloc[0],'Unit':'tonnes','Year':y,'Flag Description':'Data not available','Value':temp_y[temp_y['Flag Description']=='Data not available'].Value.iloc[0]})
	for i in range(len(data)): # former sdn
		if data[i]['Area']=='Sudan (former)': data[i]['Area_Code']='SDN'
	#yugoslav=[]
	#ussf=[]
	return pd.DataFrame(data)
			
				