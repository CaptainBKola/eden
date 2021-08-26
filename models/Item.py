from models import enum_usertype


class Item:
    def __init__(self, quantity:str, productCat:str,product_price: str):
        self.quantity = quantity
        self.type_of_product = productCat
        self.product_price = product_price
        if type(productCat) is enum_usertype.usertype:
            self.type_of_user = productCat
