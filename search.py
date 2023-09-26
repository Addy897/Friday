import requests
from bs4 import BeautifulSoup
class Search:
	def search(self,textToSearch):
		
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		url = "https://www.google.com/search?q="+textToSearch 
		response = requests.get(url,headers=headers).content
		soup=BeautifulSoup(response,"html5lib")
		div=soup.find_all("div",attrs={"class":"BNeawe s3v9rd AP7Wnd"})
		for i in div:	
			if("..." not in i.text):
				result=i.text
				break
		return result
			


	
