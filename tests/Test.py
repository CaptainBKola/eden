import unittest

from models.User import User


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.User = User("Okanynuel@gmail.com","okany123","Okany","Onyeka","sabo_Yaba","08060306819","Customer", "900889676985","9856")

    def test__User_email(self):
        user = User("Okanynuel@gmail.com","okany123","Okany","Onyeka","sabo_Yaba","08060306819","Customer","0888867558748","9856")
        self.assertIsNotNone(user.email)
        self.assertEquals("Okanynuel@gmail.com", user.email)

    def test__User_password(self):
        user = User("Okanynuel@gmail.com", "okany123", "Okany", "Onyeka", "sabo_Yaba", "08060306819", "Customer", "900889676985","9856")
        self.assertIsNotNone(user.password)
        self.assertEquals("okany123",user.password)

    def test__User_firstname(self):
        user = User("Okanynuel@gmail.com", "okany123", "Okany", "Onyeka", "sabo_Yaba", "08060306819", "Customer","900889676985","9856")
        self.assertIsNotNone(user.firstname)
        self.assertEquals("Okany",user.firstname)

    def test__User_lastname(self):
        user = User("Okanynuel@gmail.com", "okany123", "Okany", "Onyeka", "sabo_Yaba", "08060306819", "Customer","900889676985","9856")
        self.assertIsNotNone(user.lastname)
        self.assertEquals("Onyeka",user.lastname)

    def test__user_address(self):
        user = User("Okanynuel@gmail.com", "okany123", "Okany", "Onyeka", "sabo", "08060306819", "Customer","900889676985","9856")
        self.assertIsNotNone(user.address)
        self.assertEquals("sabo",user.address)

    def test__User_phone_no(self):
        user = User("Okanynuel@gmail.com", "okany123", "Okany", "Onyeka", "sabo_Yaba", "08060306819", "Customer", "900889676985","9856")
        self.assertIsNotNone(user.phone_no)
        self.assertEquals("08060306819",user.phone_no)

    def test__Usertype(self):
        user = User("Okanynuel@gmail.com", "okany123", "Okany", "Onyeka", "sabo_Yaba", "08060306819", "Customer","900889676985","9856")
        self.assertIsNotNone(user.type_of_user)
        self.assertEquals("Customer",user.type_of_user)



if __name__ == '__main__':
    unittest.main()
