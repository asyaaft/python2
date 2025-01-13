class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str):
        super().__init__(name, author)
        self._pages = self.pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()} ({self.pages} страниц)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str):
        super().__init__(name, author)
        self._duration = self.duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        """
          Устанавливает продолжительность аудиокниги. Проверяет тип и значение.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным")
        self._duration = value

    def __str__(self):
        """
        Возвращает строковое представление аудиокниги.
        """
        return f'{super().__str__()} ({self.duration} ч.)'

    def __repr__(self):
        """
        Возвращает строковое представление объекта для создания копии объекта.

        Returns:
           Строка с кодом для создания объекта.
        """
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"

if __name__ == '__main__':

    book = Book(name='test_name_1', author='test_author_1')
    print(book)
    print(repr(book))

    paper_book = PaperBook(name='test_name_2', author='test_author_2')
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook(name='test_name_3', author='test_author_3')
    print(audio_book)
    print(repr(audio_book))

    try:
        paper_book.pages = "abc"
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        audio_book.duration = -5
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        paper_book.name = 'new name'
    except AttributeError as e:
        print(f"Ошибка: {e}")
    try:
        paper_book.name = 'new name'
    except AttributeError as e:
        print(f"Ошибка: {e}")
