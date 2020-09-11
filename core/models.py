from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    origin_url = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Forum(models.Model):
    name = models.CharField(max_length=50)
    origin_url = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    parent = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Article(models.Model):
    parent = models.ForeignKey(Forum,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    origin_url = models.CharField(max_length=200)

class Language(models.Model):
    langcode = models.CharField(max_length=3)
    fullName = models.CharField(max_length=30)

class TranslatedArticle(models.Model):
    parent = models.ForeignKey(Article, on_delete=models.CASCADE)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)    
    slug = models.CharField(max_length=200)

class Question(models.Model):
    parentArticle = models.ForeignKey(TranslatedArticle,on_delete=models.CASCADE)
    content = models.TextField()

class Answer(models.Model):
    parentArticle = models.ForeignKey(TranslatedArticle,on_delete=models.CASCADE)
    content = models.TextField()
