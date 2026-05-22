from storage.json_parser import JsonParser
from models.product import Product
from models.employee import Employee
from models.customer import Customer
from models.warehouse import Warehouse
from models.sales_point import SalesPoint
from models.order import Order


class CRMDataManager:
    """Менеджер для управления всеми данными CRM"""

    def __init__(self):
        """Инициализация менеджера данных"""

        self.product_parser = JsonParser('products', Product)
        self.employee_parser = JsonParser('employees', Employee)
        self.customer_parser = JsonParser('customers', Customer)
        self.warehouse_parser = JsonParser('warehouses', Warehouse)
        self.sales_point_parser = JsonParser('sales_points', SalesPoint)
        self.order_parser = JsonParser('orders', Order)

    def save_all_products(self, products: list) -> None:
        """Сохранение всех товаров

        Args:
            products: Список товаров
        """

        self.product_parser.serialize_list(products)

    def load_all_products(self) -> list:
        """Загрузка всех товаров

        Returns:
            list: Список товаров
        """

        return self.product_parser.deserialize()

    def save_product(self, product: Product) -> None:
        """ Сохранение одного товара (добавление или обновление)

        Args:
            product: Объект товара
        """

        self.product_parser.serialize(product)

    def save_all_employees(self, employees: list) -> None:
        """Сохранение всех сотрудников"""

        self.employee_parser.serialize_list(employees)

    def load_all_employees(self) -> list:
        """Загрузка всех сотрудников"""

        return self.employee_parser.deserialize()

    def save_employee(self, employee: Employee) -> None:
        """Сохранение одного сотрудника"""

        self.employee_parser.serialize(employee)

    def save_all_customers(self, customers: list) -> None:
        """Сохранение всех покупателей"""

        self.customer_parser.serialize_list(customers)

    def load_all_customers(self) -> list:
        """Загрузка всех покупателей"""

        return self.customer_parser.deserialize()

    def save_customer(self, customer: Customer) -> None:
        """Сохранение одного покупателя"""

        self.customer_parser.serialize(customer)

    def save_all_warehouses(self, warehouses: list) -> None:
        """Сохранение всех складов"""

        self.warehouse_parser.serialize_list(warehouses)

    def load_all_warehouses(self) -> list:
        """Загрузка всех складов"""

        return self.warehouse_parser.deserialize()

    def save_warehouse(self, warehouse: Warehouse) -> None:
        """Сохранение одного склада"""

        self.warehouse_parser.serialize(warehouse)

    def save_all_sales_points(self, sales_points: list) -> None:
        """Сохранение всех пунктов продаж"""

        self.sales_point_parser.serialize_list(sales_points)

    def load_all_sales_points(self) -> list:
        """Загрузка всех пунктов продаж"""

        return self.sales_point_parser.deserialize()

    def save_sales_point(self, sales_point: SalesPoint) -> None:
        """Сохранение одного пункта продаж"""

        self.sales_point_parser.serialize(sales_point)

    def save_all_orders(self, orders: list) -> None:
        """Сохранение всех заказов"""

        self.order_parser.serialize_list(orders)

    def load_all_orders(self) -> list:
        """Загрузка всех заказов"""

        return self.order_parser.deserialize()

    def save_order(self, order: Order) -> None:
        """Сохранение одного заказа"""

        self.order_parser.serialize(order)

    def save_all_data(self, warehouses: list, sales_points: list, products: list,
                      employees: list, customers: list, orders: list) -> None:
        """Сохранение всех данных системы

        Args:
            warehouses: Список складов
            sales_points: Список пунктов продаж
            products: Список товаров
            employees: Список сотрудников
            customers: Список покупателей
            orders: Список заказов
        """

        self.save_all_warehouses(warehouses)
        self.save_all_sales_points(sales_points)
        self.save_all_products(products)
        self.save_all_employees(employees)
        self.save_all_customers(customers)
        self.save_all_orders(orders)

        print("Все данные сохранены")

    def load_all_data(self):
        """Загрузка всех данных системы

        Returns:
            tuple: (warehouses, sales_points, products, employees, customers, orders)
        """
        
        warehouses = self.load_all_warehouses()
        sales_points = self.load_all_sales_points()
        products = self.load_all_products()
        employees = self.load_all_employees()
        customers = self.load_all_customers()
        orders = self.load_all_orders()

        print("Все данные загружены")
        return warehouses, sales_points, products, employees, customers, orders