from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class FreeRangeTesterHome(BasePage):

    search_bar: tuple = (By.NAME, "q")

    def __init__(self, driver):
        super(FreeRangeTesterHome,self).__init__(driver)
