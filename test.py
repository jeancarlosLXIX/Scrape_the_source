from hashlib import algorithms_available
from urllib import response
import requests
import json
response = requests.get('https://dzone.com/services/widget/article-listV2/list?page=1&sort=newest').text

articles = json.loads(response)["result"]["data"]['nodes']

for article in articles:
    print(article["title"])