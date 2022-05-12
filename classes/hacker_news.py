from bs4 import BeautifulSoup
import requests



pages = 1

res = requests.get(f'https://news.ycombinator.com/news?p={pages}')
soup_obj = BeautifulSoup(res.text, 'html.parser') # tell it that it is html that neets to be parser
links = soup_obj.select('.titlelink')
subtext = soup_obj.select('.subtext')

def create_custom_hn(links):
    hacker_news = []
    global subtext
    for idx, item in enumerate(links):
        title = links[idx].getText() # get the titles
        href = links[idx].get('href', None) # if there are no href, default values
        vote = subtext[idx].select('.score')
        if len(vote):
            point = int(vote[0].getText().replace(' points', ''))
            if point > 100:
                hacker_news.append({'title': title, 'link': href, 'votes': point})
    
    return sorted(hacker_news, key= lambda k:k['votes'], reverse=True) # sort it by the votes keyword


for x in create_custom_hn(links):
    if 'https' not in x['link']:
        x['link'] = 'https://news.ycombinator.com/' + x['link']
    print(f"{x['title']} \nvotes: {x['votes']}\n{x['link']}")
    print()
pages += 1