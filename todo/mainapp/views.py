from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectModelFilter, NoteModelFilter
from .models import ProjectModel, NoteModel
from .paginations import ProjectModelLimitOffsetPagination, NoteModelLimitOffsetPagination
from .serializers import ProjectModelSerializer, NoteModelSerializer


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = ProjectModel.objects.all()
    filterset_class = ProjectModelFilter
    pagination_class = ProjectModelLimitOffsetPagination


class NoteModelViewSet(ModelViewSet):
    serializer_class = NoteModelSerializer
    queryset = NoteModel.objects.all()
    filterset_class = NoteModelFilter
    pagination_class = NoteModelLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        note = get_object_or_404(NoteModel, pk=kwargs['pk'])
        note.is_active = False
        note.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
