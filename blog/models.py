from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100,verbose_name="عنوان")
    blog = models.TextField(verbose_name="متن پست")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=100)
    price = models.IntegerField
    price_2 = models.PositiveBigIntegerField()
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='blog_images/',blank=True,null=True)
    txt = models.JSONField(blank=True,null=True)

   
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        ordering = ['-created_at']


    def __str__(self):
        return self.blog
    

    class Article(models.Model):
        STATUS_CHOICE = (
            ('0','پیش نویس'),
            ('1','منتشر شده'),
            ('2','آرشیو'),
            )
        title = models.CharField(max_length=200,verbose_name="عنوان")
        status = models.CharField(max_length=1,choices=STATUS_CHOICE,default='0',verbose_name="وضعیت")

        def __str__(self):
            return f"{self.title} - {self.get_status_display()}"