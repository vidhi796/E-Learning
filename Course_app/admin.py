from django.contrib import admin
from Course_app.models import Card_list,Topic,TopicDetail

# Register your models here.

admin.site.register((Card_list,Topic , TopicDetail))