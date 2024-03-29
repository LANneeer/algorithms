"""
И под конец всех блоков мы с гордостью приступаем к самой популярной теме,
Объектно-ориентированное программирование, название говорит само за себя, тут мы представляем наш код в виде объектов.
То есть, теперь у нас не просто код или функция, а полноценный объект и его методы(то что объект может делать).
"""

"""
Давай начнем с самого простого и чего-то "девчачьи", затронем женскую сумочку и его возможности.
Для начала небольшой глоссарий:
Сумочка - Bag,
Вместимость - capacity,
Свободное место - volume,
Предмет - item,
Добавить - add,
Взять - pop.
"""


class Bag:  # создаем объект сумка(да, в Python объекты указываются как класс)
    def __init__(self, capacity):  # эта функция нам нужна что-бы присвоить переменные(атрибуты) для нашего объекта
        self.capacity = capacity  # добавляем вместимость который мы получим при создании объекта
        self.volume = []  # создаем список, как пространство для хранения наших вещей

    def add(self, item):  # создаем метод(функцию) добавления для нашего объекта
        if len(self.volume) < self.capacity:  # если у нас есть еще место тогда мы добавляем предмет
            self.volume.append(item)  # добавляем предмет который мы положим в сумочку
        else:  # если недостаточно места
            return "Недостаточно места"  # говорим что недостаточно места

    def pop(self, index):  # создаем функцию для вытаскивания наших предметов
        return self.volume.pop(index)  # возвращаем предмет, который находится по указанному нами индексу


gucci = Bag(capacity=2)  # создаем нашу сумочку гуччи с вместимостью в 2 предметов

print(gucci.volume)  # смотрим что у нас в сумочке []

gucci.add('помада')  # давай положим туда помаду

print(gucci.volume)  # снова смотрим, и опа! у нас теперь там помада

gucci.pop(0)  # давай ка вытащим нашу помаду

print(gucci.volume)  # оп, сумка теперь пуста

gucci.add('помада')  # вернем-ка туда помаду
gucci.add('зеркало')  # добавим туда зеркало
gucci.add('тоналка')  # добавим туда еще тоналку

print(gucci.volume)  # смотрим что в сумке ['помада', 'зеркало']
# оп у нас не поместилась тоналка, видимо места нехавтило


"""
И так, мы прошли что такое объект,
а теперь давай ка пройдем что такое наследование!

Наследование это когда мы создаем новый объект наследуясь от другого объекта,
в нашем случае мы будем наследоваться от Bag, и создадим Suitcase (чемодан), 
так же как и в реальной жизни они имеют одинаковые свойства, и имеют один и тот же функционал,
однако чемодан более вместителен, давай ка сделаем это на практике
"""


class Suitcase(Bag):
    def __init__(self, capacity):  # эта функция нам нужна что-бы присвоить переменные(атрибуты) для нашего объекта
        self.capacity = capacity * 2  # добавляем вместимость в 2 раза больше, как-никак это чемодан
        self.volume = []  # создаем список, как пространство для хранения наших вещей


"""
Готово, все наши предыдущие методы (функции) добавления и доставания будут унаследованы от Bag (сумки)!

Давай ка проверим это
"""

Louis_vitton = Suitcase(capacity=2)  # создаем наш чемодан от луивитона с вместимостью в 2 * 2 предметов

print(Louis_vitton.volume)  # смотрим что у нас в сумочке []

Louis_vitton.add('свитер')  # давай положим туда свитер

print(Louis_vitton.volume)  # пробуем глянуть ['свитер']

Louis_vitton.pop(0)  # пробуем вытащить

print(Louis_vitton.volume)  # все работает

Louis_vitton.add('брюки')  # добавим теперь туда брюки
Louis_vitton.add('шляпа')  # добавим туда шляпу
Louis_vitton.add('рубашка')  # добавим туда еще рубашку
Louis_vitton.add('майка')  # добавим туда еще майку

print(Louis_vitton.volume)  # смотрим что в сумке ['брюки', 'шляпа', 'рубашка', 'майка']
# теперь у нас все вместилось!
