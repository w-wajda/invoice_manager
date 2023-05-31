from django.test import TestCase
from django.urls import reverse

from currencies.factories import CurrencyFactory
from users.factories import UserFactory


class TestCurrency(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.user.set_password("test")
        self.user.save()
        self.user_currencies = CurrencyFactory.create_batch(12, user=self.user)
        self.other_currency = CurrencyFactory()


class TestListCurrencies(TestCurrency):
    def setUp(self) -> None:
        super().setUp()
        self.url = reverse("currencies:list_currencies")

    def test_list_currencies_if_not_logged(self):
        response = self.client.get(self.url, follow=True)

        self.assertRedirects(response, f"/users/login/?next={self.url}")

    def test_list_currencies_if_logged(self):
        self.client.login(username=self.user.username, password="test")
        response = self.client.get(self.url)

        object_list = response.context["currencies"]

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "currencies/list_currencies.html")
        self.assertTrue(len(object_list) == 10)
        self.assertListEqual(list(object_list), self.user_currencies[:10])

    def test_list_currencies_second_pag(self):
        self.client.login(username=self.user.username, password="test")
        response = self.client.get(f"{self.url}?page=2")

        object_list = response.context["currencies"]

        self.assertTrue(len(object_list) == 2)
        self.assertListEqual(list(object_list), self.user_currencies[10:])


class TestDeleteCurrency(TestCurrency):
    def setUp(self) -> None:
        super().setUp()
        self.currency = self.user_currencies[0]
        self.url = reverse("currencies:delete_currency", args=[self.currency.pk])

    def test_delete_currency_if_not_logged(self):
        response = self.client.get(self.url, follow=True)

        self.assertRedirects(response, f"/users/login/?next={self.url}")

    def test_delete_country_if_logged(self):
        self.client.login(username=self.user.username, password="test")

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def rest_return_404_if_not_my_countries(self):
        url = reverse("countries:delete_country", args=[self.other_currency.pk])
        self.client.login(username=self.user.username, password="test")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
