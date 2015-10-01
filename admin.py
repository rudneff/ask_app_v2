from django.contrib import admin
from ask_app.models import *

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tags)
admin.site.register(User)