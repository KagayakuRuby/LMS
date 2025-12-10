from django.db import models
from django.utils import timezone



class TimeStamp(models.Model):
    create_at = models.DateField(auto_created=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateField(auto_created=True,verbose_name='تاریخ بروزرسانی')

    class Meta:
        abstract = True


class BaseModel(TimeStamp):
    is_active = models.BooleanField(default=True , verbose_name='فعال')

    class Meta:
        abstract = True

class Author(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام نویسنده")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان کتاب")
    author = models.ForeignKey(Author , on_delete=models.CASCADE,verbose_name="نویسنده")

    def __str__(self):
        return self.title
    

class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,verbose_name="کتاب")
    rating = models.IntegerField(verbose_name="امتیاز")
    comment = models.TextField(verbose_name="نظر")
    is_deletedd = models.BooleanField(default=False,verbose_name="حذف شده")

    def __str__(self):
        return f"Review for {self.book.title} by {self.rating} rate"
    def delete(self):
        self.is_deletedd = True
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    slug = models.SlugField(max_length=128,unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['-name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='products')
    slug = models.SlugField(max_length=128,unique=True)
    price = models.PositiveIntegerField()

    class Meta:
        ordering =['price']


    def __str__(self):
        return str(self.price)