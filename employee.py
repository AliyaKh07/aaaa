class Employee:
    """Класс сотрудника"""

    def __init__(self, employee_id: int, name: str, position: str, salary: float) -> None:
        """ Инициализация сотрудника.

         Args:
             employee_id: ID сотрудника
             name: Имя сотрудника
             position: Должность
             salary: Зарплата
        """

        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.is_active = True  # Статус сотрудника (работает/уволен)

    def from_dict(self, data: dict) -> None:
        """Восстановление объекта из словаря

        Args:
            data: Словарь с данными сотрудника
        """

        self.employee_id = data.get('employee_id')
        self.name = data.get('name')
        self.position = data.get('position')
        self.salary = data.get('salary')
        self.is_active = data.get('is_active', True)

    def fire(self) -> None:
        """Увольнение сотрудника"""

        self.is_active = False

    def hire(self) -> None:
        """Найм сотрудника"""

        self.is_active = True

    def __str__(self) -> str:
        """ Метод для вывода информации о сотруднике

        Returns:
           Информация о сотруднике.
        """

        status = "Работает" if self.is_active else "Уволен"

        return f"{self.employee_id}: {self.name} - {self.position} ({status})"

    def to_dict(self) -> dict:
        """Преобразование в словарь для сохранения.

        Returns:
            Словарь с информацией о сотруднике.
        """

        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'position': self.position,
            'salary': self.salary,
            'is_active': self.is_active
        }
