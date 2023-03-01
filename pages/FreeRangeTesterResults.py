from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class FreeRangeTesterResults(BasePage):

    descriptions: tuple = (By.XPATH, "//p[@class='s__55ZJ6G']")

    def __init__(self, driver):
        super(FreeRangeTesterResults, self).__init__(driver)
