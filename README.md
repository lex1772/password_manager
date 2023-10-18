# Менеджер паролей
Сформирован менеджер паролей с методами GET и POST. Пароль хранится в бд, привязанный к имени сервиса, который указывается при создании пароля.

:white_check_mark: Создано веб-приложение, с API интерфейсом.

:white_check_mark: База данных запускается как Docker контейнер.

:white_check_mark: Проект запускается через Docker-compose.

:white_check_mark: Код покрыт тестами.

Стек технологий:

- Django Rest Framework
- PostgreSQL
- Flake8
- Unittest
- coverage
- python-dotenv
- cryptography

### Начало работы
1. Заполнить .env файл в соответствии с .env_sample
2. Создать образ с помощью команды `docker-compose build`
3. Запустить контейнеры с помощью команды `docker-compose up`
4. Открыть postman и в workspace вставить в строку адрес `http://localhost:8000/password/`

### Примеры запросов к API
POST /password/{service_name} - создаем пароль/заменяем существующий пароль

GET /password/{service_name} - получить пароль по имени сервиса

GET /password/?service_name={part_of_service_name} - провести поиск по
part_of_service_name и выдать пароли с подходящими service_name
