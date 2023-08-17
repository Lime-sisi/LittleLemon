from django.test import RequestFactory, TestCase
from restaurant.models import menu
from restaurant.views import MenuItemView


class MenuViewTest(TestCase):
    def setUp(self):
        #access to request factory
        self.factory = RequestFactory()
        menu.objects.create(title='sugar cloud',price = 4.2,inventory=14)
        menu.objects.create(title='strawberry hot chocolate',price = 9.2,inventory=30)

    def test_getall(self):
        request = self.factory.get("/restaurant/menu")
        response = MenuItemView.as_view()(request)
    
        self.assertEqual(response.status_code, 200)

        