class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_product(self, product):
        self.page.click(f"text={product}")

    def go_to_cart(self):
        self.page.click("#shopping_cart_container a")
