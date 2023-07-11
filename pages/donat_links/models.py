from django.db import models

class MainDonate(models.Model):
    hero_banner_link = models.URLField(max_length=255, null=True, default='www')
    to_help_link = models.URLField(max_length=255, null=True, default='www')
class DonationDonate(models.Model):
    donate_link = models.URLField(max_length=255, null=True, default='www')
class ProjectDonate(models.Model):
    donate_link = models.URLField(max_length=255, null=True, default='www')
class ProjectsDonate(models.Model):
    donate_link = models.URLField(max_length=255, null=True, default='www')
class FooterDonate(models.Model):
    donate_link = models.URLField(max_length=255, null=True, default='www')
