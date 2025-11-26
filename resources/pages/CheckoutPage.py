class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_info(self, first, last, zip):
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", zip)

    def continue_checkout(self):
        self.page.click("#continue")

    def finish_checkout(self):
        self.page.click("#finish")

    def assert_success(self):
        self.page.wait_for_selector("text=THANK YOU FOR YOUR ORDER", timeout=5000)

        success_text = self.page.inner_text("h2.complete-header")

        if "Thank you for your order!" not in success_text:
            raise AssertionError(
                f"Checkout FAILED. Expected confirmation text not found. Got: {success_text}"
            )

        if "checkout-complete" not in self.page.url:
            raise AssertionError(
                f"Unexpected URL after checkout: {self.page.url}"
            )

        assert self.page.is_visible(".complete-text"), \
            "Order completion message container not visible"

        print(">>> CHECKOUT SUCCESS VERIFIED")

