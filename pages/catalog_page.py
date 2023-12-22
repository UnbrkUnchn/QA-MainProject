import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


"""Страница Каталога Яндекс Маркета"""


class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)

    # Локаторы(Селекторы)

    filtres_btn = "[data-auto='allFiltersButton'] button"  # Все Фильтры
    min_price = "[id='glprice'] input[data-auto='range-filter-input-min']"  # Минимальная Цена
    max_price = "[id='glprice'] input[data-auto='range-filter-input-max']"  # Максимальная Цена
    # dd_ram = "div[data-filter-id='15938685'] button"  # Ниспадающее меню Кнопки
    # ram = "div label[id='15938699']"  # Оперативная Память
    notebook_name = "div label[id='152981']"  # Наименование Ноутбука
    # dd_nb_series = "div[data-filter-id='12782797'] button"  # Ниспадающее меню Кнопки
    # notebook_series = "div label[id='16100292']"  # Линейка
    dd_resolution = "div[data-filter-id='14806501'] button"  # Ниспадающее меню Кнопки
    resolution = "div label[id='36763152']"  # Разрешение Экрана
    dd_fresh_rate = "div[data-filter-id='16499888'] button"  # Ниспадающее меню Кнопки
    fresh_rate = "div label[id='37513490']"  # Частота Обновления Экрана
    # dd_cpu = "div[data-filter-id='6069383'] button"  # Ниспадающее меню Кнопки
    # cpu = "div label[id='22389489']"  # Процессор
    # dd_cpu_cores = "div[data-filter-id='34814810'] button"  # Ниспадающее меню Кнопки
    # cpu_cores = "div label[id='35692085']"  # Количество Ядер Процессора
    dd_ssd = "div[data-filter-id='37699290'] button"  # Ниспадающее меню Кнопки
    ssd = "div label[id='39025848']"  # Общий объём накопителей SSD
    dd_condition = "div[data-filter-id='resale_goods'] button"  # Ниспадающее меню Кнопки
    condition = "div label[id='resale_new']"  # Состояние Товара
    # dd_gpu = "div[data-filter-id='36036031'] button"  # Ниспадающее меню Кнопки
    # gpu = "div label[id='36427132']"  # Видеокарта
    # dd_vram = "div[data-filter-id='17322770'] button"  # Ниспадающее меню Кнопки
    # vram = "div label[id='17324210']"  # Видеопамять
    show_btn = "div a[class='_2qvOO _3qN-v _1Rc6L']"  # Показать предложения
    add_notebook = "button[class*='390_8 _3Nc4D _2CQi1 pvpsJ _3hX']"  # селектор работает на 2 элемента
    cart = "[data-zone-name='bypassToCheckout'] button"  # Купить сейчас. Перейти в Корзину

    # Геттеры

    def get_filtres_btn(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.filtres_btn)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.max_price)))

    def get_notebook_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.notebook_name)))

    def get_dd_resolution(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.dd_resolution)))

    def get_resolution(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.resolution)))

    def get_dd_fresh_rate(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.dd_fresh_rate)))

    def get_fresh_rate(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.fresh_rate)))

    def get_dd_ssd(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.dd_ssd)))

    def get_ssd(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.ssd)))

    def get_dd_condition(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.dd_condition)))

    def get_condition(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.condition)))

    def get_show_btn(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.show_btn)))

    def get_add_notebook(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.add_notebook)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.cart)))

    # Методы

    def click_all_filtres_btn(self):
        self.get_filtres_btn().click()
        print("Нажатие на Кнопку: 'Все фильтры'")
        self.driver.refresh()
        print("Нажатие на Кнопку: 'Обновить Страницу'")

    def input_min_price(self, min_price):
        self.get_min_price().click()
        self.get_min_price().send_keys(min_price)
        print(f"Ввод: {min_price}")

    def input_max_price(self, max_price):
        self.get_max_price().click()
        self.get_max_price().send_keys(max_price)
        print(f"Ввод: {max_price}")

    def click_notebook_name(self):
        self.get_notebook_name().click()

    def click_dd_resolution(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_resolution())
        self.get_dd_resolution().click()

    def click_resolution(self):
        self.get_resolution().click()

    def click_dd_fresh_rate(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_fresh_rate())
        self.get_dd_fresh_rate().click()

    def click_fresh_rate(self):
        self.get_fresh_rate().click()

    def click_dd_ssd(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_ssd())
        self.get_dd_ssd().click()

    def click_ssd(self):
        self.get_ssd().click()

    def click_dd_condition(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_condition())
        self.get_dd_condition().click()

    def click_condition(self):
        self.get_condition().click()

    def click_show_btn(self):
        self.get_show_btn().click()

    def click_add_notebook(self):
        self.get_add_notebook().click()

    def click_cart(self):
        self.get_cart().click()

    # Действия

    def choosing_product(self):
        with allure.step("Choosing_product"):
            Logger.add_start_step(method="authorization")
            self.click_all_filtres_btn()
            self.input_min_price("150000")
            self.input_max_price("200000")
            self.click_notebook_name()
            self.click_dd_resolution()
            self.click_resolution()
            self.click_dd_fresh_rate()
            self.click_fresh_rate()
            self.click_dd_ssd()
            self.click_ssd()
            self.click_dd_condition()
            self.click_condition()
            self.click_show_btn()
            self.click_add_notebook()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="Choosing_product")
