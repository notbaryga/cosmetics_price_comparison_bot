class Url:
    _GA_PREFIX = 'https://goldapple.ru/'
    _LETUAL_PREFIX = 'https://www.letu.ru/'
    _RIVGAUCHE_PREFIX = 'https://rivegauche.ru/'
    _IRECOMMEND_PREFIX = 'https://irecommend.ru/'

    _GA_SEARCH = 'catalogsearch/result?q='
    _LETUAL_SEARCH = 'storeru/search?Dy=1&Ntt='
    _RIVGAUCHE_SEARCH = 'search?text='
    _IRECOMMEND_SEARCH = '/srch?query='

    _LETUAL_AJAX = '&pushSite=storeMobileRU&format=json&locale=ru_RU'

    _LETUAL_PRODUCT = 'product/'

    @staticmethod
    def get_ga_search_url(query: list):
        url = Url._GA_PREFIX + Url._GA_SEARCH
        for word in query:
            url += word
            url += '+'
        return url

    @staticmethod
    def get_letual_search_url(query: list):
        url = Url._LETUAL_PREFIX + Url._LETUAL_SEARCH
        for word in query:
            url += word
            url += '+'
        url += Url._LETUAL_AJAX
        return url

    @staticmethod
    def get_rivgauche_search_url(query: list):
        url = Url._RIVGAUCHE_PREFIX + Url._RIVGAUCHE_SEARCH
        for word in query:
            url += word
            url += '%20'
        return url

    @staticmethod
    def get_irecommend_search_url(query: list):
        url = Url._IRECOMMEND_PREFIX + Url._IRECOMMEND_SEARCH
        for word in query:
            url += word
            url += '%20'
        return url

    @staticmethod
    def get_letual_product_url(product_id: str):
        url = Url._LETUAL_PREFIX + Url._LETUAL_PRODUCT + product_id
        return url

    @staticmethod
    def get_rivgauche_product_url(end_url: str):
        url = Url._RIVGAUCHE_PREFIX + end_url
        return url

    @staticmethod
    def get_irecommend_product_url(end_url: str):
        url = Url._IRECOMMEND_PREFIX + end_url
        return url

    @staticmethod
    def get_letual_product_photo(photo_url: str):
        url = Url._LETUAL_PREFIX + photo_url
        return url

