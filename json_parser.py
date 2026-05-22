import json
from storage.baze_serilaizer import FileInfo, BaseSerializer, BaseDeserializer


class JsonParser(FileInfo, BaseSerializer, BaseDeserializer):
    """Парсер для JSON файлов. Работает со всеми типами объектов CRM."""

    __format_of_file = 'json'

    def __init__(self, file_name: str, model_class=None) -> None:
        """Инициализация JSON парсера

        Args:
            file_name: Имя файла
            model_class: Класс модели для десериализации (Product, Employee и т.д.)
        """

        super().__init__(file_name)
        self.set_format_of_file(self.__format_of_file)
        self.model_class = model_class

    def _get_object_id(self, obj) -> str:
        """ Получение ID объекта (внутренний метод)

        Args:
            obj: Объект для получения ID

        Returns:
            result: ID объекта в виде строки
        """

        result = str(id(obj))

        if hasattr(obj, 'product_id'):
            result = str(obj.product_id)
        elif hasattr(obj, 'employee_id'):
            result = str(obj.employee_id)
        elif hasattr(obj, 'customer_id'):
            result = str(obj.customer_id)
        elif hasattr(obj, 'warehouse_id'):
            result = str(obj.warehouse_id)
        elif hasattr(obj, 'point_id'):
            result = str(obj.point_id)
        elif hasattr(obj, 'order_id'):
            result = str(obj.order_id)

        return result

    def serialize_list(self, objects: list) -> None:
        """Сериализация списка объектов в JSON файл

        Args:
            objects: Список объектов для сохранения
        """

        data = {}

        for obj in objects:
            obj_dict = obj.to_dict()
            obj_id = self._get_object_id(obj)
            data[obj_id] = obj_dict

        with open(self.get_full_file_name(), 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2, default=str)

    def serialize(self, obj) -> None:
        """Сериализация одного объекта (добавление или обновление)

        Args:
            obj: Объект для сохранения
        """

        objects_list = self.deserialize()
        new_objects_list = []
        obj_id = self._get_object_id(obj)
        found = False

        for existing_obj in objects_list:
            existing_id = self._get_object_id(existing_obj)
            if existing_id == obj_id:
                new_objects_list.append(obj)
                found = True
            else:
                new_objects_list.append(existing_obj)

        if not found:
            new_objects_list.append(obj)

        self.serialize_list(new_objects_list)

    def deserialize(self) -> list:
        """Десериализация всех объектов из JSON файла.

        Returns:
            list: Список восстановленных объектов

        Raises:
            FileNotFoundError
            ошибка при загрузке файла
        """

        result = []

        if self.model_class:
            try:
                with open(self.get_full_file_name(), 'r', encoding='utf-8') as file:
                    data_dict = json.load(file)

                for data in data_dict.values():
                    obj = self.model_class()
                    if hasattr(obj, 'from_dict'):
                        obj.from_dict(data)
                    result.append(obj)
            except FileNotFoundError:
                print(f"Файл {self.get_full_file_name()} не найден")
            except Exception as e:
                print(f"Ошибка при загрузке {self.get_full_file_name()}: {e}")

        return result

    def deserialize_by_id(self, ids: list) -> list:
        """Десериализация объектов по списку ID

        Args:
            ids: Список ID объектов для загрузки

        Returns:
            list: Список восстановленных объектов

        Raises:
            FileNotFoundError
            ошибка при загрузке файла
        """

        result = []

        if self.model_class and ids:
            try:
                with open(self.get_full_file_name(), 'r', encoding='utf-8') as file:
                    data_dict = json.load(file)

                for obj_id in ids:
                    str_id = str(obj_id)
                    if str_id in data_dict:
                        obj = self.model_class()
                        if hasattr(obj, 'from_dict'):
                            obj.from_dict(data_dict[str_id])
                        result.append(obj)
            except FileNotFoundError:
                print(f"Файл {self.get_full_file_name()} не найден")
            except Exception as e:
                print(f"Ошибка при загрузке {self.get_full_file_name()}: {e}")

        return result
