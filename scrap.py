import requests
from bs4 import BeautifulSoup
import lxml
import json
from datetime import datetime


def sports_rss():
    article_list = []
    try:
        print('Starting scraping of Sports')
        r = requests.get('https://www.sports.ru/figure-skating/')
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all('p')
        for a in articles:
            if (a.find('span', class_='date') is not None and a.find('a', class_='short-text', href=True) is not None):
                title = a.find('a', class_='short-text', href=True).text
                link = a.find('a', class_='short-text', href=True)
                if "figure-skating" in link.get('href'):
                    published_wrong_1 = datetime.date(datetime.now())
                    published_wrong_2 = a.find('span', class_='date').text
                    published_wrong = str(published_wrong_1) + \
                        " " + str(published_wrong_2)
                    published = datetime.strptime(
                        published_wrong, '%Y-%m-%d %H:%M')

                    if link.get('href').startswith("https://www.sports.ru/"):
                        new_link = link.get('href')
                    else:
                        new_link = "https://www.sports.ru/" + link.get('href')

                    article = {
                        'title': title,
                        'link': new_link,
                        'published': published,
                        'source': 'sports'
                    }

                    article_list.append(article)
        #for i in article_list:
        #    print(i)
        print('Finished scraping the article')
        return article_list[:4]
    except Exception as e:
        print('The scraping job failed. See exception: ', "SPORTS")
        print(e)



def hackernews_rss():
    article_list = []

    try:
        print('Starting the scraping tool hacks')
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(r.content, features='xml')

        # select only the "items" I want from the data
        articles = soup.findAll('item')

        # for each "item" I want, parse it into a list
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published_wrong = a.find('pubDate').text
            published = datetime.strptime(
                published_wrong, '%a, %d %b %Y %H:%M:%S %z')
            # print(published, published_wrong) # checking correct date format

            # create an "article" object with the data
            # from each "item"
            article = {
                'title': title,
                'link': link,
                'published': published,
                'source': 'HackerNews RSS'
            }

            # append my "article_list" with each "article" object
            article_list.append(article)

        print('Finished scraping the articles')
        # after the loop, dump my saved objects into a .txt file
        return article_list[:4]
    except Exception as e:
        print('The scraping job failed. See exception: ', "HACKS")
        print(e)



def games_rss():
    article_list = []

    try:
        print('Starting the scraping tool games')
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://ru.ign.com/')
        soup = BeautifulSoup(r.content, features='xml')

        # select only the "items" I want from the data
        articles = soup.find_all('div', class_='m')

        # for each "item" I want, parse it into a list
        for a in articles:
            if (a.find('h3') is not None and a.find('a').get('href') is not None):
                title = a.find('h3').text
                link = a.find('a').get('href')
                published3 = a.find('time').get('datetime')
                published2 = published3.replace('T', ' ')
                published1 = published2.replace('+03:00', '')
                published = datetime.strptime(published1, '%Y-%m-%d %H:%M:%S')
                article = {
                    'title': title,
                    'link': link,
                    'published': published,
                    'source': "Games"
                }

                # append my "article_list" with each "article" object
                article_list.append(article)
        # print(article_list)

        print('Finished scraping the articles')
        # after the loop, dump my saved objects into a .txt file
        return article_list[:4]
    except Exception as e:
        print('The scraping job failed {}. See exception: ', "GAMES")
        print(e)



def movies_rss():
    article_list = []

    try:
        print('Starting the scraping tool movies')
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://www.kinoafisha.info/news/')
        soup = BeautifulSoup(r.content, features='html.parser')

        # select only the "items" I want from the data
        articles = soup.find_all('div', class_='newsV2_item')

        # for each "item" I want, parse it into a list
        for a in articles:
            if (a.find('span', class_='newsV2_date') is not None and a.find('a').get('href') is not None and a.find('span', class_='newsV2_date') is not None):
                title = a.find('img', class_='picture_image').get('alt')
                link = a.find('a').get('href')
                published_wrong1 = a.find('span', class_='newsV2_date').text
                months = {
                    'октября': 10,
                    'ноября': 11
                }
                #print(published_wrong1)
                for key in months:
                    if key in published_wrong1:
                        published_wrong = published_wrong1.replace(
                            key, str(months[key]))

                published = datetime.strptime(published_wrong, '%d %m %Y %H:%M')
                article = {
                    'title': title,
                    'link': link,
                    'published': published,
                    'source': "Movies"
                }

                # append my "article_list" with each "article" object
                article_list.append(article)

        print('Finished scraping the articles')
        # after the loop, dump my saved objects into a .txt file
        return article_list[:4]
    except Exception as e:
        print('The scraping job failed. See exception:', "MOVIES")
        print(e)

#example = sports_rss()
#example = games_rss()
#example = hackernews_rss()
#example = movies_rss()

#answer = ""
#for i in example:
#    answer += i.get('title') + '\n' + i.get('link') + '\n' + '\n'


#answer = example.get('title') + '\n'

#print(answer)

