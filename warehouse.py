from models.employee import Employee
from models.product import Product


class StorageCell:
    """Класс ячейки склада"""

    def __init__(self, cell_id: int, max_capacity: int) -> None:
        """ Инициализация ячейки.

        Args:
            cell_id: ID ячейки.
            max_capacity: Максимальная вместимость.
        """

        self.cell_id = cell_id
        self.max_capacity = max_capacity
        self.product = None  # Товар в ячейке
        self.quantity = 0  # Количество товара

    def from_dict(self, data: dict) -> None:
        """Восстановление объекта из словаря

        Args:
            data: Словарь с данными ячейки
        """

        self.cell_id = data.get('cell_id')
        self.max_capacity = data.get('max_capacity')
        # product восстанавливается отдельно
        self.quantity = data.get('quantity', 0)

    def add_product(self, product: Product, quantity: int) -> bool:
        """Добавление товара в ячейку.

        Returns:
            bool: True если добавление успешно, False если превышена вместимость.
        """

        if self.product is None or self.product.product_id == product.product_id:
            if self.quantity + quantity <= self.max_capacity:
                self.product = product
                self.quantity += quantity

                return True

        return False

    def remove_product(self, quantity: int) -> bool:
        """Удаление товара из ячейки.

        Args:
            quantity: Количество для удаления

        Returns:
            bool:True если удаление успешно, False если недостаточно товара.
        """

        if self.quantity >= quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.product = None

            return True

        return False

    def __str__(self) -> str:
        """Строковое представление ячейки.

        Returns:
            Информация о содержимом ячейки
        """

        if self.product:

            return f"Ячейка {self.cell_id}: {self.product.name} - {self.quantity} шт."

        return f"Ячейка {self.cell_id}: пусто"

    def to_dict(self) -> dict:
        """ Преобразование данных ячейки в словарь для сохранения.

        Returns:
            dict: Словарь с данными ячейки.
        """

        return {
            'cell_id': self.cell_id,
            'max_capacity': self.max_capacity,
            'product_id': self.product.product_id if self.product else None,
            'quantity': self.quantity
        }

class Warehouse:
    """Класс склада"""

    def __init__(self, warehouse_id: int, name: str, address: str) -> None:
        """Инициализация склада.

        Args:
            warehouse_id: ID склада
            name: Название склада
            address: Адрес склада
        """

        self.warehouse_id = warehouse_id
        self.name = name
        self.address = address
        self.cells = []  # Список ячеек
        self.responsible_person = None  # Ответственное лицо
        self.is_active = True  # Статус склада

    def add_cell(self, cell: StorageCell) -> None:
        """Добавление ячейки на склад

        Args:
            cell:Объект ячейки
        """
        self.cells.append(cell)

    def set_responsible_person(self, employee:Employee) -> None:
        """Назначение ответственного лица.

        Args:
            employee: Объект сотрудника.
        """

        self.responsible_person = employee

    def close(self) -> None:
        """Закрытие склада."""

        self.is_active = False

    def open(self) -> None:
        """Открытие склада."""

        self.is_active = True

    def get_all_products(self) -> list:
        """Получение всех товаров на складе.

        Returns:
            list: Список словарей с информацией о товарах
        """

        products_info = []

        for cell in self.cells:
            if cell.product:
                products_info.append({
                    'product': cell.product,
                    'quantity': cell.quantity,
                    'cell_id': cell.cell_id
                })

        return products_info

    def __str__(self) -> str :
        """Строковое представление склада.

        Returns:
            Строка с информацией о складе.
        """

        status = "Работает" if self.is_active else "Закрыт"
        responsible = self.responsible_person.name if self.responsible_person else "Не назначен"

        return f"Склад {self.warehouse_id}: {self.name}, Адрес: {self.address}, Статус: {status}, Ответственный: {responsible}"

    def to_dict(self) -> dict:
        """Преобразование объекта в словарь для сохранения.

        Returns:
            Словарь с данными склада
        """
        return {
            'warehouse_id': self.warehouse_id,
            'name': self.name,
            'address': self.address,
            'cells': [cell.to_dict() for cell in self.cells],
            'responsible_person_id': self.responsible_person.employee_id if self.responsible_person else None,
            'is_active': self.is_active
        }
