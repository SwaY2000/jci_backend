from django.db import models


class Achievement(models.Model):
    support = models.CharField(max_length=55, null=True, default='1,5m+')
    helped = models.CharField(max_length=55, null=True, default='9k+')
    partner = models.CharField(max_length=55, null=True, default='25+')


class Multimedia(models.Model):
    photo = models.ImageField(upload_to='multimedia', max_length=100)


class MainBanner(models.Model):
    title = models.CharField(max_length=255, null=True)
    subtitle = models.CharField(max_length=255, null=True)
    photo = models.ForeignKey(Multimedia, on_delete=models.CASCADE, related_name='banners')
    show_ua_flag = models.BooleanField(default=True)


class JCIUkrainePresident(models.Model):
    text = models.CharField(max_length=255, null=True)
    photo = models.ForeignKey(Multimedia, on_delete=models.CASCADE, related_name='jci_ukraine_presidents')


class Partner(models.Model):
    name = models.CharField(max_length=255, null=True)
    url = models.URLField()
    logo = models.ForeignKey(Multimedia, on_delete=models.CASCADE, related_name='partners')


class FAQ(models.Model):
    question = models.CharField(max_length=255, null=True)
    answer = models.TextField()
