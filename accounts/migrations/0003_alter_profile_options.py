# Generated by Django 5.0.1 on 2024-03-25 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'حساب کاربری', 'verbose_name_plural': 'حساب های کاربری'},
        ),
    ]
