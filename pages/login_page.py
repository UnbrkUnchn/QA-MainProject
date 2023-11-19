import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger

"""Страница Авторизации Яндекс Маркета"""


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы(Селекторы)

    login_menu = "div button[data-type='login']"
    login = "input[id='passp-field-login']"
    password = "input[id='passp-field-passwd']"
    sign_in_button = "button[id='passp:sign-in']"
    assert_text = "div a[class='Ft4FS']"

    # Геттеры

    def get_login_menu(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.login_menu)))

    def get_login(self):
        return WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.password)))

    def get_sign_in_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.sign_in_button)))

    def get_assert_text(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.assert_text)))

    # Действия

    def click_login_menu(self):
        self.get_login_menu().click()
        print("Нажатие на Кнопку: 'Почта'")

    def input_login(self, email):
        self.get_login().send_keys(email)
        print(f"Ввод Логина: {email}")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print(f"Ввод Пароля: {password}")

    def click_sign_in_button(self):
        self.get_sign_in_button().click()
        print("Нажатие на Кнопку: 'Вход'")

    # Методы

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.click_login_menu()
            self.input_login("***")  # ЛОГИН ДЛЯ ВХОДА
            self.click_sign_in_button()
            self.input_password("***")  # ПАРОЛЬ ДЛЯ ВХОДА
            self.click_sign_in_button()
            self.assert_word(self.get_assert_text(), result="ЯНДЕКС")  # Сравнение по полю в футере Я.Маркета
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
