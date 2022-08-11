from rest_framework import pagination


class ProjectModelLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 10


class NoteModelLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 20
