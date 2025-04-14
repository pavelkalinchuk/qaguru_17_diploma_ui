from utils.allure_attach import *

from selene import browser, be, have

from pages.home_page import HomePage
from pages.training_page import TrainingPage
from pages.erin_recommends_page import ErinRecommendsPage

home_page = HomePage()
training_page = TrainingPage()
erin_recom_page = ErinRecommendsPage()


@allure.tag("web")
@allure.tag("ui")
@allure.title("Контент на странице 'Training'")
@allure.description("Тестирование ссылки рекомендаций от профессионального тренира Эрин Ренни")
@allure.link('https://magento.softwaretestingboard.com', name="Главная страница магазина")
def test_recommendation_link():
    with allure.step("Открываем браузер"):
        browser.open('/')

    with allure.step("Принимаем соглашение"):
        home_page.accept_permission_to_process_data().click()

    with allure.step("Переходим на страницу Training"):
        home_page.training_page().click()

    with allure.step("Делаем переход на страницу с рекоммендациями от Эрин Ренни"):
        training_page.link_for_recommendations_from_erin_renny().should(be.visible)
        training_page.link_for_recommendations_from_erin_renny().click()

    with allure.step("Убеждаемся в успешном переходе"):
        erin_recom_page.title_page().should(be.visible)

    with allure.step("Убеждаемся в том, что список товаров не пустой"):
        erin_recom_page.list_products().should(have.size_greater_than(0))

