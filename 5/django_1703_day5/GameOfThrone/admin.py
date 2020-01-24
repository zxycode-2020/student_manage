from django.contrib import admin

# Register your models here.

import models

admin.site.register(models.Student)
admin.site.register(models.Class)
admin.site.register(models.Group)