from rest_framework.test import APITestCase
from .models import UserInfo

class UserAPITestCase(APITestCase):
    """Testing the UserInfo Api.."""
    def setUp(self):
        """It executes before all the test methods execution"""
        UserInfo.objects.create(id=1, first_name='Clarivate',
                                last_name='Analytics',email='clarivate@analytics.com')

    def test_get_method(self):
        """This method can get UserInfo.."""
        url = 'http://127.0.0.1:8000/api/'
        response = self.client.get(url)
        print("Get method status code: ",response.status_code)
        self.assertEqual(response.status_code, 200)
        qs = UserInfo.objects.filter(first_name='Clarivate')
        self.assertEqual(qs.count(),1)

    def test_post_method_success(self):
        """This method can post data of the User"""
        url = 'http://127.0.0.1:8000/api/'
        data = {'id':8,'first_name': 'Roman', 'last_name':'Clarivate', 'email':'roman@gmail.com'}
        response = self.client.post(url, data, format='json')
        print("Post method status code for success: ", response.status_code)
        self.assertEqual(response.status_code, 201)

    def test_post_method_fail(self):
        """This method checks for failure of incomplete User details."""
        url = 'http://127.0.0.1:8000/api/'
        data = {'first_name': 'DabApps', 'email':'dummy@gmail.com'}
        response = self.client.post(url, data, format='json')
        print("Post method status code for failure: ", response.status_code)
        self.assertEqual(response.status_code, 400)

    def test_delete_method(self):
        """Verifies the user info is deleted."""
        url = 'http://127.0.0.1:8000/api/1/'
        response = self.client.delete(url)
        print("Delete method status code: ", response.status_code)
        self.assertEqual(response.status_code, 204)







