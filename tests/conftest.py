from dotenv import load_dotenv
import os
from selene import browser
import pytest
from selenium import webdriver
from utils.allure_attach import *

# Загрузка переменных окружения из файла .env
load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--selenoid", action="store_true", default=False, help="Run tests on Selenoid"
    )


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    use_selenoid = request.config.getoption("--selenoid")

    if use_selenoid:
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'normal'

        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "127",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            }
        }

        # Получение учетных данных из переменных окружения
        selenoid_user = os.getenv('SELENOID_USER')
        selenoid_password = os.getenv('SELENOID_PASSWORD')
        selenoid_host = os.getenv('SELENOID_HOST')

        driver_options.capabilities.update(selenoid_capabilities)

        selenoid_url = f'https://{selenoid_user}:{selenoid_password}@{selenoid_host}/wd/hub'
        driver = webdriver.Remote(command_executor=selenoid_url, options=driver_options)

        browser.config.driver = driver
    else:
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'normal'
        browser.config.driver = webdriver.Chrome(options=driver_options)

    browser.config.base_url = 'https://magento.softwaretestingboard.com'

    # Изменение масштаба страницы
    # browser.driver.execute_script("document.querySelector('body').style.transform='scale(0.65)';")

    yield browser

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    if use_selenoid:
        add_video_selenoid(browser)

    print("\nТестирование завершено. Закрываем браузер!")
    browser.quit()
