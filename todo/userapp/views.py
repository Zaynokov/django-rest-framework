from rest_framework.viewsets import ModelViewSet

from .models import UserModel


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModel
    queryset = UserModel.objects.all()
