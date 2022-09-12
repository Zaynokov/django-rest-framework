import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from mainapp.models import NoteModel, ProjectModel
from userapp.models import UserModel


class NoteType(DjangoObjectType):
    class Meta:
        model = NoteModel
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = ProjectModel
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = '__all__'


class ProjectUpdateMutation(graphene.Mutation):
    class Arguments:
        repository = graphene.String()
        id = graphene.ID()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        project = ProjectModel.objects.get(id=kwargs.get('id'))
        project.repository = kwargs.get('repository')
        project.save()
        return cls(project=project)


class ProjectCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        repository = graphene.String()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        project = ProjectModel.objects.create(**kwargs)
        return cls(project=project)


class ProjectDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    projects = graphene.List(ProjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        ProjectModel.objects.get(id=kwargs.get('id')).delete()
        return cls(projects=ProjectModel.objects.all())


class Mutations(ObjectType):
    update_project = ProjectUpdateMutation.Field()
    create_project = ProjectCreateMutation.Field()
    delete_project = ProjectDeleteMutation.Field()


class Query(ObjectType):

    all_notes = graphene.List(NoteType)
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)

    project_by_name = graphene.List(ProjectType, name=graphene.String(required=False))

    def resolve_all_notes(root, info):
        return NoteModel.objects.all()

    def resolve_all_projects(root, info):
        return ProjectModel.objects.all()

    def resolve_project_by_name(root, info, name=None):
        if name:
            return ProjectModel.objects.get(name=name)
        return ProjectModel.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations)
