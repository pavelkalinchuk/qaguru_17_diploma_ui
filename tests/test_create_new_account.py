import json
import os
import time

import allure
from allure_attach import *

from selene import browser, have, be, by

from pages.home_page import HomePage
from pages.new_account_page import NewAccountPage
from utils.user_date_gen import generate_user_data

home_page = HomePage()
new_account_page = NewAccountPage()

# Получаем абсолютный путь к корневому каталогу проекта
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def load_user_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)[0]  # Загружаем первого пользователя из файла


@allure.tag('web')
@allure.title('Регистрация нового пользователя')
@allure.description('Тестирование регистрации нового пользователя в магазине')
@allure.link('https://magento.softwaretestingboard.com', name="Главная страница магазина")
def test_create_new_account():
    with allure.step('Открываем браузер'):
        browser.open('/')

    with allure.step('Принимаем соглашение'):
        home_page.accept_permission_to_process_data().click()

    with allure.step('Переходим на страницу создания нового пользователя'):
        new_account_page.open_create_new_account_page()
        browser.element('.base').should(have.text("Create New Customer Account"))

    with allure.step('Создаём данные для регистрации тестового пользователя'):
        generate_user_data(1)

    with allure.step('Загружаем данные пользователя из файла'):
        user_data = load_user_data(os.path.join(project_dir, 'utils', 'user_data.json'))

    with allure.step('Заполняем поле "First name"'):
        new_account_page.first_name_field().type(user_data["First Name"])

    with allure.step('Заполняем поле "Last name"'):
        new_account_page.last_name_field().type(user_data["Last Name"])

    with allure.step('Заполняем поле "Email"'):
        new_account_page.email_field().type(user_data["Email"])

    with allure.step('Заполняем поле "Password"'):
        new_account_page.password_field().type(user_data["Password"])

    with allure.step('Заполняем поле "Confirm Password"'):
        new_account_page.confirm_password_field().type(user_data["Password"])

    with allure.step('Кликаем на кнопке создания аккаунта с введёнными данными'):
        new_account_page.button_for_create_account().should(be.visible)
        new_account_page.button_for_create_account().click()
        add_screenshot(browser)

    with allure.step('Проверяем появление сообщения об успешной регистрации'):
        element = browser.element(by.text('Thank you for registering with Main Website Store.'))
        assert element.matching(be.visible), "Element is not visible on the page"

    with allure.step('Проверяем, что пользователь создался с корректными данными'):
        box_content = browser.element('.box-content')
        box_content.should(have.text(user_data["First Name"]))
        box_content.should(have.text(user_data["Last Name"]))
        box_content.should(have.text(user_data["Email"]))
