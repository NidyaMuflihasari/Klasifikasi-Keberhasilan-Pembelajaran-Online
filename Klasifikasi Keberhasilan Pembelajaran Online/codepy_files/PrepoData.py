import pandas as pd 
import numpy as np 

class data_:
	def read_file(self,filepath):
		return pd.read_excel(str(filepath))

	def get_column_list(self,df):

		column_list=[]

		for i in df.columns:
			column_list.append(i)
		return column_list

	def get_shape(self,df):
		return df.shape 

	def drop_columns(self,df,column):
		return df.drop(column,axis=1)

	