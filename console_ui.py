from models.warehouse import Warehouse, StorageCell
from models.product import Product
from models.employee import Employee
from models.customer import Customer
from models.sales_point import SalesPoint
from models.order import Order
from storage.crm_data_manager import CRMDataManager


class ConsoleUI:
    """Класс консольного интерфейса CRM системы"""

    def __init__(self) -> None:
        """Инициализация системы, загрузка данных и создание тестовых данных при необходимости"""

        self.data_manager = CRMDataManager()

        # Загрузка данных из файлов
        (self.warehouses, self.sales_points, self.products,
         self.employees, self.customers, self.orders) = self.data_manager.load_all_data()

        # Счетчики для генерации ID
        self.next_ids = {
            'warehouse': 1,
            'sales_point': 1,
            'product': 1,
            'employee': 1,
            'customer': 1,
            'order': 1
        }

        # Обновляем счетчики из загруженных данных
        self._update_next_ids()

        # Если данных нет, создаем тестовые
        if not self.products:
            self.create_test_data()

    def _update_next_ids(self) -> None:
        """Обновление счетчиков ID на основе загруженных данных"""

        if self.warehouses:
            self.next_ids['warehouse'] = max(w.warehouse_id for w in self.warehouses) + 1
        if self.sales_points:
            self.next_ids['sales_point'] = max(sp.point_id for sp in self.sales_points) + 1
        if self.products:
            self.next_ids['product'] = max(p.product_id for p in self.products) + 1
        if self.employees:
            self.next_ids['employee'] = max(e.employee_id for e in self.employees) + 1
        if self.customers:
            self.next_ids['customer'] = max(c.customer_id for c in self.customers) + 1
        if self.orders:
            self.next_ids['order'] = max(o.order_id for o in self.orders) + 1

    def save_all_data(self) -> None:
        """Сохранение всех данных в файлы"""

        self.data_manager.save_all_data(
            self.warehouses, self.sales_points, self.products,
            self.employees, self.customers, self.orders
        )

    def create_test_data(self) -> None:
        """Создание тестовых данных для демонстрации работы системы"""

        # Создаем товары
        product1 = Product(1, "Ноутбук", 50000.0, 70000.0)
        product2 = Product(2, "Мышь", 500.0, 1000.0)
        product3 = Product(3, "Клавиатура", 1500.0, 2500.0)
        self.products.extend([product1, product2, product3])

        # Создаем сотрудников

        emp1 = Employee(1, "Иван Иванов", "Менеджер", 50000.0)
        emp2 = Employee(2, "Петр Петров", "Продавец", 30000.0)
        self.employees.extend([emp1, emp2])

        # Создаем покупателей
        cust1 = Customer(1, "Алексей Сидоров", "+7-999-123-4567")
        cust2 = Customer(2, "Мария Смирнова", "+7-999-765-4321")
        self.customers.extend([cust1, cust2])

        # Создаем склад
        warehouse = Warehouse(1, "Центральный склад", "ул. Промышленная, 1")
        cell1 = StorageCell(1, 100)
        cell2 = StorageCell(2, 50)
        warehouse.add_cell(cell1)
        warehouse.add_cell(cell2)
        warehouse.set_responsible_person(emp1)
        warehouse.cells[0].add_product(product1, 10)
        warehouse.cells[1].add_product(product2, 20)
        self.warehouses.append(warehouse)

        # Создаем пункт продаж
        sales_point = SalesPoint(1, "Магазин на Центральной", "ул. Центральная, 10")
        sales_point.set_responsible_person(emp2)
        sales_point.add_product(product1, 5)
        sales_point.add_product(product2, 15)
        sales_point.add_product(product3, 10)
        self.sales_points.append(sales_point)

        # Обновляем счетчики ID
        self.next_ids['product'] = 4
        self.next_ids['employee'] = 3
        self.next_ids['customer'] = 3
        self.next_ids['warehouse'] = 2
        self.next_ids['sales_point'] = 2
        self.next_ids['order'] = 1

        # Сохраняем тестовые данные
        self.save_all_data()

    def run(self) -> None:
        """Запуск главного меню и основного цикла программы"""

        while True:
            self.show_main_menu()
            choice = input("\nВыберите действие: ")

            if choice == '1':
                self.manage_warehouses()
            elif choice == '2':
                self.manage_sales_points()
            elif choice == '3':
                self.manage_products()
            elif choice == '4':
                self.manage_employees()
            elif choice == '5':
                self.manage_customers()
            elif choice == '6':
                self.manage_orders()
            elif choice == '7':
                self.show_statistics()
            elif choice == '8':
                self.save_all_data()
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def show_main_menu(self) -> None:
        """Отображение главного меню программы"""

        print("ГЛАВНОЕ МЕНЮ CRM СИСТЕМЫ")
        print("1. Управление складами")
        print("2. Управление пунктами продаж")
        print("3. Управление товарами")
        print("4. Управление сотрудниками")
        print("5. Управление покупателями")
        print("6. Операции с заказами")
        print("7. Статистика и отчеты")
        print("8. Выход и сохранение")

    # вспомогательные методы

    def find_warehouse_by_id(self, wh_id: int) -> Warehouse:
        """Поиск склада по ID

        Returns:
            result: Объект Warehouse
        """

        result = None

        for w in self.warehouses:
            if w.warehouse_id == wh_id:
                result = w
                break

        return result

    def find_sales_point_by_id(self, sp_id: int) -> SalesPoint:
        """Поиск пункта продаж по ID

        Returns:
            result: Объект SalesPoint
        """

        result = None

        for sp in self.sales_points:
            if sp.point_id == sp_id:
                result = sp
                break

        return result

    def find_product_by_id(self, prod_id: int) -> Product:
        """Поиск товара по ID

        Returns:
            result: Объект Product
        """

        result = None

        for p in self.products:
            if p.product_id == prod_id:
                result = p
                break

        return result

    def find_employee_by_id(self, emp_id: int) -> Employee:
        """Поиск сотрудника по ID

        Returns:
            result: Объект Employee
        """

        result = None

        for e in self.employees:
            if e.employee_id == emp_id:
                result = e
                break

        return result

    def find_customer_by_id(self, cust_id: int) -> Customer:
        """Поиск покупателя по ID

        Returns:
            result: Объект Customer
        """

        result = None

        for c in self.customers:
            if c.customer_id == cust_id:
                result = c
                break

        return result

    def show_sales_point_products_by_id(self, sp_id: int) -> None:
        """Показать товары в конкретном пункте продаж"""

        sales_point = self.find_sales_point_by_id(sp_id)

        if sales_point:
            products = sales_point.get_all_products()
            if products:
                for prod_id, quantity in products.items():
                    product = self.find_product_by_id(prod_id)
                    if product:
                        print(f"{product.product_id}. {product.name} - {quantity} шт. ({product.selling_price} руб.)")
            else:
                print("Нет товаров")

    # управление складами

    def manage_warehouses(self) -> None:
        """Меню управления складами"""

        while True:
            print("\n УПРАВЛЕНИЕ СКЛАДАМИ ")
            print("1. Показать все склады")
            print("2. Открыть новый склад")
            print("3. Закрыть склад")
            print("4. Информация о складе")
            print("5. Товары на складе")
            print("6. Перемещение товаров")
            print("7. Смена ответственного лица")
            print("8. Закупка товара")
            print("9. Назад")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.show_all_warehouses()
            elif choice == '2':
                self.open_new_warehouse()
            elif choice == '3':
                self.close_warehouse()
            elif choice == '4':
                self.show_warehouse_info()
            elif choice == '5':
                self.show_warehouse_products()
            elif choice == '6':
                self.move_products()
            elif choice == '7':
                self.change_warehouse_responsible()
            elif choice == '8':
                self.purchase_products()
            elif choice == '9':
                break
            else:
                print("Неверный выбор")

    def show_all_warehouses(self) -> None:
        """Показать список всех складов"""

        if not self.warehouses:
            print("Склады отсутствуют")
        else:
            for warehouse in self.warehouses:
                print(warehouse)

    def open_new_warehouse(self) -> None:
        """Открытие нового склада (создание и добавление в систему)"""

        name = input("Введите название склада: ")
        address = input("Введите адрес склада: ")

        warehouse_id = self.next_ids['warehouse']
        self.next_ids['warehouse'] += 1

        warehouse = Warehouse(warehouse_id, name, address)

        # Добавляем ячейки
        num_cells = int(input("Сколько ячеек создать? "))
        for i in range(num_cells):
            capacity = int(input(f"Вместимость ячейки {i + 1}: "))
            cell = StorageCell(i + 1, capacity)
            warehouse.add_cell(cell)

        # Назначаем ответственного
        self.show_all_employees()
        emp_id = int(input("Выберите ID ответственного сотрудника: "))
        responsible = self.find_employee_by_id(emp_id)

        if responsible:
            warehouse.set_responsible_person(responsible)

        self.warehouses.append(warehouse)
        print(f"Склад {name} успешно открыт!")
        self.save_all_data()

    def close_warehouse(self) -> None:
        """Закрытие склада"""

        self.show_all_warehouses()
        wh_id = int(input("Введите ID склада для закрытия: "))
        warehouse = self.find_warehouse_by_id(wh_id)

        if warehouse:
            warehouse.close()
            print(f"Склад {warehouse.name} закрыт")
            self.save_all_data()
        else:
            print("Склад не найден")

    def show_warehouse_info(self) -> None:
        """Информация о складе"""

        self.show_all_warehouses()
        wh_id = int(input("Введите ID склада: "))
        warehouse = self.find_warehouse_by_id(wh_id)

        if warehouse:
            print(warehouse)
            print(f"Количество ячеек: {len(warehouse.cells)}")
        else:
            print("Склад не найден")

    def show_warehouse_products(self) -> None:
        """Товары на складе"""

        self.show_all_warehouses()
        wh_id = int(input("Введите ID склада: "))
        warehouse = self.find_warehouse_by_id(wh_id)

        if warehouse:
            products = warehouse.get_all_products()
            if products:
                for item in products:
                    print(f"Ячейка {item['cell_id']}: {item['product']}, Количество: {item['quantity']}")
            else:
                print("На складе нет товаров")
        else:
            print("Склад не найден")

    def move_products(self) -> None:
        """Перемещение товаров между складом и пунктом продаж"""

        print("Перемещение товаров между складом и пунктом продаж")

        self.show_all_warehouses()
        from_wh_id = int(input("С какого склада переместить? "))
        from_warehouse = self.find_warehouse_by_id(from_wh_id)

        if not from_warehouse:
            print("Склад не найден")
            return

        self.show_all_sales_points()
        to_sp_id = int(input("В какой пункт продаж переместить? "))
        to_sales_point = self.find_sales_point_by_id(to_sp_id)

        if not to_sales_point:
            print("Пункт продаж не найден")
            return

        # Показываем товары на складе
        products = from_warehouse.get_all_products()
        if not products:
            print("Нет товаров для перемещения")
            return

        for item in products:
            print(f"{item['product']} - {item['quantity']} шт.")

        prod_id = int(input("Введите ID товара для перемещения: "))
        product = self.find_product_by_id(prod_id)

        if not product:
            print("Товар не найден")
            return

        quantity = int(input("Сколько переместить? "))

        # Ищем ячейку с товаром
        for cell in from_warehouse.cells:
            if cell.product and cell.product.product_id == prod_id:
                if cell.remove_product(quantity):
                    to_sales_point.add_product(product, quantity)
                    print(f"Перемещено {quantity} шт. товара {product.name}")
                    self.save_all_data()
                    return

        print("Недостаточно товара на складе")

    def change_warehouse_responsible(self) -> None:
        """Смена ответственного лица на складе"""

        self.show_all_warehouses()
        wh_id = int(input("Введите ID склада: "))
        warehouse = self.find_warehouse_by_id(wh_id)

        if not warehouse:
            print("Склад не найден")
            return

        self.show_all_employees()
        emp_id = int(input("Выберите ID нового ответственного сотрудника: "))
        employee = self.find_employee_by_id(emp_id)

        if employee:
            warehouse.set_responsible_person(employee)
            print(f"Ответственный на складе {warehouse.name} изменен на {employee.name}")
            self.save_all_data()
        else:
            print("Сотрудник не найден")

    def purchase_products(self) -> None:
        """Закупка товара на склад"""

        self.show_all_warehouses()
        wh_id = int(input("Введите ID склада для закупки: "))
        warehouse = self.find_warehouse_by_id(wh_id)

        if not warehouse:
            print("Склад не найден")
            return

        self.show_all_products()
        prod_id = int(input("Введите ID товара для закупки: "))
        product = self.find_product_by_id(prod_id)

        if not product:
            print("Товар не найден")
            return

        quantity = int(input("Введите количество для закупки: "))

        # Ищем свободную ячейку или ячейку с таким же товаром
        for cell in warehouse.cells:
            if cell.product is None or cell.product.product_id == prod_id:
                if cell.add_product(product, quantity):
                    print(f"Закуплено {quantity} шт. товара {product.name} на склад {warehouse.name}")
                    self.save_all_data()
                    return

        print("Нет свободных ячеек на складе для этого товара")

    # управление пунктами продаж

    def manage_sales_points(self) -> None:
        """Меню управления пунктами продаж"""

        while True:
            print("\n УПРАВЛЕНИЕ ПУНКТАМИ ПРОДАЖ ")
            print("1. Показать все пункты продаж")
            print("2. Открыть новый пункт продаж")
            print("3. Закрыть пункт продаж")
            print("4. Информация о пункте продаж")
            print("5. Товары в пункте продаж")
            print("6. Смена ответственного лица")
            print("7. Назад")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.show_all_sales_points()
            elif choice == '2':
                self.open_new_sales_point()
            elif choice == '3':
                self.close_sales_point()
            elif choice == '4':
                self.show_sales_point_info()
            elif choice == '5':
                self.show_sales_point_products()
            elif choice == '6':
                self.change_sales_point_responsible()
            elif choice == '7':
                break
            else:
                print("Неверный выбор")

    def show_all_sales_points(self) -> None:
        """Показать все пункты продаж"""

        if not self.sales_points:
            print("Пункты продаж отсутствуют")
        else:
            for sp in self.sales_points:
                print(sp)

    def open_new_sales_point(self) -> None:
        """Открытие нового пункта продаж"""

        name = input("Введите название пункта продаж: ")
        address = input("Введите адрес: ")

        point_id = self.next_ids['sales_point']
        self.next_ids['sales_point'] += 1

        sales_point = SalesPoint(point_id, name, address)

        self.show_all_employees()
        emp_id = int(input("Выберите ID ответственного сотрудника: "))
        responsible = self.find_employee_by_id(emp_id)

        if responsible:
            sales_point.set_responsible_person(responsible)

        self.sales_points.append(sales_point)
        print(f"Пункт продаж {name} успешно открыт!")
        self.save_all_data()

    def close_sales_point(self) -> None:
        """Закрытие пункта продаж"""

        self.show_all_sales_points()
        sp_id = int(input("Введите ID пункта продаж для закрытия: "))
        sales_point = self.find_sales_point_by_id(sp_id)

        if sales_point:
            sales_point.close()
            print(f"Пункт продаж {sales_point.name} закрыт")
            self.save_all_data()
        else:
            print("Пункт продаж не найден")

    def show_sales_point_info(self) -> None:
        """Информация о пункте продаж"""

        self.show_all_sales_points()
        sp_id = int(input("Введите ID пункта продаж: "))
        sales_point = self.find_sales_point_by_id(sp_id)

        if sales_point:
            print(sales_point)
            print(f"Доходность: {sales_point.get_profit()} руб.")
        else:
            print("Пункт продаж не найден")

    def show_sales_point_products(self) -> None:
        """Товары в пункте продаж"""

        self.show_all_sales_points()
        sp_id = int(input("Введите ID пункта продаж: "))
        sales_point = self.find_sales_point_by_id(sp_id)

        if sales_point:
            products = sales_point.get_all_products()
            if products:
                for prod_id, quantity in products.items():
                    product = self.find_product_by_id(prod_id)
                    if product:
                        print(f"{product.name} - {quantity} шт. (цена: {product.selling_price} руб.)")
            else:
                print("В пункте продаж нет товаров")
        else:
            print("Пункт продаж не найден")

    def change_sales_point_responsible(self) -> None:
        """Смена ответственного лица в пункте продаж"""

        self.show_all_sales_points()
        sp_id = int(input("Введите ID пункта продаж: "))
        sales_point = self.find_sales_point_by_id(sp_id)

        if not sales_point:
            print("Пункт продаж не найден")
            return

        self.show_all_employees()
        emp_id = int(input("Выберите ID нового ответственного сотрудника: "))
        employee = self.find_employee_by_id(emp_id)

        if employee:
            sales_point.set_responsible_person(employee)
            print(f"Ответственный в {sales_point.name} изменен на {employee.name}")
            self.save_all_data()
        else:
            print("Сотрудник не найден")

    # управление товарами

    def manage_products(self) -> None:
        """Меню управления товарами"""
        while True:
            print("\n УПРАВЛЕНИЕ ТОВАРАМИ ")
            print("1. Показать все товары")
            print("2. Добавить новый товар")
            print("3. Информация о товарах доступных к закупке")
            print("4. Назад")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.show_all_products()
            elif choice == '2':
                self.add_new_product()
            elif choice == '3':
                self.show_available_for_purchase()
            elif choice == '4':
                break
            else:
                print("Неверный выбор")

    def show_all_products(self) -> None:
        """Показать все товары"""

        if not self.products:
            print("Товары отсутствуют")
        else:
            for product in self.products:
                print(product)
                print(f"  Прибыль с единицы: {product.get_profit_per_unit()} руб.")

    def add_new_product(self) -> None:
        """Добавление нового товара"""

        name = input("Название товара: ")
        purchase_price = float(input("Закупочная цена: "))
        selling_price = float(input("Цена продажи: "))

        product_id = self.next_ids['product']
        self.next_ids['product'] += 1

        product = Product(product_id, name, purchase_price, selling_price)
        self.products.append(product)
        print(f"Товар {name} добавлен!")
        self.save_all_data()

    def show_available_for_purchase(self) -> None:
        """Товары доступные к закупке (все товары системы)"""

        print("\n ТОВАРЫ ДОСТУПНЫЕ К ЗАКУПКЕ")
        for product in self.products:
            print(f"{product.product_id}. {product.name} - {product.purchase_price} руб.")

    # управление сотрудниками

    def manage_employees(self) -> None:
        """Меню управления сотрудниками"""

        while True:
            print("\n УПРАВЛЕНИЕ СОТРУДНИКАМИ ")
            print("1. Показать всех сотрудников")
            print("2. Найм сотрудника")
            print("3. Увольнение сотрудника")
            print("4. Назад")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.show_all_employees()
            elif choice == '2':
                self.hire_employee()
            elif choice == '3':
                self.fire_employee()
            elif choice == '4':
                break
            else:
                print("Неверный выбор")

    def show_all_employees(self) -> None:
        """Показать всех сотрудников"""

        if not self.employees:
            print("Сотрудники отсутствуют")
        else:
            for employee in self.employees:
                print(employee)

    def hire_employee(self) -> None:
        """Найм нового сотрудника"""

        name = input("Имя сотрудника: ")
        position = input("Должность: ")
        salary = float(input("Зарплата: "))

        employee_id = self.next_ids['employee']
        self.next_ids['employee'] += 1

        employee = Employee(employee_id, name, position, salary)
        self.employees.append(employee)
        print(f"Сотрудник {name} нанят!")
        self.save_all_data()

    def fire_employee(self) -> None:
        """Увольнение сотрудника"""

        self.show_all_employees()
        emp_id = int(input("Введите ID сотрудника для увольнения: "))
        employee = self.find_employee_by_id(emp_id)

        if employee:
            employee.fire()
            print(f"Сотрудник {employee.name} уволен")
            self.save_all_data()
        else:
            print("Сотрудник не найден")

    # управление покупателями

    def manage_customers(self) -> None:
        """Меню управления покупателями"""

        while True:
            print("\n УПРАВЛЕНИЕ ПОКУПАТЕЛЯМИ ")
            print("1. Показать всех покупателей")
            print("2. Добавить покупателя")
            print("3. Назад")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.show_all_customers()
            elif choice == '2':
                self.add_customer()
            elif choice == '3':
                break
            else:
                print("Неверный выбор")

    def show_all_customers(self) -> None:
        """Показать всех покупателей"""

        if not self.customers:
            print("Покупатели отсутствуют")
        else:
            for customer in self.customers:
                print(customer)

    def add_customer(self) -> None:
        """Добавление нового покупателя"""

        name = input("Имя покупателя: ")
        phone = input("Телефон: ")

        customer_id = self.next_ids['customer']
        self.next_ids['customer'] += 1

        customer = Customer(customer_id, name, phone)
        self.customers.append(customer)
        print(f"Покупатель {name} добавлен!")
        self.save_all_data()

    # операции с заказами

    def manage_orders(self) -> None:
        """Меню управления заказами"""

        while True:
            print("\n ОПЕРАЦИИ С ЗАКАЗАМИ ")
            print("1. Продажа товара")
            print("2. Возврат товара")
            print("3. Показать все заказы")
            print("4. Назад")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.sell_product()
            elif choice == '2':
                self.return_product()
            elif choice == '3':
                self.show_all_orders()
            elif choice == '4':
                break
            else:
                print("Неверный выбор")

    def sell_product(self) -> None:
        """Продажа товара покупателю"""

        self.show_all_sales_points()
        sp_id = int(input("Выберите пункт продаж: "))
        sales_point = self.find_sales_point_by_id(sp_id)

        if not sales_point or not sales_point.is_active:
            print("Пункт продаж не найден или закрыт")

            return

        self.show_all_customers()
        cust_id = int(input("Выберите покупателя: "))
        customer = self.find_customer_by_id(cust_id)

        if not customer:
            print("Покупатель не найден")

            return

        self.show_sales_point_products_by_id(sp_id)
        prod_id = int(input("Выберите ID товара: "))
        product = self.find_product_by_id(prod_id)

        if not product:
            print("Товар не найден")

            return

        quantity = int(input("Количество: "))

        success, revenue = sales_point.sell_product(product, quantity, customer)

        if success:
            # Создаем заказ
            order_id = self.next_ids['order']
            self.next_ids['order'] += 1
            order = Order(order_id, customer, product, quantity, 'sale')
            self.orders.append(order)
            customer.add_purchase(order)

            print(f"Продажа успешна! Сумма: {revenue} руб.")
            self.save_all_data()
        else:
            print("Недостаточно товара в наличии")

    def return_product(self) -> None:
        """Возврат товара"""

        print("Возврат товара")

        order_id = int(input("Введите ID заказа для возврата: "))
        found_order = None

        for order in self.orders:
            if order.order_id == order_id and order.order_type == 'sale':
                found_order = order
                break

        if found_order:
            print(f"Возврат товара {found_order.product.name} x{found_order.quantity}")
            print(f"Сумма возврата: {found_order.amount} руб.")

            # Создаем заказ на возврат
            return_order_id = self.next_ids['order']
            self.next_ids['order'] += 1
            return_order = Order(return_order_id, found_order.customer,
                                 found_order.product, found_order.quantity, 'return')
            self.orders.append(return_order)

            self.save_all_data()
        else:
            print("Заказ не найден")

    def show_all_orders(self) -> None:
        """Показать все заказы"""
        if not self.orders:
            print("Заказов нет")
        else:
            for order in self.orders:
                print(order)

    # статистика

    def show_statistics(self) -> None:
        """Статистика и отчеты"""

        print("\n СТАТИСТИКА И ОТЧЕТЫ ")

        active_warehouses = len([w for w in self.warehouses if w.is_active])
        active_sales_points = len([sp for sp in self.sales_points if sp.is_active])
        active_employees = len([e for e in self.employees if e.is_active])

        print(f"Всего складов: {active_warehouses}")
        print(f"Всего пунктов продаж: {active_sales_points}")
        print(f"Всего сотрудников: {active_employees}")
        print(f"Всего покупателей: {len(self.customers)}")
        print(f"Всего заказов: {len(self.orders)}")

        total_revenue = sum(sp.total_revenue for sp in self.sales_points)
        print(f"Общая выручка: {total_revenue} руб.")

        # Информация о доходности по каждому пункту продаж
        print("\n ДОХОДНОСТЬ ПУНКТОВ ПРОДАЖ ")
        for sp in self.sales_points:
            if sp.is_active:
                print(f"{sp.name}: {sp.get_profit()} руб.")