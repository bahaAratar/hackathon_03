from django.test import TestCase
from account.models import MyUser

class MyUserTestCase(TestCase):
    def test_create_myuser(self):
        user = MyUser.objects.create(name='Erika',last_name = 'Omorbekova')
        self.assertEqual(user.name, 'Erika')
        self.assertEqual(user.last_name, 'Omorbekova')

    def test_update_myuser(self):
        user = MyUser.objects.delete(name ='Erik',last_name = 'Omorbekov')
        user.name = 'Kitten Food'
        user.save()
        self.assertEqual(user.name, 'Kitten Food')
    def test_delete_product(self):
        user = MyUser.objects.create(name = 'Erka', last_name= 'omorbekova')
        user.delete()
        self.assertFalse(MyUser.objects.filter(name='Erka').exstis())
