import allure

from pages.cart_page import Cart
from pages.home_page import HomePage
from pages.men_page import ManPage
from pages.product_page import ProductPage

home_page = HomePage()
man_page = ManPage()
product_page = ProductPage()
cart = Cart()


def test_buying_hoodies():
    with allure.step('Открываем домашнюю страницу магазина'):
        home_page.accept_permission_to_process_data().click()

    with allure.step('Открываем страницу с товарами для мужчин'):
        man_page.open_page()

    with allure.step('Открываем раздел "Худи и Свитшоты"'):
        man_page.hoodies_and_sweatshirts().click()

    with allure.step('Находим худи с названием "Marco Lightweight Active Hoodie" и открываем карточку товара'):
        product_page.product('marco-lightweight-active-hoodie').click()

    with allure.step('Выбираем размер товара'):
        product_page.select_size('M').click()

    with allure.step('Выбираем цвет товара'):
        product_page.select_color('Green').click()

    with allure.step('Добавляем товар в карзину'):
        product_page.add_to_cart().click()

    with allure.step('Проверяем вывод сообщения об успешном добавлении товара в карзину'):
        product_page.should_be_message_added_cart_product('Marco Lightweight Active Hoodie')

    with allure.step('Открываем карзину'):
        cart.open_cart().click()

    with allure.step('Проверяем, что в карзине находится выбраный товар с выбранными размером и цветом'):
        cart.product_name('Marco Lightweight Active Hoodie')
        cart.product_details('M', 'Green')
