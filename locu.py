import json
from urllib.parse import urlencode
import requests
import pprint


api_key='655ac4f76ad469745276f2e67144dd45a5a644a9'

def search(query):
	search_key=api_key
	url="https://api.locu.com/v1_0/venue/search/?region=" + query + '&'
	main_url=url + urlencode({"api_key":search_key})
	response=requests.get(main_url)

	jsonobj=response.json()
	for item in jsonobj['objects']:
		print(item['name'])
		print(item['phone'])
		print(" ")


def main():
	keyword=input("Enter the query:")
	search(keyword)

if __name__ == '__main__':
	main()




