min_value = 4
max_value = 18
print('all squar roots: ')
for i in range(min_value, max_value, 2):
    print(i**0.5)

queriesList = "смотреть сериалы онлайн".split()
print('\n', queriesList, '\n')

queriesText = "смотреть сериалы онлайн;новости спорта;афиша кино;курс доллара;сериалы этим летом;курс по питону;сериалы про спорт"
print('word count:', len(queriesText.replace(";", " ").split()), '\n')

semantic_list = ['одеяло !купить', 'одеяло !продажа','одеяло цена',
                'одеяло стоимость','одеяло прайс','одеяло дешево',
                'одеяло недорого','одеяло заказать','одеяло на заказ',
                'одеяло с доставкой', 'одеяло магазин','одеяло интернет магазин',
                'одеяло со скидкой','одеяло акция','одеяло распродажа']
string_to_find = 'одеяло по дешевке'

if string_to_find in semantic_list:
    print('Фраза "{}" входит в семантическое ядро'.format( string_to_find), '\n') 
else:
    print('Фраза "{}" не входит в семантическое ядро'.format( string_to_find), '\n')

queries = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"

words = ['сериалы', 'курс']
result = ""
for query in queries.split(','):
    for text in query.split():
        if text in words:
            result = query
            print(result)
print(result)
