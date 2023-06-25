from django.db import models


class FieldModel(models.Model):
    class Meta:
        db_table = 'main_page_fields'
    # achievements_block
    support = models.CharField(max_length=55, null=True, default='1,5m+')
    helped = models.CharField(max_length=55, null=True, default='9k+')
    partner = models.CharField(max_length=55, null=True, default='25+')
