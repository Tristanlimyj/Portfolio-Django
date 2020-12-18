from django.contrib import admin
from django.contrib.auth.models import Group

# No 2FA Edits
admin.site.site_header = "Dashboard"
admin.site.unregister(Group)
