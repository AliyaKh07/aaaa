from abc import ABC, abstractmethod


class BaseSerializer(ABC):
    """Абстрактный базовый класс для сериализаторов"""

    @abstractmethod
    def serialize(self, obj) -> None:
        """
        Метод для сериализации одного объекта

        Args:
            obj: Объект для сериализации
        """

        pass

    @abstractmethod
    def serialize_list(self, objects: list) -> None:
        """Метод для сериализации списка объектов

        Args:
            objects: Список объектов для сериализации
        """

        pass


class BaseDeserializer(ABC):
    """Абстрактный базовый класс для десериализаторов"""

    @abstractmethod
    def deserialize(self) -> list:
        """
        Метод для десериализации всех данных из файла

        Returns:
            list: Список восстановленных объектов
        """

        pass

    @abstractmethod
    def deserialize_by_id(self, ids: list) -> list:
        """Метод для десериализации объектов по ID

        Args:
            ids: Список ID объектов для загрузки

        Returns:
            list: Список восстановленных объектов
        """

        pass


class FileInfo:
    """Класс с информацией о файле"""

    __format_of_file = None
    __full_file_name = None

    def __init__(self, file_name: str) -> None:
        """Инициализация файла

        Args:
            file_name: Имя файла
        """

        self.__file_name = file_name

    def set_filename(self, file_name: str) -> None:
        """Сеттер для имени файла

        Args:
            file_name: Имя файла
        """

        self.__file_name = file_name

    def get_file_name(self) -> str:
        """Геттер для имени файла

        Returns:
            file_name: Имя файла
         """

        return self.__file_name

    def set_format_of_file(self, format_of_file: str) -> None:
        """Сеттер для формата файла

        Args:
            format_of_file: Формат файла
        """

        self.__format_of_file = format_of_file

    def get_format_of_file(self) -> str:
        """Геттер для формата файла

        Returns:
            format_of_file: Формат файла
        """

        return self.__format_of_file

    def get_full_file_name(self) -> str:
        """Метод для получения полного имени файла

        Returns:
            file_name.format_of_file: Полное имя файла
        """
        
        return f'{self.__file_name}.{self.__format_of_file}'