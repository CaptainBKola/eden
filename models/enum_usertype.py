import enum


class usertype(enum.Enum):
       Customer = 1
       Merchant = 2
       Admin = 3

class cardtype(enum.Enum):
       Master = 1
       Visa = 2
       Verve= 3

class productCat(enum.Enum):
       Fashion = 1
       Phone = 2
       Kitchen_Utensils=3
       Sports_Kit = 4
       Electronics = 5

