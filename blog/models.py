from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify


#ManyToOne
#ManyToMany
#OneToOne

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها'



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    category = models.ManyToManyField(Category, related_name='posts', verbose_name='دسته بندی')
    title = models.CharField(max_length=70 , verbose_name='عنوان')
    body = models.TextField()
    image = models.ImageField(upload_to='images/posts', verbose_name='تصویر', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)


    class Meta:
        ordering = ('-updated', '-created')

        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


    def __str__(self):
        return f"{self.title} - {self.body[:5]} "

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px", height="50px">')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'



class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', verbose_name='پست')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post.title}'

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ['-created']