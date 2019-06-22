from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_time = models.DateField(auto_now_add=True)

    publish = models.ForeignKey(to='Publish')
    authors = models.ManyToManyField(to='Author')


    def __str__(self):
        return '书籍对象的名字:%s'%self.title
class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return '出版社对象的名字:%s'%self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    authordetail = models.OneToOneField(to='AuthorDetail')

    def __str__(self):
        return '作者对象的名字:%s'%self.name


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=32)

    def __str__(self):
        return '作者详情对象的名字:%s'%self.phone