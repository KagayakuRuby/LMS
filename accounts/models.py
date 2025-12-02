from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin
from blog.models import *

class CustomUserManager(BaseUserManager):
    def _create_user(self,phone,password=None,**extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,phone,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self,phone,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('is_active must have is True.')

        return self._create_user(phone, password, **extra_fields)





class User(AbstractBaseUser , PermissionsMixin):
    phone = models.CharField(max_length=15, unique=True ,verbose_name='شماره تلفن')
    first_name = models.CharField(max_length=20, null=True , blank=True)
    last_name = models.CharField(max_length=20, null=True , blank=True)
    is_active =models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

# class Article(BaseModel):
#     title = models.CharField(max_length=200 , verbose_name='عنوان')
#     author = models.ForeignKey(User,verbose_name='نویسنده',on_delete=models.CASCADE,related_name='articles')
#     content = models.TextField(verbose_name='محتوا')

#     class Meta:
#         verbose_name = 'مقاله'
#         verbose_name_plural ='مقالات'

#     def __str__(self):
#         return self.title