import allure
from selene import browser

from pages.cart_page import Cart
from pages.home_page import HomePage
from pages.men_page import MenPage
from pages.product_page import ProductPage

home_page = HomePage()
men_page = MenPage()
product_page = ProductPage()
cart = Cart()


@allure.tag('web')
@allure.tag('ui')
@allure.title("Покупка мужской одежды")
@allure.description("Тестирование покупки мужского худи")
@allure.link('https://magento.softwaretestingboard.com/', name="Главная страница магазина")
def test_buying_hoodies():
    with allure.step("Открываем браузер"):
        browser.open('/')

    with allure.step("Принимаем соглашение"):
        home_page.accept_permission_to_process_data().click()

    with allure.step("Открываем страницу с товарами для мужчин"):
        men_page.open_men_page()

    with allure.step("Открываем раздел 'Худи и Свитшоты'"):
        men_page.hoodies_and_sweatshirts_for_men().click()

    with allure.step("Находим худи с названием 'Marco Lightweight Active Hoodie' и открываем карточку товара"):
        product_page.product('marco-lightweight-active-hoodie').click()

    with allure.step("Выбираем размер товара"):
        product_page.select_size('M').click()

    with allure.step("Выбираем цвет товара"):
        product_page.select_color('Green').click()

    with allure.step("Добавляем товар в карзину"):
        product_page.add_to_cart().click()

    with allure.step("Проверяем вывод сообщения об успешном добавлении товара в карзину"):
        product_page.should_be_message_added_cart_product('Marco Lightweight Active Hoodie')

    with allure.step("Открываем карзину"):
        cart.open_cart().click()

    with allure.step("Проверяем, что в карзине находится выбраный товар с выбранными размером и цветом"):
        cart.product_name('Marco Lightweight Active Hoodie')
        cart.product_details('M', 'Green')
