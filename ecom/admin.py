from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Lessons)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Notes)
