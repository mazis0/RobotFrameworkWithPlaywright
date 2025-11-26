class CartPage:
    def __init__(self, page):
        self.page = page

    def click_checkout(self):
        self.page.click("#checkout")
