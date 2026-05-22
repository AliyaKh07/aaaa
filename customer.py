class Customer:
    """Класс покупателя"""

    def __init__(self, customer_id: int, name: str, phone: str) -> None:
        """ Инициализация покупателя.

        Args:
            customer_id: ID покупателя
            Имя покупателя
            Телефон покупателя
        """

        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.purchase_history = []  # История покупок

    def from_dict(self, data: dict) -> None:
        """Восстановление объекта из словаря

        Args:
            data: Словарь с данными покупателя
        """

        self.customer_id = data.get('customer_id')
        self.name = data.get('name')
        self.phone = data.get('phone')
        # purchase_history восстанавливается отдельно через менеджер

    def add_purchase(self, order) -> None:
        """Добавление покупки в историю.

        Args:
            order:Объект заказа.
        """

        self.purchase_history.append(order)

    def __str__(self) -> str:
        """ Метод для вывода информации о покупателе

        Returns:
            Информация о покупателе
        """

        return f"Покупатель {self.customer_id}: {self.name}, тел: {self.phone}"

    def to_dict(self) -> dict:
        """Преобразование в словарь для сохранения.

        Returns:
            Словарь с информацией о покупателе
        """

        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'phone': self.phone,
            'purchase_history_ids': [order.order_id for order in self.purchase_history]
        }
