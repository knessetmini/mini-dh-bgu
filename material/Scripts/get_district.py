from selenium import webdriver
import xlrd
#import pandas
import pandas
import math
url='https://www.google.com/maps/place/Kiryat+Ono/@32.0518032,34.8391313,14z/data=!3m1!4b1!4m5!3m4!1s0x151d4a79a53c296d:0x9c1594841c109c08!8m2!3d32.054863!4d34.858858'
url='https://www.google.com/maps/place/'+'עומר'
url='https://www.google.com/maps/place/'
#browser.maximize_window() 
#browser.implicitly_wait(20) 
#browser.get(url)


#browser.find_element_by_id('searchbox-searchbutton').click()

#username = browser.find_element_by_class_name("section-facts-description-text")
#print (username.text)


xls = pandas.ExcelFile('/Users/Timna/Downloads/last_knesset.xls')

sheetX = xls.parse() #2 is the sheet number

var1 = sheetX['address']
var2 = sheetX['Column']

text = ["" for x in range(120)]
browser = webdriver.Chrome(executable_path='/Users/Timna/Downloads/chromedriver')

text={}
for x in range(2, 120):
	print(var1[x]) #1 is the row number...
	if isinstance(var1[x], str):
		browser = webdriver.Chrome(executable_path='/Users/Timna/Downloads/chromedriver')

		browser.maximize_window() 
		browser.implicitly_wait(20) 
		browser.get(url+var1[x])

		browser.find_element_by_id('searchbox-searchbutton').click()
		username = browser.find_element_by_class_name("section-facts-description-text")
		browser.implicitly_wait(20) 
		#text[x]= username.text
		text.update({var2[x]: {"place": username.text}})

		print (username.text)
		browser.quit()



print(text)
df = pandas.DataFrame(text).T
df.to_excel('/Users/Timna/Downloads/file.xls')


