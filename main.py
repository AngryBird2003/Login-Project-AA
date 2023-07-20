from userlogin import UserLogin
from product import Product


class Main:
    def __init__(self):
        self.user = UserLogin(info["user_data"])
        if self.user.login_status:
            product_obj = Product(info["Product_data"])
            product_obj.product_interface()


info = {"id": [1, 2, 3, 4],
        "user_data": [{"user": ["user1", "user2", "user3", "user4"], "password": ["1", "2", "3", "4"]}],
        "Product_data": {"Product": ["product1", "product2", "product3"],
                         "Quantity": [24, 56, 15],
                         "Rate": [2000, 1500, 1800],
                         "cart": [],
                         "order": []
                         }
        }

start = Main()
