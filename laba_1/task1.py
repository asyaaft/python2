# TODO: Подробно описать три произвольных класса
# TODO: описать класс
class Book:
    def __init__(self, title: str, author: str, pages: int):
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int) -> str:
        """
               Возвращает сообщение о том, сколько страниц книги было прочитано.

               Args:
                   pages_to_read (int): Количество страниц для чтения.

               Returns:
                   str: Сообщение о прочтении страниц.

               Raises:
                   ValueError: Если количество страниц для чтения не является положительным числом.

               >>> book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 250)
               >>> book.read(50)
               'Вы прочитали 50 страниц из 250.'
               """
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным числом.")
        return f"Вы прочитали {pages_to_read} страниц из {self.pages}."

    def get_summary(self) -> str:
        """
        Возвращает краткое описание книги (название и автор).

        Returns:
          str: Строка, содержащая название и автора.

        >>> book = Book("Pride and Prejudice", "Jane Austen", 400)
        >>> book.get_summary()
        'Pride and Prejudice написана Jane Austen'
        """
        return f"{self.title} написана {self.author}"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# TODO: описать ещё класс
class Tree:
    def __init__(self, species: str, height: float, age: int = 0):
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительна.")
        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, growth_amount: float) -> None:
        """
                Увеличивает высоту дерева.

                Args:
                    growth_amount: Прирост высоты (число с плавающей точкой, в метрах).

                Raises:
                    ValueError: Если прирост высоты не положителен.
                    TypeError: Если прирост высоты не число.
                """
        if not isinstance(growth_amount, (int, float)):
            raise TypeError("Прирост высоты должен быть числом.")
        if growth_amount <= 0:
            raise ValueError("Прирост высоты должен быть положительным.")
        self.height += growth_amount

    def get_age(self) -> int:
        """
                Возвращает возраст дерева.

                Returns:
                    Возраст дерева (целое число).

                >>> tree = Tree("Дуб", 10, 5)
                >>> tree.get_age()
                5
                """
        return self.age

# TODO: и ещё один
class Profile:
    def __init__(self, username: str, friends_count: int = 0):
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой.")
        if not isinstance(friends_count, int):
            raise TypeError("Количество друзей должно быть целым числом.")
        if friends_count < 0:
            raise ValueError("Количество друзей не может быть отрицательным.")
        self.username = username
        self.friends_count = friends_count

    def add_friend(self, num_friends: int) -> int:
        """
                Добавляет друзей к профилю.

                Args:
                    num_friends: Количество добавляемых друзей (целое число).

                Returns:
                    Обновленное количество друзей (целое число).

                Raises:
                    ValueError: если количество добавляемых друзей меньше нуля.
                    TypeError: если num_friends не целое число.

                >>> profile = Profile("testuser")
                >>> profile.add_friend(5)
                5
                """
        if not isinstance(num_friends, int):
            raise TypeError("Количество друзей должно быть целым числом.")
        if num_friends < 0:
            raise ValueError("Количество друзей не может быть отрицательным.")
        self.friends_count += num_friends
        return self.friends_count

    def get_username(self) -> str:
        """
                Возвращает имя пользователя.

                Returns:
                    Имя пользователя (строка).

                >>> profile = Profile("testuser")
                >>> profile.get_username()
                'testuser'
                """
        return self.username