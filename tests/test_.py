import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage


"""Тест Основной Бизнес Логики Магазина YandexMarket - Покупка Товара: Ноутбук из категории: Ноутбуки"""


@pytest.mark.run(order=1)
@allure.description("Test Buy Product 1")
def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()

    """Открытие браузера на Главной странице Яндекс.Маркета и последующее Открытие страницы Авторизации"""

    mp = MainPage(driver)
    mp.start_test()
    mp.login_page()

    """Выполнение процедуры Авторизации в Яндекс.Маркете с помощью валидных данных"""

    lp = LoginPage(driver)
    lp.authorization()

    """Выбор категории желаемого к покупке Товара: Ноутбуки"""

    mp.type_product()

    """Выбор Товара из категории: Ноутбуки"""

    catalog_p = CatalogPage(driver)
    catalog_p.choosing_product()

    """Выполнение процедуры покупки выбранного Товара: Ноутбука"""

    cart_p = CartPage(driver)
    cart_p.buy_product()

    """Конец выполнения теста"""

    driver.quit()
