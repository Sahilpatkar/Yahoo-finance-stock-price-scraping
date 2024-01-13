from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import bs4
import pandas as pd
import excelLearning
import pandas_datareader as pdr
import datetime 
#stock = input("enter stock id:")


def Market_Cap(stock):
	#r = requests.get("https://finance.yahoo.com/quote/"+stock)
	soup = bs4.BeautifulSoup(r.text,"lxml")

	M_cap = soup.find_all("div",{"class":"D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)"})[0]
	m = M_cap.find_all("span",{"class":"Trsdu(0.3s)"})

	return m[0].text

def PE_Ratio(stock):
	
	soup = bs4.BeautifulSoup(r.text,"lxml")

	M_cap = soup.find_all("div",{"class":"D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)"})[0]
	m = M_cap.find_all("span",{"class":"Trsdu(0.3s)"})

	return m[2].text

def EPS(stock):
	soup = bs4.BeautifulSoup(r.text,"lxml")

	M_cap = soup.find_all("div",{"class":"D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)"})[0]
	m = M_cap.find_all("span",{"class":"Trsdu(0.3s)"})

	return m[3].text

def Price_to_Book_Ratio(stock):
	r = requests.get("https://finance.yahoo.com/quote/"+stock+"/key-statistics?p="+stock)
	soup = bs4.BeautifulSoup(r.text,"lxml")

	BV = soup.find_all("div",{"Fl(start) smartphone_W(100%) W(50%)"})[0]
	m = BV.find_all("td",{"class":"Fw(500) Ta(end) Pstart(10px) Miw(60px)"})

	return m[6].text

def parsePrice(stock):
	#r = requests.get("https://finance.yahoo.com/quote/"+stock)

	soup = bs4.BeautifulSoup(r.text,"lxml")

	price = soup.find_all("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text

	return price

def previous_close(stock):
	#r = requests.get("https://finance.yahoo.com/quote/"+stock)
	soup = bs4.BeautifulSoup(r.text,"lxml")
	prev_close = soup.find_all("div",{"class":"D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)"})[0]
	m = prev_close.find_all("span",{"class":"Trsdu(0.3s)"})
	return m[0].text

def previous_dates(stock,date):
	start = date
	end = date
	df = pdr.get_data_yahoo(stock,start,end)
	return df["Close"].astype(float).values



		

dates = excelLearning.read_cells()

BV_list = []
EPS_list = []
PE_Ratio_list = []
Market_Cap_list = []
stock_list = excelLearning.CodeList()
price_list = []
prev_close_list = []
history = []

# for i in stock_list:
# 	if i == None:
# 		stock_list.pop(stock_list.index(i))






print(stock_list)

history_data_required = input("do u want to scan the Historical data? <y/n> :").lower()
stock_price_close = input("do u want to update current stock and previous close price? <y/n>").lower()

if(history_data_required == "y"):
	for j in dates:

		for i in stock_list:
			if i != None:
				try:

					print(previous_dates(i,j))
					history.append(float(previous_dates(i,j)))
					#excelLearning.write_value(history,"D")
					#print(history)
					
				except:
					if i != None: print("history error:"+i)
					history.append("error")

if(stock_price_close == 'y'):
	
	for i in stock_list:
		if i == None:
			price_list.append("")
			prev_close_list.append("")
			Market_Cap_list.append("")
			PE_Ratio_list.append("")
			EPS_list.append("")

		if i != None:
			r = requests.get("https://finance.yahoo.com/quote/"+i)
			print("--------------------",i,"--------------------")
			try: 
				price = parsePrice(i)
				price = price.replace(',','')
				price_list.append(float(price))
				print("Current Price of "+i+" : "+str(parsePrice(i)))
			except:
				print("[-]Error getting Current Price of "+i)
				price_list.append("error")
			try:
				prev_close = previous_close(i)
				prev_close = prev_close.replace(',','')
				prev_close_list.append(float(prev_close))
				print("Previous Close of "+i+" : "+str(previous_close(i)))
			except:
				print("[-]Error getting Previous Close of "+i)
				prev_close_list.append("error")
			try:
				m_cap = Market_Cap(i)
				m_cap = m_cap.replace(',','')
				Market_Cap_list.append(m_cap)
				print("Market Cap of "+i+" : "+str(Market_Cap(i)))
			except:
				print("[-]Error getting Market Cap of "+i)
				Market_Cap_list.append("error")

			try:
				pe_ratio = PE_Ratio(i)
				PE_Ratio_list.append(float(pe_ratio))
				print("P/E of "+i+" : "+str(PE_Ratio(i)))
			except:
				print("[-]Error getting P/E of "+i)
				PE_Ratio_list.append("error")

			try:
				eps = EPS(i)
				EPS_list.append(float(eps))
				print("ESP of "+i+" : "+str(EPS(i)))
			except:
				print("[-]Error getting EPS of "+i)
				EPS_list.append("error")

			try:
				BV = Price_to_Book_Ratio(i)
				BV_list.append(float(BV))
				print("BV of "+i+" : "+str(Price_to_Book_Ratio(i)))
			except:
				print("[-]Error getting BV of "+i)
				BV_list.append("error")

		# BV = Price_to_Book_Ratio(i)
		# print("BV of "+i+" : "+str(Price_to_Book_Ratio(i)))
	

	#print("the current price of "+i+" is "+str(parsePrice(i))+" and Previous Close is "+str(previous_close(i)))
if(stock_price_close == 'y'):
	excelLearning.write_value(price_list,"K")
	excelLearning.write_value(prev_close_list,"J")
	excelLearning.write_value(Market_Cap_list,"O")
	excelLearning.write_value(PE_Ratio_list,"P")
	excelLearning.write_value(EPS_list,"Q")
	excelLearning.write_value(BV_list,"R")
if(history_data_required == "y"):
	excelLearning.write(history)

excelLearning.save_file()