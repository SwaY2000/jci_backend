# Generated by Django 4.2.1 on 2023-07-06 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, null=True)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='multimedia')),
            ],
        ),
        migrations.RenameModel(
            old_name='FieldModel',
            new_name='Achievement',
        ),
        migrations.AlterModelTable(
            name='achievement',
            table=None,
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('url', models.URLField()),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='main_page.multimedia')),
            ],
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('subtitle', models.CharField(max_length=255, null=True)),
                ('show_ua_flag', models.BooleanField(default=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='main_page.multimedia')),
            ],
        ),
        migrations.CreateModel(
            name='JCIUkrainePresident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, null=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jci_ukraine_presidents', to='main_page.multimedia')),
            ],
        ),
    ]