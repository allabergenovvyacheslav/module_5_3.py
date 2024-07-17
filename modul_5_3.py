class House:
    houses_history = []  # список для хранения названия созданных объектов.

    def __new__(cls, *args, **kwargs):

        name = args[0]  # Создаем переменную и присваиваем ей значение объекта по индексу

        cls.houses_history.append(name)  # Добавляем переменную в список названия созданных объектов

        return super().__new__(cls)  # переопределенный __new__ возвращает созданный экз-р класса House

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)



