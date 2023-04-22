# TODO Добавить словарь с ссылками на картинки, возможно добавить ссылку на отзывы


class Product:
    def __init__(self, name: str):
        self.name = name
        self.description = ''
        self.product_in_shops = {}
        self.photo_link = None
        self.rating = None
        self.reviews_link = None

    def add_description(self, desc: str):
        self.description = desc

    def add_product_data(self, shop: str, price: str, url: str):
        self.product_in_shops[shop] = {'Цена': price, 'Ссылка': url}

    def add_product_photo(self, photo_link: str):
        self.photo_link = photo_link

    def add_rating(self, rating: str):
        self.rating = rating

    def add_reviews_link(self, reviews_link: str):
        self.reviews_link = reviews_link

    def get_product_photo(self) -> str|None:
        return self.photo_link

    def get_product_rating(self) -> str|None:
        return self.rating

    def get_product_reviews_link(self) -> str|None:
        return self.reviews_link

    def get_product(self) -> dict:
        return self.product_in_shops
