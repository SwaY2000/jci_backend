from django.contrib import admin

from .models import MainDonate, DonationDonate, ProjectDonate, ProjectsDonate, FooterDonate

admin.site.register(MainDonate)
admin.site.register(DonationDonate)
admin.site.register(ProjectDonate)
admin.site.register(ProjectsDonate)
admin.site.register(FooterDonate)
