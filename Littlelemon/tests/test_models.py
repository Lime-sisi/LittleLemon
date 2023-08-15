from django.test import TestCase
from restaurant.models import menu


class MenuTest(TestCase):
    def test_addnew_item(self):
        item = menu.objects.create(title = 'icy lime coffee', price = 20,inventory=40)
        item = item.__str__()
      

        self.assertEqual(item, "icy lime coffee : 20")

