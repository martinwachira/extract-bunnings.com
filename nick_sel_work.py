# A small python script to scrap products data from a website
# Author: Martin Wachira, martinnwachira@gmail.com
# Import the required libraries to run this script on your machine
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

browser = webdriver.Firefox()
#browser = webdriver.Chrome()
#browser = webdriver.PhantomJS()
try:
	browser.get("https://www.bunnings.com.au/search/products?facets=CategoryIdPath%3D2a021706-07d5-4648-bf26-2ea8fea049df%20%3E%206ef144fa-daa0-4ac6-9558-56e4480742ea%20%3E%204d53fb34-dc69-457b-8577-2d9d647206f4%20%3E%20f5b31f93-dfa4-4123-bb50-0d2b19495bfe&redirectFrom=Diy#")
except Exception as e:
	print("Error: ",str(e))
sleep(3)

#clicking on the button after loading the page for the first time (View next 48 Products)
try:
	browser.find_element_by_xpath("/html/body/form/div[7]/div/div[2]/div[3]/div/div/section/div[3]/div/div[2]/a/span/span").click()
except Exception as e:
	print("Error: ",str(e))
sleep(6)

#clicking on the button for the second time (View next 11 Products)
try:
	browser.find_element_by_xpath("/html/body/form/div[7]/div/div[2]/div[3]/div/div/section/div[3]/div/div[2]/a/span/span").click()
except Exception as e:
	print("Error: ",str(e))
sleep(8)

try:
	html = browser.page_source
except Exception as e:
	print("Error: ",str(e))

soup = BeautifulSoup(html,"lxml")
names =  soup.findAll('div',{'class':"product-list__prodname product-list__title fn"})
name_list = []
for name in names:
	name_list.append(name.text)

prices = soup.findAll('div',{'class':"price-value"})
price_list = []
for price in prices:
	price_list.append(price.text)


names_and_prices = list(zip(name_list,price_list))


df = pd.DataFrame(names_and_prices)
#Give a column names
df.columns = ['Product Name', 'Product Price']

# Saving data into csv
# Generate filename based on current timestamp
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time_now = time_now.replace(':','-')
time_now = time_now.replace(' ','_')
df.to_csv("product items at "+time_now+".csv", index=False)

#quiting the browser
browser.quit()

this is macro recording testthis is macro recording testthis is macro recording testthis is macro recording test
