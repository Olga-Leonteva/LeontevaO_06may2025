from selenium.webdriver.common.by import By
from config import URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sibdar_UI:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(URL)
        self._driver.maximize_window()

    # Нажать "Грибная крошка"
    def mushroom_crumble(self):
        crumble = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '[attr_item="Грибная крошка"]')))
        crumble.click()

    # Нажать "Корзина"
    def mushroom_basket(self):
        basket = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '#bask_ic_count')))
        basket.click()

    # Количество товара в корзине
    def amount_product_basket(self):
        a_p = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '#name_product_item_180'))).text
        return a_p

    # Удалить товар из корзины
    def delete_product(self):
        d_product = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.delet_pr_bas')))
        d_product.click()

    # Заголовок пустой корзины
    def empty_cart(self):
        empty = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '#order-list'))).text
        return empty

    # Найти корзину
    def search_cart(self):
        cart = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '#bask_ic_count'))).text
        return cart
