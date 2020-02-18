# E-1
[![Travis][build-badge]][build]

[build-badge]: https://img.shields.io/travis/ Artromterra / E-1 /master.png?style=flat-square

[build]: https://travis-ci.org/ Artromterra / E-1

Скачиваем репозиторий, распаковываем.

Переходим в папку и создаем виртуальное окружение.
Для проведения тестов устанавливаем виртуальное окружение используя модули из requirements.txt

командой pip install -r requirements.txt

Запуск теста коммандой: python -m pytest -v --cov=tests  tests/test_pytest.py
