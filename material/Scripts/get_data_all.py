import http.cookiejar, urllib.request, pandas, datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen


data={}
def get_name(soup,title):
	name=""
	if title is not None:
		if len(title.text.split("הכנסת"))>=2:
			name=title.text.split("הכנסת")[1]
		else:
			name=title.text
	return name

def get_info_by_id(soup, memberID):
	if soup.find("p",{"id": "ctl00_PlaceHolderMain_dcpDesktop_ctl00_mkKnessetList"})is None:
		id="ctl00_ctl42_g_9fdc5a4a_058e_4885_9afc_ce66cdfb5602_"
		type1="true"
	else:
		id="ctl00_ctl42_g_4e85a275_d641_41ab_8bc5_98c140927f3d_"
		type1="false"

	print(type1)

	if type1=="true" :
		title = soup.find("h2", {"class" : "BreadcrumbPageTitle"})

	else:
		title = soup.find("h3", {"class" : "BreadcrumbPageTitle"})

	name=get_name(soup,title)
	birth=soup.find("span", {"id" : id + "BirthDateSpn"})
	if birth is None:
		birth=soup.find("span", {"id" : id + "BirthDateSpn2"})
	if birth is None:
		date=""
	else:
		date=birth.text
	print(date)

	placeBirth=soup.find("span", {"id" : id + "countrySpn"})
	if placeBirth is None:
		placeBirth=soup.find("span", {"id" : id + "countrySpn2"})
	if placeBirth is None:
		place=""
	else:
		place=placeBirth.text
	print(place)
	data.update({ memberID: {"name": name, "birthDate": date, "birthPlace": place}})


def open_link(link):
	r = opener.open(link)
	content = r.read()
	return BeautifulSoup(content, "lxml")


counter=0
url="http://main.knesset.gov.il/mk/all/Pages/default.aspx"
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(url)
soup=open_link(url)
for memberID in range(1,964):
		link='http://main.knesset.gov.il/mk/pages/MkPersonalDetails.aspx?MKID='+str(memberID)
		soup=open_link(link)
		get_info_by_id(soup, memberID)
		counter=counter+1



df = pandas.DataFrame(data).T
df.to_excel('file.xls')



print(counter)













