import allure
from selene import browser

from pages.cart_page import Cart
from pages.home_page import HomePage
from pages.gear_page import GearPage
from pages.product_page import ProductPage

home_page = HomePage()
gear_page = GearPage()
product_page = ProductPage()
cart = Cart()


@allure.tag('web')
@allure.tag('ui')
@allure.title("Покупка снаряжения")
@allure.description("Тестирование покупки сумки для снаряжения")
@allure.link('https://magento.softwaretestingboard.com/', name="Главная страница магазина")
def test_buying_hoodies():
    with allure.step("Открываем браузер"):
        browser.open('/')

    with allure.step("Принимаем соглашение"):
        home_page.accept_permission_to_process_data().click()

    with allure.step("Открываем страницу со снаряжением"):
        gear_page.open_gear_page()

    with allure.step("Открываем раздел 'Сумки'"):
        gear_page.bags_list().click()

    with allure.step("Находим сумку с названием 'Endeavor Daytrip Backpack' и открываем карточку товара"):
        product_page.product('endeavor-daytrip-backpack').click()

    with allure.step("Добавляем товар в карзину"):
        product_page.add_to_cart().click()

    with allure.step("Проверяем вывод сообщения об успешном добавлении товара в карзину"):
        product_page.should_be_message_added_cart_product("Endeavor Daytrip Backpack")

    with allure.step("Открываем карзину"):
        cart.open_cart().click()

    with allure.step("Проверяем, что в карзине находится выбранная сумка"):
        cart.product_name('Endeavor Daytrip Backpack')
