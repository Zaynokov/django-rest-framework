from rest_framework import serializers

from .models import ProjectModel, NoteModel


class ProjectModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectModel
        fields = '__all__'


class NoteModelSerializer(serializers.ModelSerializer):

    is_active = serializers.HiddenField(default=True)

    class Meta:
        model = NoteModel
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(NoteModelSerializer, self).to_representation(instance)
        rep['is_active'] = 'Active' if instance.is_active else 'Closed'
        rep['project'] = instance.project.name
        return rep