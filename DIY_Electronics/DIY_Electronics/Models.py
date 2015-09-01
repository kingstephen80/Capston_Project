__author__ = 'kings_000'

from django.db import models


class BlogPost(models.Model):
    text_main = models.TextField(max_length=365)
    author = models.User
    date = models.DateTimeField
    topic = models.CharField(choices=Arduino,RaseberryPi,Intel-Galileo)
    user_comments = models.TextField(max_length=130)


class Projects(models.Model):
    title = models.CharField(60)
    author = models.Users
    date = models.DateTimeField
    difficulty = models.CharField(choices=)
    instructions = models.TextField(max_length=365)
    tool_list = models.CharField(max_length=180)
    parts_list = models.CharField(max_length=180)
    scripts_code = models.TextField(max_length=365)
    script_language = models.CharField(max_length=180)


class User(models.User):
    first_name = User.first_name
    last_name = user.last_name
    email = user.email
    userName = user.userName
    password = user.password



