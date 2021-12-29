from django.contrib import admin
from .models import *

admin.site.register(Ideas)
admin.site.register(Comments)
admin.site.register(PersonalProject)
admin.site.register(Stage_of_PersonalProject)
admin.site.register(Task_of_PersonalProject)
