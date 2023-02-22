from django.contrib import admin
from applications.feedback.models import *
from .models import Like


admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Like)


