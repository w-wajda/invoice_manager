from django.test import TestCase
from django.urls import reverse

from countries.factories import CountryFactory
from users.factories import UserFactory


class TestCountry(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.user.set_password("test")
        self.user.save()
        self.user_countries = CountryFactory.create_batch(12, user=self.user)
        self.user_country = CountryFactory()

    def test_list_countries_if_not_logged(self):
        url = reverse("countries:list_countries")
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, "/users/login/?next=/countries/")

    def test_list_countries_if_logged(self):
        url = reverse("countries:list_countries")
        self.client.login(username=self.user.username, password="test")
        response = self.client.get(url)

        object_list = response.context["countries"]

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "countries/list_countries.html")
        self.assertTrue(len(object_list) == 10)
        self.assertListEqual(list(object_list), self.user_countries[:10])

    def test_list_countries_second_pag(self):
        url = reverse("countries:list_countries")
        self.client.login(username=self.user.username, password="test")
        response = self.client.get(f"{url}?page=2")

        object_list = response.context["countries"]

        self.assertTrue(len(object_list) == 2)
        self.assertListEqual(list(object_list), self.user_countries[10:])

    # def test_call_view_fail_blank(self):
    #     self.client.login(username='user', password='test')
    #     response = self.client.post('/url/to/view', {}) # blank data dictionary
    #     self.assertFormError(response, 'form', 'some_field', 'This field is required.')
    #     # etc. ...
    #
    # def test_call_view_fail_invalid(self):
    #     # as above, but with invalid rather than blank data in dictionary
    #
    # def test_call_view_success_invalid(self):
    #     # same again, but with valid data, then
    #     self.assertRedirects(response, '/contact/1/calls/')
