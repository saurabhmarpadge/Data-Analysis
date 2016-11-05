import requests
from bs4 import BeautifulSoup

def elements():
	response = requests.get("http://archive.ics.uci.edu/ml/datasets.html")
	soup = BeautifulSoup(response.content, 'html.parser')
	anchors = soup.find_all('a')
	arr = []
	for link in anchors[44:-5:2][1:]:
		arr.append(["http://archive.ics.uci.edu/ml/"+link.get('href'), link.get_text(), "test"])
	return arr