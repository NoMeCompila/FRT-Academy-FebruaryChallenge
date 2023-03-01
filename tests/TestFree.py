import os
import pytest
from tests.conftest import load_data
from pages.FreeRangeTesterHome import FreeRangeTesterHome
from pages.FreeRangeTesterResults import FreeRangeTesterResults
from selenium.webdriver.chrome.webdriver import WebDriver


class TestFree:

    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', r'..\data\search_data.json'))
    data = load_data(data_path)

    @pytest.mark.free_test
    @pytest.mark.parametrize("element", data["search_input"])
    def test_free_range_page(self, init_driver: WebDriver, element: str) -> None:
        free_home = FreeRangeTesterHome(init_driver)
        free_home.go_to_page("https://www.freerangetesters.com/")
        assert "Free" in free_home.get_text(free_home.title)
        free_home.do_send_key(free_home.search_bar, element)
        free_home.do_enter(free_home.search_bar)

        free_results = FreeRangeTesterResults(init_driver)
        assert "Resultados" in free_results.get_text(free_results.title)
        assert all("Selenium" in desc for desc in free_results.get_all_texts(free_results.descriptions))

