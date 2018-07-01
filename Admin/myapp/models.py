from django.db import models

# Create your models here.
# 出版社类
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

# 书籍类
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # 创建外键

# 作者类
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    # 一个作者对应多本书，一本书可以有多个作者，多对多，在数据库中创建第三张表
    book = models.ManyToManyField(Book, through='BookToAuthor')

class BookToAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)