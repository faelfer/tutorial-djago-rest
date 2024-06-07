from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.request import Request
from snippets.models import Snippet
from django.contrib.auth.models import User
from .serializers import SnippetSerializer, UserSerializer
import logging

logger = logging.getLogger(__name__)


class GetAllSnippetTest(APITestCase):
    def setUp(self):
        Snippet.objects.create(title="title01", code="code01")
        Snippet.objects.create(title="title02", code="code02")
        Snippet.objects.create(title="title03", code="code03")

    def test_get_all_snippet(self):
        url = "/snippets/"
        response = self.client.get(url, format="json")
        factory = APIRequestFactory()
        request = factory.get("/")
        snippets = Snippet.objects.all()
        serializer_context = {
            "request": Request(request),
        }
        serializer = SnippetSerializer(
            instance=snippets, context=serializer_context, many=True
        )
        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleSnippetTest(APITestCase):
    def setUp(self):
        self.snippet_four = Snippet.objects.create(
            title="title04", code="code04"
        )

    def test_get_single_snippet(self):
        url = "/snippets/" + str(self.snippet_four.pk) + "/"
        response = self.client.get(url, format="json")
        factory = APIRequestFactory()
        request = factory.get("/")
        snippet = Snippet.objects.get(pk=self.snippet_four.pk)
        serializer_context = {
            "request": Request(request),
        }
        serializer = SnippetSerializer(
            instance=snippet, context=serializer_context
        )
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateSnippetTest(APITestCase):
    def setUp(self):
        self.snippet_five_payload = {"title": "title05", "code": "code05"}
        self.admin_one_mock = {
            "username": "admin1",
            "email": "admin1@example.com",
            "password": "111111",
        }
        self.admin_one = User.objects.create_superuser(
            self.admin_one_mock["username"],
            self.admin_one_mock["email"],
            self.admin_one_mock["password"],
        )

    def test_create_snippet(self):
        url = "/snippets/"
        self.client.login(
            username=self.admin_one.username,
            password=self.admin_one_mock["password"],
        )
        response = self.client.post(
            url, self.snippet_five_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 1)
        self.assertEqual(
            Snippet.objects.get().title, self.snippet_five_payload["title"]
        )


class UpdateSnippetTest(APITestCase):
    def setUp(self):
        self.admin_two_mock = {
            "username": "admin2",
            "email": "admin2@example.com",
            "password": "222222",
        }
        self.admin_two = User.objects.create_superuser(
            self.admin_two_mock["username"],
            self.admin_two_mock["email"],
            self.admin_two_mock["password"],
        )
        self.client.login(
            username=self.admin_two.username,
            password=self.admin_two_mock["password"],
        )
        self.snippet_six = Snippet.objects.create(
            title="title06", code="code06", owner=self.admin_two
        )
        self.snippet_six_updated = {"title": "title07", "code": "code07"}

    def test_update_snippet(self):
        url = "/snippets/" + str(self.snippet_six.pk) + "/"
        response = self.client.put(
            url, self.snippet_six_updated, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["title"], self.snippet_six_updated["title"]
        )
        self.assertEqual(
            response.data["code"], self.snippet_six_updated["code"]
        )


class DeleteSnippetTest(APITestCase):
    def setUp(self):
        self.admin_three_mock = {
            "username": "admin3",
            "email": "admin3@example.com",
            "password": "333333",
        }
        self.admin_three = User.objects.create_superuser(
            self.admin_three_mock["username"],
            self.admin_three_mock["email"],
            self.admin_three_mock["password"],
        )
        self.client.login(
            username=self.admin_three.username,
            password=self.admin_three_mock["password"],
        )
        self.snippet_seven = Snippet.objects.create(
            title="title07", code="code07", owner=self.admin_three
        )

    def test_delete_snippet(self):
        url = "/snippets/" + str(self.snippet_seven.pk) + "/"
        response = self.client.delete(
            url, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GetAllUserTest(APITestCase):
    def setUp(self):
        self.user_one_mock = {
            "username": "user1",
            "email": "user1@example.com",
            "password": "111111",
        }
        self.user_two_mock = {
            "username": "user2",
            "email": "user2@example.com",
            "password": "222222",
        }
        self.user_three_mock = {
            "username": "user3",
            "email": "user3@example.com",
            "password": "333333",
        }
        self.user_one = User.objects.create_superuser(
            self.user_one_mock["username"],
            self.user_one_mock["email"],
            self.user_one_mock["password"],
        )
        self.user_two = User.objects.create_superuser(
            self.user_two_mock["username"],
            self.user_two_mock["email"],
            self.user_two_mock["password"],
        )
        self.user_three = User.objects.create_superuser(
            self.user_three_mock["username"],
            self.user_three_mock["email"],
            self.user_three_mock["password"],
        )
        self.client.login(
            username=self.user_one.username,
            password=self.user_one_mock["password"],
        )

    def test_get_all_user(self):
        url = "/users/"
        response = self.client.get(url, format="json")
        factory = APIRequestFactory()
        request = factory.get("/")
        users = User.objects.all()
        serializer_context = {
            "request": Request(request),
        }
        serializer = UserSerializer(
            instance=users, context=serializer_context, many=True
        )
        logger.info("multiple user:" + str(response.data))
        self.assertEqual(response.data["results"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleUserTest(APITestCase):
    def setUp(self):
        self.user_four_mock = {
            "username": "user4",
            "email": "user4@example.com",
            "password": "444444",
        }
        self.user_four = User.objects.create_superuser(
            self.user_four_mock["username"],
            self.user_four_mock["email"],
            self.user_four_mock["password"],
        )
        self.client.login(
            username=self.user_four.username,
            password=self.user_four_mock["password"],
        )

    def test_get_single_user(self):
        url = "/users/" + str(self.user_four.pk) + "/"
        response = self.client.get(url, format="json")
        factory = APIRequestFactory()
        request = factory.get("/")
        user = User.objects.get(pk=self.user_four.pk)
        serializer_context = {
            "request": Request(request),
        }
        serializer = UserSerializer(
            instance=user, context=serializer_context
        )
        logger.info("sigle user:" + str(response.data))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
