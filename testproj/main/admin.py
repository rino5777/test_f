
from django.contrib import admin

# Register your models here.

from .models import Skill, Value_skill, Skills

admin.site.register(Skill)
admin.site.register(Skills)
admin.site.register(Value_skill)