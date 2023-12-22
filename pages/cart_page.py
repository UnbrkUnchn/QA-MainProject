import allure

from base.base_class import Base
from utilities.logger import Logger


"""Страница Корзины Яндекс Маркета"""


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def buy_product(self):
        with allure.step("Buy Product"):
            Logger.add_start_step(method="buy_product")
            self.get_current_url()
            self.assert_url("https://market.yandex.ru/my/cart")
            self.get_screenshot()
            print("Ноутбук куплен(Условно)")
            print("Тест успешно завершён!")
            Logger.add_end_step(url=self.driver.current_url, method="buy_product")
