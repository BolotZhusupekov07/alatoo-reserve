from django.contrib.auth import get_user_model

User = get_user_model()


def register_user(email, password, name=None, surname=None):
    User.objects.create_user(
        email=email, password=password, name=name, surname=surname
    )
