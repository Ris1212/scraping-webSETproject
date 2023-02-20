import pandas as pd
from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.set.or.th/th/market/product/stock/quote/AMANAH/financial-statement/company-highlights?fbclid=IwAR2xGdoXBNvn0sq7GTzGhlAdD2kuMZIxMgawclZRKTYiXazctbgveOWeiLs')
data = driver.page_source

data_df=pd.read_html(data)[1]
data_df.to_html('1.html', index=False)

data_df=pd.read_html(data)[0]
data_df.to_html('2.html', index=False)


