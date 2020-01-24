from django.contrib import admin

# Register your models here.
import models

admin.site.register(models.Slider)
admin.site.register(models.Video)
admin.site.register(models.Classification)
admin.site.register(models.Direction)

