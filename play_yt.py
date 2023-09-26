import requests
import re
import json ,subprocess


def play(textToSearch):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	url = "https://www.youtube.com/results?search_query="+textToSearch 
	data=requests.get(url,headers=headers)
	reg=re.findall("(?:ytInitialData = )(\{.*\})(?:\;\</script)",data.text)
	ytInitial=json.loads(reg[0])
	contetns=ytInitial.get("contents",{}).get("twoColumnSearchResultsRenderer",{}).get("primaryContents",{}).get("sectionListRenderer",{}).get("contents",0)
	videos=[]
	titles=[]
	for i in contetns:
		contents2=i.get("itemSectionRenderer",{}).get("contents",[])
		for j in contents2:
			vId=j.get("videoRenderer",{}).get("videoId")
			title=j.get("videoRenderer",{}).get("title",{}).get("runs",[{}])[0].get("text",0)
			videos.append(vId)
			titles.append(title)
	nurl="https://www.youtube.com/watch?v="+videos[0]
	print(f"Playing {titles[0]}")
	subprocess.check_output("start "+nurl,shell=True,stderr=subprocess.STDOUT)


if __name__ == '__main__':
	while True:
		try:
			q=input("Enter Song name to play: ")
			if(q != "q"):
				play(q)
			
			else:
			
				exit()	
		except KeyboardInterrupt:	
				exit()
