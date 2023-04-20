# TODO Добавить словарь с ссылками на картинки, возможно добавить ссылку на отзывы


class Product:
    def __init__(self, name: str):
        self.name = name
        self.description = ''
        self.product_in_shops = {}

    def add_description(self, desc: str):
        self.description = desc

    def add_product_data(self, shop: str, price: str, url: str):
        self.product_in_shops[shop] = {'Цена': price, 'Ссылка': url}

    def get_product(self) -> list:
        return [self.name, self.product_in_shops]