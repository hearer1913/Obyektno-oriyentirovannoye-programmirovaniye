# TODO Написать 3 класса с документацией и аннотацией типов
class Bus:
    def __init__(self, route_number: int, number_of_passengers: int, bus_capacity: int):
        """
        Создание и подготовка к работе объекта "Автобус"

        :param route_number: Номер маршрута автобуса
        :param number_of_passengers: Количество пассажиров в автобусе
        :param bus_capacity: Вместимость автобуса
        """

        self.route_number = route_number
        self.number_of_passengers = number_of_passengers
        self.bus_capacity = bus_capacity
        if not isinstance(route_number, int):
            raise TypeError
        if route_number < 0:
            raise ValueError

        if not isinstance(number_of_passengers, int):
            raise TypeError
        if number_of_passengers < 0:
            raise ValueError

        if not isinstance(bus_capacity, int):
            raise TypeError
        if not bus_capacity > 0:
            raise ValueError

    def passengers_get_on_bus(self, passengers: int) -> int:
        """
        Пассажиры заходят в автобус.

        Если количество зашедших пассажиров превышает количество свободных мест,
        то возвращается количество непоместившихся пассажиров.

        :param passengers: Количество заходящих пассажиров
        :return: Количество непоместившихся пассажиров

        >>> bus = Bus(24, 0, 37)
        >>> bus.passengers_get_on_bus(38)

        """
        ...

    def is_bus(self) -> bool:
        """
         Функция которая проверяет является ли словарь автобусом

        :return: Является ли объект автобусом или нет

        >>> bus = Bus(24, 0, 37)
        >>> bus.is_bus()
        """
        ...


class Table:
    def __init__(self, table_legs: int, material: str, width: float, length: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param table_legs: Количество ножек у стола
        :param material: Материал, из которого изготовлен стол
        :param width: Ширина стола, м
        :param length: Длина стола, м
        """

        self.table_legs = table_legs
        self.material = material
        self.width = width
        self.length = length

        if not isinstance(table_legs, int):
            raise TypeError
        if not table_legs >= 0:
            raise ValueError

        if not isinstance(material, str):
            raise TypeError

        if not isinstance(width, float):
            raise TypeError
        if not width >= 0:
            raise ValueError

        if not isinstance(length, float):
            raise TypeError
        if not length >= 0:
            raise ValueError

    def table_area(self) -> float:
        """
        Функция, которая вычисляет площадь стола

        :return: Площадь стола

        >>> table = Table(4, 'дерево', 0.37, 0.55)
        >>> table.table_area()

        """
        ...

    def is_table(self) -> bool:
        """
        Функция которая проверяет является ли словарь столом

        :return: Является ли объект столом или нет

        >>> table = Table(4, 'дерево', 0.37, 0.55)
        >>> table.is_table()

        """
        ...


class Pine:
    def __init__(self, diameter_of_trunk: int | float, height_of_trunk: int | float):
        """
        Создание и подготовка к работе объекта "Сосна"

        :param diameter_of_trunk: Диаметр ствола сосны на высоте груди, см
        :param height_of_trunk: Высота ствола сосны, м
        """

        self.diameter_of_trunk = diameter_of_trunk
        self.height_of_trunk = height_of_trunk

        if not isinstance(diameter_of_trunk, (int, float)):
            raise TypeError
        if diameter_of_trunk < 0:
            raise ValueError

        if not isinstance(height_of_trunk, (int, float)):
            raise TypeError
        if height_of_trunk < 0:
            raise ValueError

    def tree_volume(self) -> int | float:
        """
        Определение объема ствола растущей сосны.

        :return: Объем ствола растущей сосны

        >>> pine = Pine(29.8, 25.3)
        >>> pine.tree_volume()

        """
        ...

    def wood_beams(self, length_of_beam: int, width_of_beam: int, height_of_beam: int) -> int:
        """
         Функция которая определяет количество бруса или досок в одной сосне

        :param length_of_beam: Длина бруса/доски, мм
        :param width_of_beam: Ширина бруса/доски, мм
        :param height_of_beam: Высота бруса/доски, мм

        :return: Количество бруса или досок в одной сосне

        >>> pine = Pine(29.8, 25.3)
        >>> pine.wood_beams(6000, 150, 100)
        """
        ...


if __name__ == "__main__":
    bus = Bus(24, 0, 37)
    table = Table(4, 'дерево', 0.37, 0.55)
    pine = Pine(29.8, 25.3)

    import doctest

    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
