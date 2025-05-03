import curl
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    driver = webdriver.Chrome(options=options)
    driver.get(curl.MAIN)
    yield driver
    driver.quit()


