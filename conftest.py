import pytest


@pytest.fixture()
def set_up():
    print("Начало Теста")
    yield
    print("Конец Теста")


@pytest.fixture(scope="module")
def set_group():
    print("Вход в Систему")
    yield
    print("Выход из Системы")
