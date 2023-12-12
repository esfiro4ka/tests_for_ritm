# Описание проекта
Этот репозиторий содержит тесты, покрывающие различные эндпоинты на сайте [https://reqres.in/](https://reqres.in/). Тесты написаны с использованием библиотек pytest и requests.

# Установка
Склонируйте данный репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/esfiro4ka/tests_for_ritm.git
```

Перейдите в директорию с проектом:

```bash
cd tests_for_ritm
```

Создайте и активируйте виртуальное окружение. Например, для Linux или macOS:

```bash
python3 -m venv venv

source venv/bin/activate
```

Установите зависимости, выполнив следующую команду:

```bash
pip install -r requirements.txt
```

# Запуск тестов
Для запуска тестов перейдите в директорию `tests/`:

```bash
cd tests
```

Выполните команду для запуска всех тестов:

```bash
pytest
```

Или для запуска какого-либо из тестов. Например:


```bash
pytest test_1_list_users.py
```
