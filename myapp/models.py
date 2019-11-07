from django.db import models

# Create your models here.

class Search_content(models.Model):
    title = models.CharField(max_length=28)
    content =  models.CharField(max_length=60)
    imgPath = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'search_content'
        verbose_name_plural = verbose_name

class User_infor(models.Model):
    #ID = models.CharField(max_length=20, unique='True')
    GENDER =  models.CharField(max_length=20)
    SCHOOL = models.CharField(max_length=16)
    F_EDUCATION = models.CharField(max_length=16)
    M_EDUCATION = models.CharField(max_length=16)
    F_CAREER = models.CharField(max_length=16)
    M_CAREER = models.CharField(max_length=16) 

    class Meta:
        verbose_name = 'User_infor'
        verbose_name_plural = verbose_name
