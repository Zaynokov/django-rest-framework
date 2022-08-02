import mimesis
from django.core.management import BaseCommand

from userapp.models import UserModel

quantity = 20


class Command(BaseCommand):
    def handle(self, *args, **options):
        UserModel.objects.all().delete()
        person = mimesis.Person('ru')
        for _ in range(quantity):
            UserModel.objects.create_user(
                username=person.username(),
                first_name=person.first_name(),
                last_name=person.last_name(),
                email=person.email(unique=True),
                password=person.password()
            )

        UserModel.objects.create_superuser('Admin', 'admin@mail.ru', 'AdminR12345')

