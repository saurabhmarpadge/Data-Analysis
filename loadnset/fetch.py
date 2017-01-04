import requests
from bs4 import BeautifulSoup

def elements():
	response = requests.get("http://archive.ics.uci.edu/ml/datasets.html")
	soup = BeautifulSoup(response.content, 'html.parser')
	megatag = soup.find_all('td')
	content_arr = megatag[18].find_all('td') 
	arr, indexer = [], 11 #{link product description}
	for val in range(11, len(content_arr)-1) :
		setter = []

	return arr