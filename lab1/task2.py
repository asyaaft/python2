from task_1 import Book
from task_1 import Tree
from task_1 import Profile

# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    book = Book("Мцыри", "Лермонтов", 300)
    tree = Tree("Береза", 15.0, 20)
    profile = Profile("user1", 100)

    try:
     # TODO: вызвать метод с некорректными аргументами(b)
     book.read(2.4)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
     tree.grow("abc")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
     profile.add_friend(40.5)
    except TypeError:
        print('Ошибка: неправильные данные')
