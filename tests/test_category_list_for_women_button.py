from selene import browser, have

from pages.home_page import HomePage

from utils.allure_attach import *

home_page = HomePage()

expected_items_for_tops_level = [
    "Jackets",
    "Hoodies & Sweatshirts",
    "Tees",
    "Bras & Tanks"
]
expected_items_for_bottoms_level = [
    "Pants",
    "Shorts"
]


@allure.tag('web')
@allure.tag('ui')
@allure.title("Тестирование кнопок верхнего меню")
@allure.description("Тестирование раскрывающегося списка категорий при наведении на кнопку")
@allure.link('https://magento.softwaretestingboard.com/', name="Главная страница магазина")
def test_category_list_for_women_button_tops_level():
    with allure.step("Открываем браузер"):
        browser.open('/')

    with allure.step("Принимаем соглашение"):
        home_page.accept_permission_to_process_data().click()

    with allure.step("Раскрываем список категорий для кнопки 'Women'"):
        home_page.list_of_categories_for_women('Women', 'Tops')

    with allure.step("Проверяем доступные подпункты для пункта 'Tops'"):
        all_items = browser.all('//li[contains(@class, "level2")]//span')
        all_items.should(have.texts(*expected_items_for_tops_level))
        add_screenshot(browser)

    with allure.step("Раскрываем список категорий для кнопки 'Women'"):
        home_page.list_of_categories_for_women('Women', 'Bottoms')

    with allure.step("Проверяем доступные подпункты для пункта 'Bottoms'"):
        all_items = browser.all('//li[contains(@class, "level2")]//span')
        all_items.should(have.texts(*expected_items_for_bottoms_level))
