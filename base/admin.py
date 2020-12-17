from django.contrib import admin
from django.contrib.auth.models import Group, User
from .views import TwoFAAdmin
from django_otp.plugins.otp_totp.models import TOTPDevice

admin.site.site_header = "Dashboard"
admin.site.unregister(Group)

admin_site = TwoFAAdmin(name="OTPAdmin")
admin_site.register(User)
admin_site.register(TOTPDevice)
