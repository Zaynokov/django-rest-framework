from django_filters import rest_framework as filters

from mainapp.models import ProjectModel, NoteModel


class ProjectModelFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ProjectModel
        fields = ['name']


class NoteModelFilter(filters.FilterSet):

    project = filters.ModelChoiceFilter(queryset=ProjectModel.objects.all())

    class Meta:
        model = NoteModel
        fields = ['project']
