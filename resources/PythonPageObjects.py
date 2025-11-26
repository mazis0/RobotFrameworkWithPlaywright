import sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from playwright.sync_api import sync_playwright
import allure

class PythonPageObjects:

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.browser=None
        self.page=None
        self.pw=None

    def open_browser(self):
        self.pw = sync_playwright().start()
        self.browser = self.pw.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def close_browser(self):
        if self.browser:
            self.browser.close()
        if self.pw:
            self.pw.stop()

    # BDD KEYWORDS (embedded args)
    def given_user_open_saucedemo_login_page(self):
        self.page.goto("https://www.saucedemo.com")

    def when_user_login_with(self, username, password):
        LoginPage(self.page).login(username, password)

    def user_adds_product(self, product):
        InventoryPage(self.page).add_product(product)

    def user_go_to_cart(self):
        InventoryPage(self.page).go_to_cart()

    def user_checkout_with(self, first, last, zip):
        cart = CartPage(self.page)
        cart.click_checkout()
        checkout = CheckoutPage(self.page)
        checkout.fill_info(first, last, zip)
        checkout.continue_checkout()
        checkout.finish_checkout()

    def checkout_should_be_successful(self):
        CheckoutPage(self.page).assert_success()

    def capture_failure_screenshot(self, status):
        if status.upper()=="FAIL" and self.page:
            allure.attach(self.page.screenshot(), "failure", allure.attachment_type.PNG)
