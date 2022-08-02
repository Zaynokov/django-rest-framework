from rest_framework.viewsets import ModelViewSet

from .models import UserModel
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()
