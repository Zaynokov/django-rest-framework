from rest_framework.viewsets import ModelViewSet

from .models import ProjectModel, NoteModel
from .serializers import ProjectModelSerializer, NoteModelSerializer


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = ProjectModel.objects.all()


class NoteModelViewSet(ModelViewSet):
    serializer_class = NoteModelSerializer
    queryset = NoteModel.objects.all()
