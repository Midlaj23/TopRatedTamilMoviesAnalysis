from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup
import json

def SoupFunction(url):
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
    html = request.urlopen(request_site).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def allLinks():
    urls = []
    soup = SoupFunction('https://www.imdb.com/india/top-rated-tamil-movies/')
    for i in soup.findAll('a'):
        links = i.get('href')
        urls.append(links)
    urls = ['https://www.imdb.com' + i.strip() for i in urls if i is not None and i.startswith('/title/tt')]

    return urls


def movieInfo():
    urls = allLinks()
    data = []
    for i in urls[:2]:
        soup = SoupFunction(i)

        title = soup.find("div", {'class': "sc-69e49b85-0 jqlHBQ"}).find("span").text
        rating = soup.find("div", {"class": "sc-bde20123-2 cdQqzc"}).find("span").text
        img = soup.find("meta",property="og:image")['content']
        genre = soup.find("div", {"class": "ipc-chip-list__scroller"}).find("span").text
        director = soup.find("div", {'class': "ipc-metadata-list-item__content-container"}).find("a").text
        duration = soup.find('div',{'class':'ipc-html-content-inner-div'}).text

        myData = {
            "Name": title,
            "Director": director,
            "Genre": genre,
            "Rating": rating,
            'Minimal': img,
            'Duration':duration

        }
        data.append(myData)
    print(data)
d = movieInfo()

#     jsonfile = open("tamil_movies.json","w")
#     json.dump(data,jsonfile)
# if __name__ == "__main__":
#          movieInfo()












