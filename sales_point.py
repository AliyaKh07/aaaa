from models.product import Product
from models.employee import Employee
from models.customer import Customer


class SalesPoint:
    """Класс пункта продаж"""

    def __init__(self, point_id: int, name: str, address: str) -> None:
        """Инициализация пункта продаж.

        Args:
            point_id: Уникальный идентификатор пункта продаж
            name: Название пункта
            address: Адрес пункта

        """
        self.point_id = point_id
        self.name = name
        self.address = address
        self.products: dict = {}  # Словарь {product_id: quantity}
        self.responsible_person: Employee | None = None # Может быть Employee или None
        self.is_active: bool = True
        self.total_revenue: float = 0  # Общая выручка

    def from_dict(self, data: dict) -> None:
        """Восстановление объекта из словаря

        Args:
            data: Словарь с данными пункта продаж
        """
        self.point_id = data.get('point_id')
        self.name = data.get('name')
        self.address = data.get('address')
        self.products = data.get('products', {})
        self.is_active = data.get('is_active', True)
        self.total_revenue = data.get('total_revenue', 0)

    def set_responsible_person(self, employee: Employee) -> None:
        """Назначение ответственного лица за пункт продаж.

        Args:
            employee: Объект сотрудника
        """

        self.responsible_person = employee

    def add_product(self, product: Product, quantity: int) -> None:
        """Добавление товара в пункт продаж.

        Args:
            product: Объект товара
            quantity: Количество товара для добавления
        """

        if product.product_id in self.products:
            self.products[product.product_id] += quantity
        else:
            self.products[product.product_id] = quantity

    def remove_product(self, product: Product, quantity: int) -> bool:
        """Удаление товара из пункта продаж.

        Args:
            product: Объект товара
            quantity: Количество для удаления

        Returns:
            bool: True если удаление успешно, False если недостаточно товара
        """

        if (product.product_id in self.products and
                self.products[product.product_id] >= quantity):
            self.products[product.product_id] -= quantity
            if self.products[product.product_id] == 0:
                del self.products[product.product_id]

            return True

        return False

    def sell_product(self, product: Product, quantity: int, customer: Customer) -> tuple:
        """Продажа товара покупателю.

        Args:
            product: Объект товара
            quantity: Количество для продажи
            customer: Объект покупателя

        Returns:
            tuple: (bool, float) - (успех_операции, сумма_продажи)
        """

        if self.remove_product(product, quantity):
            revenue: float = product.selling_price * quantity
            self.total_revenue += revenue

            return True, revenue

        return False, 0

    def get_profit(self) -> float:
        """Геттер для получения прибыли пункта продаж.

        Returns:
           total_revenue: Прибыль (общая выручка)
        """

        return self.total_revenue

    def close(self) -> None:
        """Закрытие пункта продаж."""

        self.is_active = False

    def open(self) -> None:
        """ Открытие пункта продаж."""

        self.is_active = True

    def get_all_products(self) -> dict:
        """ Получение всех товаров в пункте продаж

        Returns:
            products: Словарь {id_товара: количество}
        """

        return self.products

    def __str__(self) -> str:
        """ Вывод информации о пункте продаж.

        Returns:
          Строка с информацией о пункте продаж
        """

        status: str = "Работает" if self.is_active else "Закрыт"
        responsible: str = self.responsible_person.name if self.responsible_person else "Не назначен"

        return (f"Пункт продаж {self.point_id}: {self.name}, Адрес: {self.address}, "
                f"Статус: {status}, Ответственный: {responsible}, Выручка: {self.total_revenue}")

    def to_dict(self) -> dict:
        """Преобразование объекта в словарь для сохранения

        Returns:
           Словарь с данными пункта продаж
        """

        return {
            'point_id': self.point_id,
            'name': self.name,
            'address': self.address,
            'products': self.products,
            'responsible_person_id': self.responsible_person.employee_id if self.responsible_person else None,
            'is_active': self.is_active,
            'total_revenue': self.total_revenue
        }
