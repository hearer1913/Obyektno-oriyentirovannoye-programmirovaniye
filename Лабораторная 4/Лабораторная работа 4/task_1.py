class Aircraft:
    """ Базовый класс самолета. """

    def __init__(self, name: str, first_flight: int, wingspan: float):
        """
         Создание и подготовка к работе объекта "Самолет"

         :param name: Именование модели самолета
         :param first_flight: Год первого полета этого самолета
         :param wingspan: Размах крыла самолета, м
         """

        self.name = name
        self.first_flight = first_flight
        self.wingspan = wingspan

    def __str__(self):
        """
        Возвращает строковое представление самолета.
        :return: Информация о самолете.

        """

        return f"Самолет {self.name}. Первый полёт в {self.first_flight} году. Размах крыльев {self.wingspan}"

    def __repr__(self):
        """
        Возвращает строку, представляющую объект класса Aircraft.
        :return: Представление объекта класса Aircraft.

        """

        return f"{self.__class__.__name__}(name={self.name!r}, first_flight={self.first_flight!r}), wingspan={self.wingspan!r})"

    def time_in_service(self):
        """
        Функция которая вычисляет время эксплуатации модели самолета, при условии что текущий год 2024

        :return: Время эксплуатации этой модели самолета в годах

        Примеры:
        >>> aircraft = Aircraft('Airbus A321', 1993, 35.8)
        >>> aircraft.time_in_service()
        31
        """
        return 2024 - self.first_flight


class CargoAircraft(Aircraft):
    """ Дочерний класс транспортного самолета. """

    def __init__(self, name: str, first_flight: int, wingspan: float, payload_capacity: float):
        """
         Создание и подготовка к работе объекта "Транспортный самолет"

         :param name: Именование модели самолета
         :param first_flight: Год первого полета этого самолета
         :param wingspan: Размах крыла самолета, м
         :param payload_capacity: Грузоподъемность, т
         """

        super().__init__(name, first_flight, wingspan)
        self.payload_capacity = payload_capacity

    def __str__(self):
        """
        Возвращает строковое представление самолета.
        :return: Информация о самолете.

        """

        return f"Самолет {self.name}. Первый полёт в {self.first_flight} году. Размах крыльев {self.wingspan}.Грузоподъемность {self.payload_capacity} "

    def cargo_on_aircraft(self, new_cargo: int):
        """
        Функция, которая определяет, может ли самолет перевести заданную массу груза
        :param new_cargo: Масса груза, которую нужно перевезти

        :return: Может ли самолет перевести заданную массу груза

        Примеры:
        >>> caircraft = CargoAircraft('Ил-76', 1971, 50.5, 28)
        >>> caircraft.cargo_on_aircraft(10)
        Транспортный самолет Ил-76 может перевезти 10 т груза.
        """

        if new_cargo <= self.payload_capacity:
            print(f"Транспортный самолет {self.name} может перевезти {new_cargo} т груза.")
        else:
            print(f"Транспортный самолет {self.name} не может перевезти {new_cargo} т груза.")

    def time_in_service(self):
        """
        Функция, которая вычисляет время эксплуатации модели транспортного самолета, при условии что текущий год 2024.
        Время указывается в десятилетиях, так как многие используемые в наше время транспортных самолетов
        были разработаны свыше полувека назад, в отличие от других типов самолетов.

        :return: Время эксплуатации этой модели транспортного самолета в десятилетиях

        Примеры:
        >>> caircraft = CargoAircraft('Ил-76', 1971, 50.5, 28)
        >>> caircraft.time_in_service()
        5.3
        """

        return super().time_in_service() / 10


class PassengerAircraft(Aircraft):
    """ Дочерний класс пассажирского самолета. """

    def __init__(self, name: str, first_flight: int, wingspan: float, passengers: int):
        """
         Создание и подготовка к работе объекта "Транспортный самолет"

         :param name: Именование модели самолета
         :param first_flight: Год первого полета этого самолета
         :param wingspan: Размах крыла самолета, м
         :param passengers: Количество возможных пассажиров
         """

        super().__init__(name, first_flight, wingspan)
        self.passengers = passengers

    def __str__(self):
        """
        Возвращает строковое представление самолета.
        :return: Информация о самолете.

        """

        return f"Самолет {self.name}. Первый полёт в {self.first_flight} году. Размах крыльев {self.wingspan}. Количество пассажиров {self.passengers} "

    def passengers_get_on_aircraft(self, number_of_passengers: int):
        """
        Функция, которая определяет, может ли самолет перевести заданное количество пассажиров
        :param number_of_passengers: Количество пассажиров, которое нужно перевезти

        :return: Может ли самолет перевести заданное количество пассажиров

        Примеры:
        >>> paircraft = PassengerAircraft('Airbus A321', 1993, 35.8, 220)
        >>> paircraft.passengers_get_on_aircraft(280)
        Пассажирский самолет Airbus A321 не может перевезти 280 пассажиров.
        """
        if number_of_passengers <= self.passengers:
            print(f"Пассажирский самолет {self.name} может перевезти {number_of_passengers} пассажиров.")
        else:
            print(f"Пассажирский самолет {self.name} не может перевезти {number_of_passengers} пассажиров.")





if __name__ == "__main__":
    # Write your solution here
    aircraft = Aircraft('Airbus A321', 1993, 35.8)
    caircraft = CargoAircraft('Ил-76', 1971, 50.5, 28)
    paircraft = PassengerAircraft('Airbus A321', 1993, 35.8, 220)

    import doctest

    doctest.testmod()
    pass
