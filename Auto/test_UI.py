import allure
import pytest
from sibdar_UI import Sibdar_UI


@allure.epic("UI")
@allure.title("Добавить товар в корзину")
@pytest.mark.ui
@pytest.mark.smoke
def test_amount_product(browser):
    with allure.step("Открыть браузер"):
        m_c = Sibdar_UI(browser)

    with allure.step("Добавить продукт"):
        m_c.mushroom_crumble()

    with allure.step("Открыть корзину"):
        m_c.mushroom_basket()

    with allure.step("Проверить наличие товара в корзине"):
        a_p = m_c.amount_product_basket()

    with allure.step("Проверить корзину"):
        assert a_p == ('Грибная крошка')


@allure.epic("UI")
@allure.title("Удалить товар из корзины")
@pytest.mark.ui
@pytest.mark.smoke
def test_delete_product(browser):
    with allure.step("Открыть браузер"):
        m_c = Sibdar_UI(browser)

    with allure.step("Добавить продукт"):
        m_c.mushroom_crumble()

    with allure.step("Открыть корзину"):
        m_c.mushroom_basket()

    with allure.step("Удалить товар из корзины"):
        m_c.delete_product()

    with allure.step("Найти заголовок"):
        empty = m_c.empty_cart()

    with allure.step("Проверить заголовок"):
        assert empty == ('Корзина пуста, необходимо это исправить')


@allure.epic("UI")
@allure.title("При открытии страницы сайта, корзина пуста")
@pytest.mark.ui
@pytest.mark.smoke
def test_Cart(browser):
    with allure.step("Открыть браузер"):
        m_c = Sibdar_UI(browser)

    with allure.step("Найти корзину"):
        text = m_c.search_cart()

    with allure.step("Проверить значение"):
        assert text == ('пуста')
