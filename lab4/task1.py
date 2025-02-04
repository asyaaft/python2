from datetime import datetime
# TODO: описать базовый класс
class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        Returns:
            Строка с информацией о транспортном средстве.
        """
        return f"Транспортное средство: {self.make} {self.model}, {self.year} года выпуска"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для создания копии.

        Returns:
            Строка, представляющая объект для его реконструкции.
        """
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"

    def get_age(self) -> int:
        """Возвращает возраст транспортного средства."""
        return datetime.now().year - self.year

# TODO: описать дочерний класс
class Car(Vehicle):
    """Класс для легковых автомобилей."""

    def __init__(self, make: str, model: str, year: int, num_doors: int):
        """
        Raises:
            ValueError: Если количество дверей не является положительным числом.
        """
        super().__init__(make, model, year)
        if num_doors <= 0:
            raise ValueError("Количество дверей должно быть положительным числом.")
        self._num_doors = num_doors # _num_doors - непубличный атрибут

    def __str__(self) -> str:
        """Перегруженный метод __str__ для более подробной информации."""
        return f"{super().__str__()} ({self._num_doors} двери)"

    def __repr__(self) -> str:
        """Перегруженный метод __repr__ для класса Car."""
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, num_doors={self._num_doors})"

    def get_num_doors(self) -> int:
        """
        Возвращает количество дверей автомобиля.
        Этот метод унаследован от базового класса
        """
        return self._num_doors

    def get_age(self) -> int:
        """
        Перегруженный метод get_age, который возвращает возраст автомобиля и дополнительные сведения.
        Перегрузка необходима для добавления специфической информации для автомобилей.
        """
        age = super().get_age()
        return f"Возраст автомобиля: {age} лет."


if __name__ == "__main__":
    vehicle = Vehicle("Toyota", "Camry", 2020)
    print(vehicle)  # Вывод: Транспортное средство: Toyota Camry, 2020 года выпуска
    print(vehicle.get_age()) # Вывод: 3
    print(repr(vehicle))  # Вывод: Vehicle(make='Toyota', model='Camry', year=2020)


    car = Car("Honda", "Civic", 2022, 4)
    print(car)  # Вывод: Транспортное средство: Honda Civic, 2022 года выпуска (4 двери)
    print(car.get_age()) # Вывод: Возраст автомобиля: 1 лет.
    print(repr(car))  # Вывод: Car(make='Honda', model='Civic', year=2022, num_doors=4)

    try:
        car = Car("Ford", "Focus", 2023, -2) # Проверка на ValueError
    except ValueError as e:
        print(f"Ошибка: {e}") # Вывод: Ошибка: Количество дверей должно быть положительным числом.
        
