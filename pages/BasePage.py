from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    title: tuple = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # get an URL in string format and goes there
    def go_to_page(self, url: str) -> None:
        self.driver.get(url)

    # waits for an element then clicks it
    def do_click(self, by_locator: tuple) -> None:
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    # writes some text given as a parameter in a textbox
    def do_send_key(self, by_locator: tuple, txt: str) -> None:
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(txt)

    # do an enter at input locator
    def do_enter(self, by_locator: tuple) -> None:
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    # clear the text from a textbox
    def clear_textbox(self, by_locator: tuple) -> None:
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()

    # waits for an element and returns its text
    def get_text(self, by_locator: tuple) -> str:
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    # prints text for a list of locators
    def print_all_texts(self, by_locator: tuple) -> None:
        all_descriptions = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        for desc in all_descriptions:
            print(desc.text)

    # returns a list with a texts from web locators
    def get_all_texts(self, by_locator: tuple) -> list:
        all_descriptions = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        desc_list = []
        for desc in all_descriptions:
            desc_list.append(desc.text)
        return desc_list
