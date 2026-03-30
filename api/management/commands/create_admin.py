from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            user = User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin"
            )

            self.stdout.write("✅ Superuser admin créé")
        else:
            self.stdout.write("⚠️ Admin existe déjà")