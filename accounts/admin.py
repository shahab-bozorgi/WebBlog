from django.contrib import admin
from accounts.models import Profile

admin.site.register(Profile)

admin.site.site_header = 'مدیریت وبلاگ'
