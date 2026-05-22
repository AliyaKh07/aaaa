from ui.console_ui import ConsoleUI


def main() -> None:
    """Основная функция запуска приложения """

    print("=" * 50)
    print("Добро пожаловать в CRM систему!")
    print("=" * 50)

    # Создаем и запускаем интерфейс
    app = ConsoleUI()
    app.run()


if __name__ == "__main__":
    main()