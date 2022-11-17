from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from faker import Factory

from web.tests.factories import JournalFactory

User = get_user_model()
faker = Factory.create()


class JournalViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username=faker.user_name(), password=faker.password())
        self.client.login(username=self.user.username, password=faker.password())
        self.journal = JournalFactory.create(user=self.user)

    def test_journal_list_view(self):
        response = self.client.get(reverse("web:journal_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "web/journal_list.html")

    def test_journal_create_view(self):
        response = self.client.get(reverse("web:journal_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/add.html")

    def test_journal_update_view(self):
        response = self.client.get(reverse("web:journal_update", kwargs={"pk": self.journal.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/update.html")

    def test_journal_delete_view(self):
        response = self.client.get(reverse("web:journal_delete", kwargs={"pk": self.journal.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "common/delete.html")
