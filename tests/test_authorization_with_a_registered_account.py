import json
import os

from allure_attach import *

from selene import browser, have, be

from pages.home_page import HomePage
from pages.authorization_page import AuthorizationPage

home_page = HomePage()
auth_page = AuthorizationPage()

# Получаем абсолютный путь к корневому каталогу проекта
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def load_user_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)[-1]  # Загружаем последнего зарегистрированного пользователя из файла


@allure.tag('web')
@allure.tag('ui')
@allure.title('Авторизация ранее зарегистрированного пользователя')
@allure.description('Тестируем авторизацию зарегистрировнного пользователя в магазине')
@allure.link('https://magento.softwaretestingboard.com', name="Главная страница магазина")
def test_create_new_account():
    with allure.step('Открываем браузер'):
        browser.open('/')

    with allure.step('Принимаем соглашение'):
        home_page.accept_permission_to_process_data().click()

    with allure.step('Переходим на страницу авторизации пользователя'):
        home_page.link_for_authorization().click()
        browser.element('[data-ui-id="page-title-wrapper"]').should(be.visible)

    with allure.step('Загружаем данные пользователя из файла'):
        user_data = load_user_data(os.path.join(project_dir, 'utils', 'user_data.json'))

    with allure.step('Заполняем поле "Email"'):
        auth_page.email_input_field().type(user_data["Email"])

    with allure.step('Заполняем поле "Password"'):
        auth_page.password_input_field().type(user_data["Password"])

    with allure.step('Кликаем на кнопке "Sing in"'):
        auth_page.button_for_authorization().click()

    with allure.step('Проверяем, что авторизация успешно выполнена'):
        home_page.user_is_authorized().should(be.visible)
        home_page.user_is_authorized().should(have.text(user_data["First Name"]))
        home_page.user_is_authorized().should(have.text(user_data["Last Name"]))