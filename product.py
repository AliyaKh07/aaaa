class Product:
    """Класс товара"""

    def __init__(self, product_id: int, name: str, purchase_price: float, selling_price: float) -> None:
        """ Инициализация товара.

        Args:
            product_id: ID товара
            name: Название товара
            purchase_price: Закупочная цена
            selling_price: Цена продажи
        """

        self.product_id = product_id
        self.name = name
        self.purchase_price = purchase_price
        self.selling_price = selling_price

    def from_dict(self, data: dict) -> None:
        """Восстановление объекта из словаря

        Args:
            data: Словарь с данными товара
        """

        self.product_id = data.get('product_id')
        self.name = data.get('name')
        self.purchase_price = data.get('purchase_price')
        self.selling_price = data.get('selling_price')

    def get_profit_per_unit(self) -> float:
        """ Метод для получения прибыли с одной единицы товара".

        Returns:
            profit_per_unit: прибыль с единицы товара
        """

        profit_per_unit = self.selling_price - self.purchase_price

        return profit_per_unit

    def __str__(self) -> str:
        """ Метод для получения информации о товаре

        Returns:
            информация о товаре
        """

        return f"Товар {self.product_id}: {self.name} (покупка: {self.purchase_price}, продажа: {self.selling_price})"

    def to_dict(self) -> dict:
        """Преобразование в словарь для сохранения

        Returns:
             Словарь с информацией о товаре."""

        return {
            'product_id': self.product_id,
            'name': self.name,
            'purchase_price': self.purchase_price,
            'selling_price': self.selling_price
        }
