from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# extending the user model

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)
    subID = models.CharField(max_length=50, null = True)
    def __str__(self):
        return self.user.username


# The Person model is used in the page optin.html and provide the information of the user subscription
class Person(models.Model):
    name = models.CharField(max_length=100) # the name of the user
    country = models.CharField(max_length=30) # the country where the user is located
    email = models.EmailField(max_length=100) # the email of the user
    # print the name of the user in the database
    def __str__(self):
        return self.name

#The construction of the courses form course page; the general view

TYPE = (("free", "free"),
        ("Pro", "Pro"))
NEW = (("yes", "yes"),
       ("no", "no"))
POPULAR = (("yes", "yes"),
           ("no", "no"))
class Course(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    tutor = models.CharField(max_length=100, default = "Name")
    language = models.CharField(max_length=100, default = "English")
    upload_date = models.DateField()
    description = models.TextField()
    thumbnail_url = models.CharField(max_length=1000)
    type_course = models.CharField(choices = TYPE, default = 'free', max_length=30)
    new_course = models.CharField(choices = NEW, default = 'yes', max_length=10)
    course_length = models.CharField(max_length=100)
    total_free_lessons = models.CharField(max_length=100, default="Free lessons: ")
    is_popular = models.CharField(choices= POPULAR, default="no", max_length=10)
    def __str__(self):
        return self.title

#Every course has sections; those sectionhasmultiple lessons
LESSONS_FREE = (("yes", "yes"),
        ("no", "no"))
class Section(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    free_count_lessons = models.CharField(choices = LESSONS_FREE, default = 'no', max_length=30)
    def __str__(self):
        return self.title


PREVIEW = (("yes", "yes"),
        ("no", "no"))
# every course has multiple lessons, a lesson will be defined by a course and a section, Lessons model extends Course and Section model
class Lessons(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.CharField(max_length=1000)
    lesson_description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null = True)
    preview = models.CharField(choices = PREVIEW, default = 'no', max_length=30)
    def __str__(self):
        return self.title
 
class Notes(models.Model):
    user_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100, null = True)
    lesson_name = models.CharField(max_length=100, null = True)
    notes = models.TextField()
    def __str__(self):
        return self.user_name