def make_product_message(query: str, shops: dict, rating: str) -> str:
    ans = query + '\n\n'

    ans += f'Рейтинг: {rating}\n\n'

    ans += 'Товар в магазинах:\n'
    for shop in shops:
        ans += '*' + shop + '*' + '\n'
        for option in shops[shop]:
            if option == 'Ссылка':
                ans += f'[Перейти в магазин]({shops[shop][option]})'
            else:
                ans += option + ': ' + str(shops[shop][option]) + '\n'
        ans += '\n\n'
    return ans
#
# print(make_product_message('привет', {
#                                 'Золотое яблоко':
#                                     {'Цена': '3570',
#                                      'Ссылка': 'https://goldapple.ru/10001-19000003807-rouge-dior-velvet-star-edition'},
#                                 'Летуаль':
#                                     {'Цена': 3650,
#                                      'Ссылка': 'https://www.letu.ru/product/114300377'},
#                                 'Рив Гош':
#                                     {'Цена': '4600',
#                                      'Ссылка': 'https://rivegauche.ru//product/dior-rouge-blush-361-potseluy'}
#                                 }
# ))

