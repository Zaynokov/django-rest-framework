from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import UserModel
from .serializers import UserModelSerializer


class UserModelViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       GenericViewSet):

    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()
