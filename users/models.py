from django.db import models

# from django.contrib.auth.models import User


class Info(models.Model):
    name = models.CharField(max_length=30)
    gender = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "users_info"
        unique_together = ['name', 'gender', 'age']


# class Class(models.Model):
#     subject = models.CharField(max_length=255)
#     last_updated = models.DateTimeField(auto_now_add=True)
#     info = models.ForeignKey(Info, related_name='class')
#     starter = models.ForeignKey(User, related_name='class')

# class Post(models.Model):
#     message = models.TextField(max_length=4000)
#     topic = models.ForeignKey(Topic, related_name='posts')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(null=True)
#     created_by = models.ForeignKey(User, related_name='posts')
#     updated_by = models.ForeignKey(User, null=True, related_name='+')
