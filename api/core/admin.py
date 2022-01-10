from django.contrib import admin

from .models import *

admin.site.register(Meal)
admin.site.register(Activity)
admin.site.register(ActivityUser)
admin.site.register(MealUser)
