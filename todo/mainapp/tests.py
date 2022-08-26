from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from mainapp.models import ProjectModel
from mainapp.views import ProjectModelViewSet
from userapp.models import UserModel


class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = UserModel.objects.create_user('Miha', 'Miha@mail.ru', 'qwerflgkjnbl32k23tlnl2')
        self.client = APIClient()
        self.project = mixer.blend(ProjectModel)

    def test_factory_get_list(self):
        request = self.factory.get('api/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_factory_create_guest(self):
        request = self.factory.post(
            'api/projects/',
            {'name': 'new', 'repository': '', 'users': [1]},
            format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_client_get_detail(self):
        response = self.client.get(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestNoteViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
