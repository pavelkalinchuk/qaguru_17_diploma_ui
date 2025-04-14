import allure
from selene import browser

from pages.cart_page import Cart
from pages.home_page import HomePage
from pages.women_page import WomenPage
from pages.product_page import ProductPage

home_page = HomePage()
women_page = WomenPage()
product_page = ProductPage()
cart = Cart()


@allure.tag('web')
@allure.tag('ui')
@allure.title("Покупка женской одежды")
@allure.description("Тестирование покупки женского свитшота")
@allure.link('https://magento.softwaretestingboard.com/', name="Главная страница магазина")
def test_buying_hoodies():
    with allure.step("Открываем браузер"):
        browser.open('/')

    with allure.step("Принимаем соглашение"):
        home_page.accept_permission_to_process_data().click()

    with allure.step("Открываем страницу с товарами для женщин"):
        women_page.open_women_page()

    with allure.step("Открываем раздел 'Худи и Свитшоты'"):
        women_page.hoodies_and_sweatshirts_for_women().click()

    with allure.step("Находим худи с названием 'Cassia Funnel Sweatshirt' и открываем карточку товара"):
        product_page.product('cassia-funnel-sweatshirt').click()

    with allure.step("Выбираем размер товара"):
        product_page.select_size('S').click()

    with allure.step("Выбираем цвет товара"):
        product_page.select_color('Purple').click()

    with allure.step("Добавляем товар в карзину"):
        product_page.add_to_cart().click()

    with allure.step("Проверяем вывод сообщения об успешном добавлении товара в карзину"):
        product_page.should_be_message_added_cart_product('Cassia Funnel Sweatshirt')

    with allure.step("Открываем карзину"):
        cart.open_cart().click()

    with allure.step("Проверяем, что в карзине находится выбраный товар с выбранными размером и цветом"):
        cart.product_name('Cassia Funnel Sweatshirt')
        cart.product_details('S', 'Purple')
