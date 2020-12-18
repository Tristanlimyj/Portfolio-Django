from django.contrib import admin
from django.contrib.auth.models import Group, User
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
# No 2FA Edits
admin.site.site_header = "Dashboard"
admin.site.unregister(Group)

# With 2FA Edits
class TwoFALogin(OTPAdminSite):
    site_header = "Dashboard"

two_FA_admin = TwoFALogin(name='otp_admin')
two_FA_admin.register(TOTPDevice)
two_FA_admin.register(User)
