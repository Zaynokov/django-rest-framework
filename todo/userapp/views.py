from rest_framework import mixins, generics
from rest_framework.viewsets import GenericViewSet

from .models import UserModel
from .serializers import UserModelSerializer, StaffUserSerializer


class UserModelViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       GenericViewSet):

    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()


class StaffUserListAPIView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StaffUserSerializer
        return UserModelSerializer
