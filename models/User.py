from models import enum_usertype




class User:

    def __init__(self, email: str, password: str, firstname: str, lastname: str, address: str,phone_no:str, type_of_user:str, card_details:str, card_pin:str):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phone_no = phone_no
        self.type_of_user = type_of_user
        self.card_details =card_details
        self.card_pin = card_pin
        if type(type_of_user) is enum_usertype.usertype:
            self.type_of_user = type_of_user

class Address:
    def __init__(self,country:str, state:str, local_government_area:str, city:str, street:str):
        self.country = country
        self.state = state
        self.local_government_area = local_government_area
        self.city = city
        self.street = street

class Card_details:
    def __init__(self, card_no:str, pin:str, billing_address:str,card_type:str):
        self.card_no = card_no
        self.card_type = card_type
        self.pin = pin
        self.billing_address = billing_address
        if type(card_type) is enum_usertype.cardtype:
            self.card_type = card_type

class Customer(User):
    def __init__(self, firstname: str, lastname: str, type_of_user: str, card_pin: str, email='', password='',
                 phone_no='', address='', card_details=''):
        super().__init__(email, password, firstname, lastname, address, phone_no, type_of_user, card_details, card_pin)
        self.Address = Address
        self.Card_Details = Card_details




class Merchant(User):
    def __init__(self, password: str, firstname: str, lastname: str, address: str, phone_no: str, type_of_user: str,
                 card_details: str, card_pin: str, email:str, productCat: str):
        super().__init__(email, password, firstname, lastname, address, phone_no, type_of_user, card_details, card_pin, productCat)
        if type(productCat) is enum_usertype.productCat:
            self.productCat = productCat


class Admin(User):
    def __init__(self, firstname: str, lastname: str, type_of_user: str, card_pin: str, email='', password='',
                 phone_no='', address='', card_details=''):
        super().__init__(email, password, firstname, lastname, address, phone_no, type_of_user, card_details, card_pin)
        self.Address = Address
        self.Card_Details = Card_details



