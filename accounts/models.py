from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager , PermissionManager


class CustomUserManager(BaseUserManager):
    def _create_user(self,phone,password=None,**extrafields):
        if not phone:
            raise ValueError('The Phone field must be set')
        user = self.model(phone=phone, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user


# class User()