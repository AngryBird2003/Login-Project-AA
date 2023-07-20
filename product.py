from functions import show_product, show_cart, add_to_cart, update_cart, complete_purchase


class Product:
    def __init__(self, product_data):
        self.product_names = product_data["Product"]
        self.product_quantity = product_data["Quantity"]
        self.product_rates = product_data["Rate"]
        self.cart = product_data["cart"]
        self.order = product_data["order"]

    def product_interface(self):
        amount = 0
        show_product(self.product_names, self.product_quantity, self.product_rates)
        add_to_cart(self.product_names, self.product_quantity, self.product_rates, self.cart, amount, self.order)



