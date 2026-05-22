from datetime import datetime
from models.product import Product
from models.customer import Customer


class Order:
    """Класс заказа"""

    def __init__(self, order_id: int, customer: Customer, product: Product,
                 quantity: int, order_type: str) -> None:
        """ Инициализация заказа

        Args:
            order_id : Уникальный идентификатор заказа
            customer : Объект покупателя
            product : Объект товара
            quantity : Количество товара
            order_type : Тип заказа ('sale' - продажа, 'return' - возврат)
        """

        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.order_type = order_type
        self.date: datetime = datetime.now()

        # Расчет суммы заказа в зависимости от типа
        if order_type == 'sale':
            self.amount: float = quantity * product.selling_price
        else:
            self.amount: float = quantity * product.purchase_price

    def from_dict(self, data: dict) -> None:
        """Восстановление объекта из словаря

        Args:
            data: Словарь с данными заказа
        """

        self.order_id = data.get('order_id')
        self.quantity = data.get('quantity')
        self.order_type = data.get('order_type')
        self.amount = data.get('amount')
        date_str = data.get('date')
        if date_str:
            self.date = datetime.fromisoformat(date_str)
        # customer и product восстанавливаются отдельно через менеджер

    def __str__(self) -> str:
        """Строковое представление заказа.

        Returns:
           Строка с информацией о заказе
        """
        type_text: str = "Продажа" if self.order_type == 'sale' else "Возврат"

        return (f"Заказ {self.order_id}: {type_text}, {self.product.name} x{self.quantity}, "
                f"Сумма: {self.amount}, Дата: {self.date}")

    def to_dict(self) -> dict:
        """Преобразование объекта в словарь для сохранения.

        Returns:
            Словарь с данными заказа
        """

        return {
            'order_id': self.order_id,
            'customer_id': self.customer.customer_id,
            'product_id': self.product.product_id,
            'quantity': self.quantity,
            'order_type': self.order_type,
            'date': self.date.isoformat(),
            'amount': self.amount
        }
    