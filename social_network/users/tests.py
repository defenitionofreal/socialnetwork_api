from django.test import TestCase
from users.models import User


class UserTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123', first_name='Tester', last_name='Tester', email='test@mail.ru')
        testuser1.save()

