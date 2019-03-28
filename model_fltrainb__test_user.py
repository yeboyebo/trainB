import unittest

from models.fltrainb.user import user as User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.get(iduser='1')

    def test_name_prop(self):
        print("\nComprobando nombre: " + self.user.name + ", " + "Iván\n")
        self.assertEqual(self.user.name, "Iván")
        print("Comprobando Email \n")
        self.assertEqual(self.user.email, "ivan@yeboyebo.es")

    def test_rol(self):
        print("Comprobando rol\n")
        self.assertEqual(self.user.rol, "Developer")
