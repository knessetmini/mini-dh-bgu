import http.cookiejar, urllib.request, pandas, datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen


data={}

def get_info(soup,place):
	id="ctl00_ctl42_g_4e85a275_d641_41ab_8bc5_98c140927f3d_"+place
	born = soup.find('span', id=id)
	if born is not None:
		born=born.text
	return born

def get_all_details(soup,memberID):
    birthYear = soup.find('span', id="ctl00_ctl42_g_4e85a275_d641_41ab_8bc5_98c140927f3d_BirthDateSpn")
    data.update({memberID: {"birthYear": birthYear}})
    print(data)


def open_link(link):
	r = opener.open(link)
	content = r.read()
	return BeautifulSoup(content, "lxml")

def print_data():
 for x in data:
    print (x)
    for y in data[x]:
        print (y,':',data[x][y])


counter=0
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("https://www.knesset.gov.il/mk/heb/mkindex_current.asp")
r = opener.open("https://www.knesset.gov.il/mk/heb/mkindex_current.asp")
content = r.read()
soup= BeautifulSoup(content, "lxml")

for a in soup.findAll("a", { "class" : "DataText" }):
	memberID=a.get('href').split('=')[1]
	link='http://main.knesset.gov.il/mk/pages/MkPersonalDetails.aspx?MKID='+memberID
	soup=open_link(link)
	get_all_details(soup,memberID)
	counter=counter+1


df = pandas.DataFrame(data).T
df.to_excel('file.xls')



print(counter)













