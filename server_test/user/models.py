from django.db import models
from utils.validator import validator
from sqlite3 import IntegrityError


class CustomUserManager:
    @staticmethod
    def create_user(name, last_name, phone, password, email):
        # Нужна нормальная валидация всего, и пустоты и неправильных символов в имени и фамилии, валидация номера и емейла, и пароля.
        # Так же нужна проверка уникальности для номера телефона и емейла.
        if not name:
            return False, "No name value."
        if not last_name:
            return False, "No last_name value."
        if not phone:
            return False, "No phone value."
        if not password:
            return False, "No password value."
        try:
            user = NewUser(name=name, last_name=last_name, phone=phone, password=password, email=email)
            user.save()
            return True, "User created."
        except IntegrityError:
            return False, "Creating user error."


class NewUser(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    # optional
    email = models.CharField(max_length=100,
                             blank=True,
                             null=True)

    manager = CustomUserManager()

    def str(self):
        return self.name
