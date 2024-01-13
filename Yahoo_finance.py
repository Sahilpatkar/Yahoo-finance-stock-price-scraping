import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import xlwt

stock_ID = input('stock_ID')
download_source = (r'C:\Users\sahil\Downloads\Yahoo.xlsx')

start = dt.datetime(2000,1,1)
end = dt.datetime.today()

df = pdr.get_data_yahoo(stock_ID,start,end)

print(df.head())

df.head().to_excel(download_source)