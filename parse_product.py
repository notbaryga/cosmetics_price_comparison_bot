import requests
from product import Product
from url import Url
from bs4 import BeautifulSoup as bs
import json

# TODO: Отслеживать наличие товара, добавить сохранение картинки и описания, возможно парсить отзывы


class Parser:
    def __init__(self, query: str):
        self.query = query.split()
        self.product = Product(query)
        self.ga_url = Url.get_ga_search_url(self.query)
        self.letual_url = Url.get_letual_search_url(self.query)
        self.rivgauche_url = Url.get_rivgauche_search_url(self.query)
        self.irecommend_url = Url.get_irecommend_search_url(self.query)

    def parse_ga(self):
        response = requests.get(self.ga_url, )
        soup = bs(response.text, 'html.parser')
        try:
            price = soup.find('span', attrs={'class': 'price'}).text.replace('\xa0', '').replace('₽', '')
            url = soup.find('a', attrs={'class': 'product-item-link'})['href']

            if self.product.get_product_photo() is None:
                photo_link = soup.find('img', attrs={'class': 'product-item-photo__img'})['data-src']
                self.product.add_product_photo(photo_link)

            self.product.add_product_data('Золотое яблоко', price, url)
        except:
            ...

    def parse_letual(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/111.0.0.0 Safari/537.36',
            'accept': 'application/json, text/plain, */*'
        }
        response = requests.get(self.letual_url, headers=headers).text
        data = json.loads(response)

        try:
            price = data['contents'][0]['mainContent'][2]['records'][0]['attributes']['priceWithoutCoupons']
            product_id = data['contents'][0]['mainContent'][2]['records'][0]['attributes']['product.repositoryId'][0]
            url = Url.get_letual_product_url(product_id)

            if self.product.get_product_photo() is None:
                photo_link = data['contents'][0]['mainContent'][2]['records'][0]['attributes']['product.largeImage.url.storeSiteRU'][0]
                self.product.add_product_photo(Url.get_letual_product_photo(photo_link))

            self.product.add_product_data('Летуаль', price, url)
        except:
            ...

    def parse_rivgauche(self):
        response = requests.get(self.rivgauche_url)
        soup = bs(response.text, 'html.parser')

        try:
            price = soup.find('div', attrs={'class': 'from-price'}).text.replace('от ', '').replace(' ₽', '').replace(
                '\xa0', '')
            end_url = soup.find('a', attrs={'class': 'media'})['href']
            url = Url.get_rivgauche_product_url(end_url)

            self.product.add_product_data('Рив Гош', price, url)
        except:
            ...

    def parse_irecommend(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/111.0.0.0 Safari/537.36',
            'accept': 'application/json, text/plain, */*'
        }
        response = requests.get(self.irecommend_url, headers=headers)
        soup = bs(response.text, 'html.parser')

        try:
            link = Url.get_irecommend_product_url(soup.find(class_ = 'ProductTizer').find('a')['href'])
            rating = soup.find('span', attrs={'class': 'average-rating'}).find('span').text

            self.product.add_rating(rating)
            self.product.add_reviews_link(link)
        except:
            ...


# parse = Parser("DIOR ADDICT LIPSTICK ")
# parse.parse_irecommend()
#parse.parse_ga()
#parse.parse_letual()
#parse.parse_rivgauche()
# print(parse.product.get_product_reviews_link())
